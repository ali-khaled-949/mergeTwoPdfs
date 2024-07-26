import os
from flask import Flask, request, redirect, url_for, send_file, render_template, flash
from PyPDF2 import PdfMerger
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'supersecretkey'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/', methods=['POST'])
def upload_file():
    if 'file1' not in request.files or 'file2' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file1 = request.files['file1']
    file2 = request.files['file2']
    if file1.filename == '' or file2.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file1 and allowed_file(file1.filename) and file2 and allowed_file(file2.filename):
        filename1 = secure_filename(file1.filename)
        filename2 = secure_filename(file2.filename)
        file1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename1))
        file2.save(os.path.join(app.config['UPLOAD_FOLDER'], filename2))
        merged_pdf = merge_pdfs(filename1, filename2)
        if merged_pdf:
            return send_file(merged_pdf, as_attachment=True)
        else:
            flash('Failed to merge PDFs')
            return redirect(request.url)
    else:
        flash('Invalid file type')
        return redirect(request.url)

def merge_pdfs(file1, file2):
    try:
        merger = PdfMerger()
        merger.append(os.path.join(app.config['UPLOAD_FOLDER'], file1))
        merger.append(os.path.join(app.config['UPLOAD_FOLDER'], file2))
        output_path = os.path.join(app.config['UPLOAD_FOLDER'], 'merged.pdf')
        merger.write(output_path)
        merger.close()
        return output_path
    except Exception as e:
        print(f"Error merging PDFs: {e}")
        return None

if __name__ == "__main__":
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
