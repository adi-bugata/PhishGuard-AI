# 🛡️ PhishGuard AI

**Understand suspicious messages before you act.**

PhishGuard AI is a cybersecurity awareness prototype that helps non-experts recognise potential warning signs in suspicious messages and understand safer next steps.

It uses a local, rule-based scanner to identify patterns commonly associated with phishing and other suspicious messages. It is an educational first-check assistant, not a security certification tool.

## 🎯 Problem

People regularly receive unexpected messages about accounts, deliveries, payments, rewards and verification. Some messages use pressure or misleading instructions to encourage unsafe actions.

Many people may not recognise these warning signs.

PhishGuard AI aims to make basic cybersecurity awareness easier to understand through simple explanations and practical safety guidance.

## ✨ Features

- **Message analysis:** Paste a message for a local warning-sign scan.
- **Direct warning signs:** Identifies patterns involving urgency, threats, credentials or verification, payment requests, links or attachments, sensitive information, unexpected rewards and secrecy requests.
- **Contextual signals:** Identifies patterns involving delivery or parcel status, account or service activity, and indirect requests to review details.
- **Evidence snippets:** Highlights relevant portions of the submitted message.
- **Security report:** Displays detected indicators and a cautious assessment.
- **Safe next steps:** Provides practical reminders for handling suspicious messages.
- **Privacy-conscious design:** The scanner does not open links or interact with external systems.

## ⚙️ How it works

1. The user pastes a message into the application.
2. The local scanner checks the text against predefined warning-sign patterns.
3. Matching indicators and relevant text snippets are collected.
4. The application displays a security analysis report.
5. The user receives safe next-step recommendations.

The current implementation is rule-based. It does not establish whether a message is genuinely malicious.

## 🧪 Testing and evaluation

The project includes a set of 10 fictional synthetic test cases.

**Latest local test result:**

- Test cases: 10
- Passed: 10
- Cases requiring a check: 0

All 10 cases matched their expected warning-indicator labels in the local test script.

**Important:** This is a small, manually prepared synthetic test set. It does not represent real-world detection accuracy, and it does not prove that the application can detect every phishing message.

## 🚀 Run locally

### Requirements

- Python 3.10 or newer
- pip
- Streamlit

### Installation

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Create a virtual environment:

   ```bash
   py -m venv .venv
   ```

4. Activate it on Windows:

   ```bash
   .venv\Scripts\activate
   ```

5. Install the dependencies:

   ```bash
   py -m pip install -r requirements.txt
   ```

6. Start the application:

   ```bash
   py -m streamlit run app.py
   ```

7. Open the local address displayed in your terminal.

### Run the synthetic tests

With the virtual environment activated, run:

```bash
py test_local.py
```

The test script compares detected indicators with the expected indicators in `synthetic_test_cases.json`.

## 🔐 Safety and limitations

- Never paste passwords, OTPs, private conversations or sensitive personal information.
- The application does not open URLs or download attachments.
- A detected warning sign is not proof of phishing.
- No detected warning signs does not mean a message is safe.
- The scanner relies on predefined patterns and may miss unfamiliar or cleverly worded messages.
- Important messages should always be verified through independently obtained official contact details or channels.
- The application does not replace professional cybersecurity analysis.

## 🛠️ Technology stack

- Python
- Streamlit
- Regular expressions and rule-based text analysis
- JSON for synthetic test cases

## 🔮 Future improvements

- Multilingual message analysis.
- More comprehensive synthetic test datasets.
- Improved explanations of detected warning signs.
- Carefully evaluated AI-assisted explanations.
- Additional evaluation using diverse, safely sourced examples.

These are planned improvements, not features claimed to be available in the current version.

## 🤝 Acknowledgements

ChatGPT assisted with project planning, code drafting, debugging guidance and documentation. The project owner is responsible for reviewing, testing and understanding the submitted implementation.

## 📌 Current project status

**Working local prototype — synthetic testing completed.**

The application has been launched locally, and all 10 current synthetic test cases passed. Further testing with a larger and more diverse dataset is needed before making broader performance claims.

## 🏗️ Project architecture

PhishGuard AI is organised into three main parts:

### 1. Application — `app.py`

- Provides the Streamlit user interface.
- Accepts pasted message text.
- Runs the local rule-based analysis.
- Identifies direct warning signs and contextual signals.
- Displays evidence snippets, results and safe next steps.

### 2. Test dataset — `synthetic_test_cases.json`

- Contains 10 fictional test messages.
- Stores the expected warning indicators for each message.
- Supports repeatable testing of the scanner.

### 3. Test runner — `test_local.py`

- Loads the synthetic test cases.
- Runs each message through the analysis function.
- Compares detected indicators with expected indicators.
- Reports PASS or CHECK for each test case.

### Workflow

1. User enters a message.
2. The application analyses its text locally.
3. The scanner identifies matching warning patterns.
4. The application prepares a security analysis report.
5. The user receives safe next-step guidance.

### Architecture overview

User input → Streamlit interface → Rule-based analysis → Security report → Safe next steps

The test runner independently evaluates the analysis function using the synthetic dataset.

## 🌐 Live deployment testing

The deployed Streamlit application was manually tested using six fictional messages.

| Test scenario | Expected result | Live result |
|---|---|---|
| Suspicious account message | 4 direct indicators | PASS |
| Ordinary library reminder | No indicators | PASS |
| Ambiguous parcel delivery | 2 contextual signals | PASS |
| Parcel payment request | 1 direct indicator | PASS |
| Account update request | 1 direct + 2 contextual signals | PASS |
| Password and OTP request | 1 direct indicator | PASS |

**Result: 6 out of 6 test cases matched their expected indicator results.**

These tests demonstrate that the deployed application behaved as expected on the selected examples. They do not establish real-world phishing detection accuracy.