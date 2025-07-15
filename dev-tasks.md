# 🛠️ Dance Diffusion — Dev Tasks

## ✅ Current Goal
Refactor monolithic `index.html` into modular frontend + Flask backend.

---

## 📦 Tasks

### 1. HTML Refactor
- [ ] Extract `header`, `nav`, and tab sections into partial HTML files
- [ ] Create: `train.html`, `generate.html`, `community.html`
- [ ] Dynamically load each tab via JS fetch()

### 2. Structure & File Organization
- [ ] Move CSS to `/public/css/style.css`
- [ ] Move JS to `/public/js/main.js`
- [ ] Create `/templates/` folder for HTML components

### 3. Flask Integration
- [ ] Serve static + template files
- [ ] Add `/generate`, `/train` routes (POST, returns mock JSON)
- [ ] Add `/upload` for drag-and-drop audio

### 4. Local Settings
- [ ] Store UI config toggles in `localStorage` (GPU, transfer learning)

---

## ✅ Done
- [x] Split CSS and JS into external files
- [x] Resolved README merge conflict
- [x] Pushed clean main branch to GitHub

---

## 🤖 Codex Ready
This repo is now structured to accept code-gen AI contributions.
