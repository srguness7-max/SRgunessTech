import os
import threading
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'srgunesstech_secret_key_2026'

# --- GMAIL SMTP E-POSTA AYARLARI (Port 465 & SSL) ---
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'srgunesstech@gmail.com'
app.config['MAIL_PASSWORD'] = 'igosbkqtkzkfdkjf'
app.config['MAIL_DEFAULT_SENDER'] = ('SRgunessTech Web', 'srgunesstech@gmail.com')

mail = Mail(app)

def send_async_email(app_instance, msg):
    """Mail gönderme işlemini arka planda çalıştırır, hatayı terminale/loglara basar."""
    with app_instance.app_context():
        try:
            mail.send(msg)
            print(">>> MAIL BAŞARIYLA GÖNDERİLDİ! <<<")
        except Exception as e:
            print(f">>> MAIL GÖNDERME HATASI: {e} <<<")

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
        email = request.form.get('email')
        subject = request.form.get('subject')
        message_body = request.form.get('message')
        
        msg = Message(
            subject=f"[SRgunessTech İletişim] {subject}",
            recipients=['srgunesstech@gmail.com']
        )
        msg.body = f"""SRgunessTech Web Sitesinden Yeni Mesaj!

Gönderen Ad Soyad : {name}
Gönderen E-Posta  : {email}
Konu             : {subject}

Mesaj:
{message_body}
"""
        # Arka planda mail fırlatma
        threading.Thread(target=send_async_email, args=(app, msg)).start()
        
        flash('Mesajınız başarıyla iletildi! En kısa sürede geri dönüş yapacağız.', 'success')
        return redirect(url_for('contact'))
        
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
