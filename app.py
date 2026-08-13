from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'srgunesstech_secret_key_2026'

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
        message = request.form.get('message')
        
        flash('Mesajınız başarıyla gönderildi. En kısa sürede sizinle iletişime geçeceğiz.', 'success')
        return redirect(url_for('contact'))
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
