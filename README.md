# IGOR – Data Extraction and Alert System

**IGOR (Intelligent Gmail Observation & Response)** is a lightweight Python-based automation tool that connects to your Gmail inbox, extracts unread messages from a specific sender, and generates customizable alert emails based on the extracted content.

Although currently tailored for Gmail, its modular structure allows adaptation to other data sources and use cases.

---

## Key Features

- Email Monitoring: Uses IMAP to securely fetch unread messages from your Gmail inbox.
- Data Extraction: Extracts subject and body content from emails using Python’s `imaplib` and `email` modules.
- Custom Alerts: Generates personalized alert emails using `smtplib`, prepending “New Alert!” for quick visibility.
- Automation: Once configured, IGOR runs autonomously and processes incoming emails without user interaction.

---

## Usage Example

Imagine receiving security alerts, server logs, or time-sensitive reports by email. IGOR can monitor for these and forward only the most important ones to your phone or another email address in real time.

---

## How It Works

1. Connects to Gmail using IMAP
2. Searches for unread messages from a specific sender
3. Extracts email content (subject and body)
4. Sends a new email alert with the customized message

---

## Applications

- Real-time inbox monitoring
- SMS-based alerting (via email-to-text gateways)
- Notification routing
- Lightweight data aggregation
- Emergency or security alert systems

---

## Limitations

- Requires manual Gmail credentials or app-specific passwords
- Limited to one sender at a time (currently)
- Email-to-SMS alerts depend on cellular data
- Gmail may restrict access without IMAP and proper security setup

---

## Security Notes

- Do not hardcode credentials.
- Use environment variables, encrypted secrets, or OAuth2 for production.
- OAuth2 support is a recommended future upgrade.

---

## Future Improvements

- OAuth2 authentication
- Multi-sender and regex filtering
- CLI or config-file customization
- Modular input/output (email, API, logs, etc.)
- Logging and error handling system

---

## Project Motivation

This project was built to solve a real problem: staying informed through SMS while offline. Though it currently relies on mobile data for delivery via email-to-text, it serves as a solid foundation for larger monitoring and automation workflows.

IGOR is flexible, practical, and lightweight — but has the potential to power more advanced systems.
