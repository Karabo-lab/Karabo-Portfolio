# 💼 Karabo Madigoe - Software Engineer and Developer Portfolio

This is my personal portfolio website built with **Flask**, HTML, CSS, and Python.  
It showcases my skills, projects, blog articles, and includes a functional contact form that sends messages to my Gmail inbox using secure environment variables.

---

## 🌐 Live Site

[🔗 View Portfolio Online](https://karabo-portfolio.onrender.com)  

---

## 📁 Project Structure

karabo-portfolio/
├── static/ # CSS, icons, and images
│ ├── style.css
│ └── images/
├── templates/ # HTML pages
│ ├── index.html
│ ├── about.html
│ ├── projects.html
│ └── contact.html
├── .env # Secret credentials 
├── .gitignore
├── app.py # Flask backend
├── requirements.txt # Dependencies
└── README.md

---

## ⚙️ Features

- ✅ Responsive design with a modern dark theme
- ✅ Interactive contact form with Flask + SMTP
- ✅ Skills section with icons and tools
- ✅ Projects page with GitHub links and screenshots
- ✅ Dev Blog page with journal-style post cards
- ✅ Auto-reply confirmation email for messages

---

## 🚀 Tech Stack

- **Python / Flask** for backend
- **HTML / CSS / Jinja2** for frontend
- **SMTP with Gmail App Password** for sending email
- **GitHub + Render** for deployment

---

## 📬 Contact Form Setup

This project uses **environment variables** for email credentials.

Create a `.env` file in my root:
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_gmail_app_password


> 🔒 Do not share or push this file. It is already excluded in `.gitignore`.

---

## 📦 Install & Run Locally

```bash
git clone https://github.com/Karabo-lab/karabo-portfolio.git
cd karabo-portfolio
python -m venv env
env\\Scripts\\activate     # (or source env/bin/activate on Linux/Mac)
pip install -r requirements.txt
flask run

📚 License
This project is open-source and free to use for learning or inspiration.
Contact me if you'd like to collaborate or feature it.

🙋‍♂️ Author
Karabo Madigoe
💻 GitHub
🔗 LinkedIn
🌐 Portfolio
