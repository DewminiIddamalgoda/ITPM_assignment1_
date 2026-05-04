import openpyxl
from playwright.sync_api import sync_playwright
import time

# Load Excel file
wb = openpyxl.load_workbook('It23578500_Assignment_1_Test_Cases_.xlsx')
ws = wb['Test cases']

# Extract inputs
inputs = []
for row in range(2, ws.max_row + 1):
    input_val = ws.cell(row=row, column=3).value
    if input_val:
        inputs.append((row, str(input_val).strip()))

print(f"Found {len(inputs)} inputs to test")

# Run each input through the transliteration system
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    try:
        # Open the transliteration website
        page.goto("https://www.pixelssuite.com/chat-translator", wait_until="domcontentloaded")
        page.wait_for_load_state("networkidle", timeout=30000)
        page.wait_for_selector("textarea", timeout=30000)
        print("Website loaded successfully")
        
        # Find the input and output textareas
        input_locator = page.locator('textarea[placeholder*="English"]').first
        output_locator = page.locator('textarea[placeholder*="Sinhala"]').first
        action_locator = page.get_by_role("button", name="Transliterate").first
        
        # Test each input
        for row_num, input_text in inputs:
            print(f"Testing Row {row_num}: {input_text}")
            
            try:
                # Clear input and type new text
                input_locator.click()
                page.keyboard.press("Control+A")
                page.keyboard.press("Backspace")
                input_locator.fill(input_text)
                
                # Click transliterate button
                action_locator.click()
                
                # Wait for output
                page.wait_for_timeout(3000)
                
                # Get output
                try:
                    actual_output = output_locator.input_value()
                    if not actual_output:
                        actual_output = output_locator.inner_text()
                    if not actual_output:
                        actual_output = output_locator.text_content()
                    
                    actual_output = str(actual_output).strip() if actual_output else ""
                    
                except:
                    actual_output = ""
                
                # Get expected output from Excel
                expected_output = ws.cell(row=row_num, column=4).value
                expected_output = str(expected_output).strip() if expected_output else ""
                
                # Compare expected vs actual output and set status
                if expected_output and actual_output:
                    status = "PASS" if actual_output == expected_output else "FAIL"
                elif actual_output:
                    status = "FAIL"  # Has output but no expected to compare
                else:
                    status = "FAIL"  # No output
                
                # Update Excel
                ws.cell(row=row_num, column=5).value = actual_output  # Actual output column
                ws.cell(row=row_num, column=6).value = status  # Status column
                
                print(f"  -> Output: {actual_output}")
                
            except Exception as e:
                print(f"  -> Error: {e}")
                ws.cell(row=row_num, column=6).value = "ERROR"
            
            # Small delay between tests
            time.sleep(1)
        
        # Save results
        wb.save('It23578500_Assignment_1_Test_Cases_.xlsx')
        print("Results saved to Excel file")
        
    except Exception as e:
        print(f"Error loading website: {e}")
    
    browser.close()

print("Test execution completed")
