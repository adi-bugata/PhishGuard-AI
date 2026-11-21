# PhishGuard AI

**Track:** LLM Apps  
**Challenge fit:** C1 — The $15-an-hour expert

PhishGuard AI is an educational first-check assistant. It helps non-experts understand warning signs in suspicious messages and choose safer next steps. It does not certify a message as safe or replace a cybersecurity professional.

## What it does

- Accepts pasted message text (no link opening or external scanning).
- Runs a local warning-sign scan for urgency, credential requests, payment requests, unexpected rewards, link prompts and threats.
- Optionally uses the Gemini API to explain the message in plain language.
- Gives safe, practical next steps.
- Includes a fictional sample message for demonstration.

## Run locally

1. Install Python 3.10 or newer.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Create and activate a virtual environment (recommended).
5. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Start the app:

   ```bash
   streamlit run app.py
   ```

7. Open the local address shown in the terminal.

## Enable AI analysis

Create a Gemini API key through Google AI Studio. Run the app and paste the key into the password field in the sidebar. The key is used only during the current app session and must never be committed to GitHub or shown in a demo recording.

The app uses Google's official `google-genai` Python SDK and the `gemini-3.8-flash` model identifier. Check current model availability for your API account before recording the final demo.

## Evaluation plan

Use only fictional or synthetic messages. Record:
- Number of test messages
- Number where expected warning signs were identified
- Number of missed warning signs
- Number of false alarms
- Whether the AI explanation stayed cautious and gave safe next steps

Do not claim accuracy or performance until you run the tests and record actual results.

## Safety and limitations

- Never paste real personal data, passwords, OTPs, or private conversations.
- The app does not open URLs, download attachments, contact senders, or interact with external systems.
- A warning sign is not proof of phishing; absence of warning signs is not proof of safety.
- AI output may be incomplete or incorrect. Verify important messages independently.

## Tools and acknowledgements

- Python
- Streamlit
- Google Gen AI Python SDK (`google-genai`)
- Gemini API (`gemini-3.8-flash`, subject to account availability)
- ChatGPT: AI-assisted planning, code drafting and documentation. The project owner must review, test and understand all submitted code.

## Current status

Starter implementation. It has not yet been tested in the participant's local environment. Add screenshots, real test results, and a working demo link only after running and verifying the app.
