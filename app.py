import os
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'srgunesstech_secret_key_2026'

# --- GMAIL SMTP E-POSTA AYARLARI ---
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'srgunesstech@gmail.com'
app.config['MAIL_PASSWORD'] = 'igosbkqtkzkfdkjf'  # Gmail Uygulama Şifreniz

mail = Mail(app)

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
        
        # Gönderilecek Mail İçeriği
        msg = Message(
            subject=f"[SRgunessTech Web] {subject}",
            sender=app.config['MAIL_USERNAME'],
            recipients=['srgunesstech@gmail.com']  # Mesajın düşeceği e-posta adresi
        )
        msg.body = f"""SRgunessTech Web Sitesinden Yeni Mesaj!

Gönderen Ad Soyad : {name}
Gönderen E-Posta  : {email}
Konu             : {subject}

Mesaj:
{message_body}
"""
        
        try:
            mail.send(msg)
            flash('Mesajınız başarıyla gönderildi. En kısa sürede sizinle iletişime geçeceğiz.', 'success')
        except Exception as e:
            flash('Mesaj gönderilirken bir sorun oluştu. Lütfen daha sonra tekrar deneyin.', 'danger')
            
        return redirect(url_for('contact'))
        
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
