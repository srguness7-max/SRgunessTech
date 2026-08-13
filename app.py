import os
import smtplib
import threading
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'srgunesstech_secret_key_2026'

# --- GMAIL HESAP BİLGİLERİ ---
SENDER_EMAIL = 'srgunesstech@gmail.com'
APP_PASSWORD = 'igosbkqtkzkfdkjf'

def send_email_thread(name, user_email, subject, message_body):
    try:
        msg = MIMEMultipart()
        msg['From'] = f"SRgunessTech Web <{SENDER_EMAIL}>"
        msg['To'] = SENDER_EMAIL
        msg['Reply-To'] = user_email
        msg['Subject'] = f"[SRgunessTech İletişim] {subject}"

        body_text = f"""SRgunessTech Web Sitesinden Yeni Mesaj!

Gönderen Ad Soyad : {name}
Gönderen E-Posta  : {user_email}
Konu             : {subject}

Mesaj:
{message_body}
"""
        msg.attach(MIMEText(body_text, 'plain', 'utf-8'))

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465, timeout=10)
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.sendmail(SENDER_EMAIL, SENDER_EMAIL, msg.as_string())
        server.quit()
        print(">>> MESAJ GMAIL KUTUSUNA ULAŞTI <<<")
    except Exception as e:
        print(f">>> E-POSTA HATASI: {e} <<<")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/urunler')
def products():
    return render_template('products.html')

@app.route('/teknolojiler')
def technologies():
    return render_template('technologies.html')

@app.route('/hakkimizda')
def about():
    return render_template('about.html')

@app.route('/iletisim', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        user_email = request.form.get('email')
        subject = request.form.get('subject')
        message_body = request.form.get('message')
        
        threading.Thread(
            target=send_email_thread, 
            args=(name, user_email, subject, message_body)
        ).start()
        
        flash('Mesajınız başarıyla iletildi! En kısa sürede geri dönüş yapacağız.', 'success')
        return redirect(url_for('contact'))
        
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
