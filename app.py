
import re
import streamlit as st

st.set_page_config(page_title="PhishGuard AI", page_icon="🛡️")
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0b1220, #111c30);
    color: #f1f5f9;
}

.block-container {
    max-width: 900px;
    padding-top: 2rem;
}

h1 {
    color: #38bdf8 !important;
    font-weight: 800 !important;
}

h2, h3 {
    color: #7dd3fc !important;
}

.stTextArea textarea {
    background-color: #172338;
    color: white;
    border: 1px solid #334155;
    border-radius: 12px;
}

.stButton button {
    background: linear-gradient(90deg, #0284c7, #2563eb);
    color: white;
    border: none;
    border-radius: 10px;
    font-weight: bold;
    padding: 0.6rem 1rem;
}

.stButton button:hover {
    border: 1px solid #7dd3fc;
    color: white;
}

[data-testid="stMetric"] {
    background: #172338;
    padding: 15px;
    border-radius: 12px;
    border: 1px solid #334155;
}
</style>
""", unsafe_allow_html=True)
st.title("🛡️ PhishGuard AI")
st.caption("Understand suspicious messages before you act.")
st.info("Awareness assistant only. It does not certify whether a message is safe and never opens links.")

RULES = [
    ("Urgent pressure",
     r"\b(urgent|immediately|right away|act now|today only|final notice|expires today)\b",
     "Creates time pressure."),
    ("Threat or consequence",
     r"\b(suspended|deactivated|blocked|terminated|legal action|penalty)\b",
     "Mentions a possible negative consequence."),
    ("Credential or verification request",
 r"\b(password|passcode|otp|one-time code|one-time password|verification code|login code|security code|sign-in code)\b",
 "Mentions credentials or verification codes."),
    ("Payment or financial request",
     r"\b(pay|payment|fee|processing charge|customs duty|bank details|card details|upi|transfer)\b",
     "Mentions money or financial details."),
    ("Link or attachment instruction",
     r"\b(click|tap|open|visit|follow|use)\b.{0,55}\b(link|url|website|attachment|file)\b|       \b(link|url)\s+(below|provided|attached)\b",
     "Encourages using a link or attachment."),
    ("URL present",
    r"https?://\S+|www\.\S+",
    "Contains a web address. Verify the destination independently."),
    ("Sensitive information request",
     r"\b(confirm|update|verify|provide|submit|share)\b.{0,55}\b(address|date of birth|personal details|identity|account details)\b",
     "Appears to request personal information."),
    ("Unexpected reward",
     r"\b(prize|winner|lottery|reward|claim your|free gift)\b",
     "Mentions an unexpected reward."),
    ("Secrecy or bypass request",
     r"\b(keep this secret|do not tell|don't tell|bypass|ignore the usual process)\b",
     "Encourages secrecy or bypassing normal checks."),
]

CONTEXT_RULES = [
    ("Delivery or parcel status",
     r"\b(parcel|package|delivery|shipment|courier)\b.{0,90}\b(delayed|couldn't complete|could not complete|failed|held|attempted|update|review|confirm|details)\b|\b(delivery|parcel|shipment)\s+(details|status|update)\b",
     "Unexpected delivery requests should be checked through the courier's official app or website."),
    ("Account or service activity",
     r"\b(account|profile|subscription|service)\b.{0,90}\b(activity|issue|problem|restricted|review|update|confirm|details)\b",
     "Check account-related requests through the service's official app."),
    ("Indirect request to review details",
     r"\b(review|check|confirm|update)\b.{0,45}\b(your\s+)?(details|information|address|profile|delivery)\b",
     "Unexpected requests to review details should be verified independently."),
]


def find_evidence(message, pattern):
    matches = re.finditer(pattern, message, re.IGNORECASE)
    evidence = []

    for match in matches:
        start = max(0, match.start() - 30)
        end = min(len(message), match.end() + 40)
        evidence.append(message[start:end].strip())

        if len(evidence) == 2:
            break

    return evidence


def analyse(message):
    direct = []
    contextual = []

    for name, pattern, explanation in RULES:
        evidence = find_evidence(message, pattern)

        if evidence:
            direct.append((name, explanation, evidence))

    for name, pattern, explanation in CONTEXT_RULES:
        evidence = find_evidence(message, pattern)

        if evidence:
            contextual.append((name, explanation, evidence))

        # Avoid counting the same credential request twice
    direct_names = [item[0] for item in direct]

    if "Credential or verification request" in direct_names:
        direct = [
            item for item in direct
            if item[0] != "Sensitive information request"
        ]

    return direct, contextual


st.subheader("Analyse a message")

message = st.text_area(
    "Paste the message here",
    height=160,
    placeholder="Paste an unexpected message here."
)


if st.button("Analyse message", type="primary"):

    if not message.strip():
        st.warning("Please paste a message first.")

    else:
        direct, contextual = analyse(message)

        st.divider()
        st.markdown("## 🔍 Security Analysis Report")
        st.caption("Review the detected indicators carefully before taking action.")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("🚨 Direct warning signs", len(direct))

        with col2:
            st.metric("🔎 Contextual signals", len(contextual))

        if direct:
            if len(direct) >= 3:
                st.error("Multiple warning signs")
            else:
                st.warning("Some warning signs")

            st.write(
                "Several patterns commonly associated with "
                "suspicious messages were found."
            )

        elif contextual:
            st.warning("Needs manual verification")

            st.write(
                "This message contains contextual signals "
                "that can appear in both genuine and suspicious "
                "messages. Verify independently."
            )

        else:
            st.info("Insufficient evidence")

            st.write(
                "No patterns in the current rule list were found. "
                "This is not a safety verdict."
            )

        if direct:
            st.markdown("### Direct warning signs")

            for name, explanation, evidence in direct:
                st.markdown(f"**{name}**")
                st.write(explanation)

                for item in evidence:
                    st.code(item)

        if contextual:
            st.markdown("### Contextual signals")

            for name, explanation, evidence in contextual:
                st.markdown(f"**{name}**")
                st.write(explanation)

                for item in evidence:
                    st.code(item)

        st.info(
            "🛡️ Remember: PhishGuard AI identifies warning signs, "
            "not confirmed phishing. Always verify independently."
        )

        st.markdown("### Safe next steps")

        st.markdown("""
        - Do not click unexpected links.
        - Never share passwords or OTPs.
        - Verify requests using an official app or website.
        - Contact the organisation through a trusted channel.
        - Ask a trusted person for help if unsure.
        """)


st.caption(
    "Limitations: This is a rule-based prototype. "
    "It can miss suspicious messages and flag legitimate ones. "
    "Never rely on its result alone."
)
