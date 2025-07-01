from flask import Flask, render_template, request, redirect, flash, url_for
import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('secret_key')

EMAIL_ADDRESS = os.getenv('EMAIL_USER')
EMAIL_PASSWORD = os.getenv('EMAIL_PASS')

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/send', methods=['POST'])
def send():
    name = request.form.get('name')
    email = request.form.get('email')
    subject = request.form.get('subject')
    message = request.form.get('message')

    msg = EmailMessage()
    msg['Subject'] = f"{subject} (from portfolio site)"
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS
    msg.set_content(
        f"Name: {name}\n"
        f"Email: {email}\n"
        f"Subject: {subject}\n\n"
        f"Message:\n{message}"
    )

    auto_reply = EmailMessage()
    auto_reply['Subject'] = "Thanks for contacting me"
    auto_reply['From'] = EMAIL_ADDRESS
    auto_reply['To'] = email
    auto_reply.set_content(
        f"Hi {name},\n\n"
        "Thanks for reaching out! I'll get back to you as soon as I see your message.\n\n"
        "Best regards,\n"
        "Karabo Madigoe"
    )

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)         
            smtp.send_message(auto_reply) 
        flash('✅ Message sent successfully! A confirmation email was also sent.', 'success')
    except Exception as e:
        print("Error:", e)
        flash('❌ Message failed to send. Please try again later.', 'error')

    return redirect(url_for('contact'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Render provides a PORT env variable
    app.run(host='0.0.0.0', port=port, debug=True)

