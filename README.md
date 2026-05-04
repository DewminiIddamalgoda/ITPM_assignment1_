# ITPM Assignment 1 – Transliteration Accuracy Testing

## Overview

This project automates the testing of the **Chat Sinhala Transliteration** function available at:  
🔗 [https://www.pixelssuite.com/chat-translator](https://www.pixelssuite.com/chat-translator)

The objective is to evaluate how accurately the application converts **chat-style Singlish input** into **Sinhala output** using [Playwright](https://playwright.dev/python/) for browser automation. The test cases focus on **negative scenarios** — inputs where the system fails to produce correct transliterations.

---

## Prerequisites

Before running the tests, ensure the following are installed on your system:

| Requirement        | Version              | Notes                                              |
|--------------------|----------------------|----------------------------------------------------|
| **Python**         | 3.11 or 3.12         | [Download Python](https://www.python.org/downloads/) |
| **Google Chrome**  | Latest recommended   | Or let Playwright install Chromium automatically    |
| **pip**            | Latest               | Comes with Python; will be upgraded in setup        |

---

## Project Structure

```
ITPM_assignment1_/
├── test_automation.py                       # Playwright automation script
├── It23578500_Assignment_1_Test_Cases_.xlsx  # Excel file with test cases and results
├── README.md                                # This file
└── .gitignore                               # Git ignore rules
```

---

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/DewminiIddamalgoda/ITPM_assignment1_.git
cd ITPM_assignment1_
```

### 2. Upgrade pip

```bash
pip install -U pip
```

### 3. Install Required Python Packages

```bash
pip install playwright openpyxl
```

### 4. Install Playwright Browsers

```bash
playwright install
```

> **Note:** This will download the Chromium, Firefox, and WebKit browsers needed by Playwright. If you only want Chromium, run `playwright install chromium`.

---

## Test Cases

The test cases are recorded in the Excel file: **`It23578500_Assignment_1_Test_Cases_.xlsx`**

### Excel File Structure

| Column | Description |
|--------|-------------|
| **TC ID** | Test case identifier (e.g., `Neg_0001`) |
| **Input length type** | `S` (≤30 chars), `M` (31–299 chars), or `L` (300–450 chars) |
| **Input** | The Singlish input text to be tested |
| **Expected output** | The correct Sinhala transliteration |
| **Actual output** | The output produced by the application (auto-filled by script) |
| **Status** | `PASS` or `FAIL` (auto-filled by script) |
| **Singlish input types covered** | The category of Singlish input type being tested |
| **Evidence or rationale for the input type covered** | Justification for the input type classification |

### Singlish Input Types Covered

The 50 negative test cases cover all **24 Singlish input types** as specified in the assignment:

1. Question forms
2. Command forms
3. Greetings
4. Requests
5. Responses
6. Repeated words
7. Inputs with punctuation marks
8. Romanization / Spelling variants
9. Isolated English word insertions in Singlish
10. Multi-word English phrases in Singlish
11. English digital terms in Singlish
12. Platform/App names in Singlish
13. English abbreviations/acronyms in Singlish
14. English clipped forms in Singlish
15. Place names embedded in Singlish
16. Person names embedded in Singlish
17. Inputs with numbers and numeric suffixes
18. Inputs with currency
19. Inputs with time formats
20. Inputs with dates
21. Inputs with unit of measurements
22. Inputs with slang and casual phrasing
23. Online identifiers in Singlish
24. Inputs containing emojis

---

## Running the Tests

### Basic Command

From the project root directory, run:

```bash
python test_automation.py --excel "It23578500_Assignment_1_Test_Cases_.xlsx" --url "https://www.pixelssuite.com/chat-translator" --wait-ms 5000 --type-delay-ms 80 --slow-mo-ms 200 --save-every 1 --keep-open
```

### Command-Line Options

| Flag | Default | Description |
|------|---------|-------------|
| `--excel` | Auto-detected | Path to the Excel file with test cases |
| `--url` | `https://www.pixelssuite.com/chat-translator` | URL of the transliteration tool |
| `--wait-ms` | `5000` | Wait time (ms) after each transliteration for output to appear |
| `--type-delay-ms` | `30` | Delay (ms) between keystrokes when typing input |
| `--slow-mo-ms` | `0` | Playwright slow-motion delay (ms) for visual debugging |
| `--save-every` | `0` | Save Excel after every N test cases (0 = save only at end) |
| `--keep-open` | `false` | Keep the browser open after test execution |
| `--headless` | `false` | Run in headless mode (no browser UI) |
| `--retries` | `8` | Number of retries to read the output |
| `--retry-wait-ms` | `1000` | Wait time (ms) between retries |
| `--timeout-ms` | `60000` | Overall timeout (ms) for page operations |

### Example: Headless Mode

```bash
python test_automation.py --excel "It23578500_Assignment_1_Test_Cases_.xlsx" --headless --wait-ms 5000
```

---

## Checking Results

After the script completes:

1. Open **`It23578500_Assignment_1_Test_Cases_.xlsx`**
2. The **Actual output** and **Status** columns will be automatically populated
3. Review the results — `PASS` means actual matches expected, `FAIL` means they differ

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `playwright` not found | Run `pip install playwright` and `playwright install` |
| Browser fails to launch | Ensure Chrome is installed, or run `playwright install chromium` |
| Excel file not found | Verify the file path in the `--excel` argument |
| Timeout errors | Increase `--wait-ms` and `--timeout-ms` values |
| Site not loading | Check your internet connection and verify the URL is accessible |

---

## Author

**Registration Number:** IT23578500

---