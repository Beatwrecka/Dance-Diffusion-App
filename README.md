# Dance Diffusion Mac App (Prototype)

A local macOS-friendly UI for training and generating audio using diffusion models.

## 🔧 Features

- 🔹 HTML/CSS/JS front-end (with Tailwind UI)
- 🔹 Python Flask backend (placeholder for now)
- 🔹 Ready to expand into:
  - Style transfer
  - Spectrogram previews
  - Real-time audio generation

## 🧠 Goals

This repo is structured to:
- Be split into modular frontend + backend
- Support AI coding assistants (like Codex or Copilot)
- Eventually integrate Apple Silicon optimizations (MPS, CoreML)

## 🚀 Setup

### Frontend
Open `index.html` directly in browser OR use VS Code Live Server.

### Backend
```bash
pip install flask
python app.py
```

Then POST to:
```
http://127.0.0.1:5000/generate
```

## 📂 Structure (WIP)
```
📁 root/
├── index.html
├── style.css
├── main.js
├── app.py
├── .gitignore
├── README.md
```
