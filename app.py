from flask import Flask, render_template, request, send_file
import pdfkit

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.form
    rendered = render_template('resume_template.html', data=data)

    # Save HTML to PDF using pdfkit
    pdfkit.from_string(rendered, 'resume.pdf')
    return send_file('resume.pdf', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
