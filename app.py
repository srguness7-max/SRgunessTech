import os
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Güvenlik ve Veritabanı Yapılandırması
app.config['SECRET_KEY'] = 'srgunesstech-secret-key-2026'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.instance_path, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

os.makedirs(app.instance_path, exist_ok=True)

db = SQLAlchemy(app)

# --- Veritabanı Modeli ---
class QuoteRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    project_type = db.Column(db.String(100), nullable=False)
    budget = db.Column(db.String(50), nullable=True)
    details = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

with app.app_context():
    db.create_all()

# --- Rotalar ---
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/teklif-al', methods=['GET', 'POST'])
def quote():
    if request.method == 'POST':
        try:
            name = request.form.get('name')
            email = request.form.get('email')
            project_type = request.form.get('project_type')
            budget = request.form.get('budget')
            details = request.form.get('details')

            new_quote = QuoteRequest(
                name=name,
                email=email,
                project_type=project_type,
                budget=budget,
                details=details
            )
            
            db.session.add(new_quote)
            db.session.commit()

            print(f"\n[BİLDİRİM] Yeni Proje Teklifi!\nGönderen: {name} ({email})\nTür: {project_type}\nBütçe: {budget}\n")

            return jsonify({'success': True, 'message': 'Teklif talebiniz başarıyla alındı.'})
        except Exception as e:
            db.session.rollback()
            return jsonify({'success': False, 'message': str(e)}), 500

    return render_template('quote.html')

if __name__ == '__main__':
    app.run(debug=True)