from flask import Flask, render_template, request, send_file
from flask_sqlalchemy import SQLAlchemy
from engine import analyze_behavior
from report_gen import generate_pdf
import ast
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'footprintx_2026_secure'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///footprintx.db'
db = SQLAlchemy(app)

# --- ROUTES ---

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        # Logic is handled by the Engine
        result = analyze_behavior(name, email)
    return render_template('index.html', result=result)

@app.route('/generate-report', methods=['POST'])
def report():
    raw_data = request.form.get('report_data')
    data = ast.literal_eval(raw_data)
    pdf_path = generate_pdf(data)
    return send_file(pdf_path, as_attachment=True)

if __name__ == '__main__':
    with app.app_context():
        db.create_all() # Initializes the DB based on your requirements.txt
    app.run(debug=True, port=8000)