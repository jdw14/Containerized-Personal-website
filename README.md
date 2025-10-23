# John Wrightsman - Flask Personal Portfolio Website

A Flask-based personal portfolio website showcasing my projects, background, and skills. This version uses Flask routing to dynamically render all pages instead of static HTML navigation.

---

## 🚀 How to Run This Flask App

### Option 1: Local Development (Recommended)

1. Clone or Download this repository to your computer.
   git clone <your-repo-url>
   cd <project-folder>

2. Create a Virtual Environment (recommended for isolated dependencies):
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate

3. Install Flask (and any required dependencies):
   pip install flask

4. Run the Flask App:
   # Option 1: Using Python
   python app.py

   # Option 2: Using Flask CLI
   flask --app app run

5. Open your browser and visit:
   http://127.0.0.1:5000

6. Deactivate the virtual environment when done:
   deactivate

---

### Option 2: VS Code Integrated Terminal

If using Visual Studio Code:
1. Open the project folder in VS Code
2. Open a terminal inside VS Code
3. Activate your virtual environment (venv\Scripts\activate or source venv/bin/activate)
4. Run the app with python app.py
5. Click the local link in the terminal to preview your Flask site

---

## 🧩 Project Structure

├── app.py                 # Main Flask application
├── /templates             # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── about.html
│   ├── resume.html
│   ├── projects.html
│   ├── contact.html
│   └── thankyou.html
├── /static                # Static assets (CSS, images, JS)
│   ├── css/
│   └── images/
└── venv/                  # Virtual environment (optional, not included in repo)

---

## 🌐 Browser Compatibility
- Chrome (recommended)
- Firefox
- Safari
- Edge
- Mobile browsers

---

## 🛠️ Technologies Used
- Python 3.x – Backend logic and routing
- Flask – Web framework
- HTML5 & Jinja2 – Template rendering
- CSS3 – Custom styling and responsive layout
- Bootstrap 5.3.2 – Front-end framework
- Font Awesome 6.4.0 – Icons
