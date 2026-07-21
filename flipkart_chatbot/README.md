# Flipkart Customer Support Chatbot (Flask)

## Folder structure
```
flipkart_chatbot/
├── app.py
├── chatbot.py
├── templates/
│   └── index.html
└── static/
    ├── style.css
    └── script.js
```

## How to run

1. Install Flask (if not already installed):
   ```
   pip install flask
   ```

2. Navigate into the project folder:
   ```
   cd flipkart_chatbot
   ```

3. Run the app:
   ```
   python app.py
   ```

4. Open your browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

## What was fixed from the original code
- `index.html`: Jinja2 template tags were written as `({...})` instead of `{{ ... }}`, so CSS/JS never loaded. Also fixed a malformed viewport meta tag.
- `script.js`: Raw HTML was being concatenated directly into JavaScript (invalid syntax) instead of using template literals with backticks. Also `$(message)` was corrected to `${message}` (template literal interpolation).
- `style.css`: Added `display: flex; flex-direction: column;` to `.chat-box` so `align-self` on messages actually aligns them left/right.
