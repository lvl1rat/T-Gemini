# 🧠 Gemini CLI Prompt Tool

This is a simple command-line tool written in Python that allows you to interact with the **Google Gemini API** via prompts. You can input prompts manually or pass them as arguments, and optionally save the output to a file using the `-o` flag.

## 🚀 Features

- Interact with Gemini 2.0 Flash using your API key
- Prompt input via terminal or command-line arguments
- Save responses to a file with `-o <filename>`
- Automatically stores and reuses your API key via `API.txt`
- Clean JSON parsing and terminal output

---

## 📦 Requirements

- Python 3.6+
- `curl` installed and available in your system PATH

---

## 🛠️ Setup

1. Clone or download the project.
2. Install required tools (Python + `curl`).
3. Run the script:
   ```bash
   python terminal_gemini.py

On first run, you’ll be prompted to enter your GEMINI API key. It will be stored in API.txt for future use.
(https://aistudio.google.com/apikey)