PDF Merger Application
Created by Ali Khaled

Overview
This project provides a simple web interface to merge two PDF files. Users can upload two PDF files, and the application will merge them into one PDF, which can then be downloaded.

Features
Upload two PDF files.
Merge the uploaded PDFs into a single file.
Download the merged PDF.
Simple and intuitive web interface.
Prerequisites
Python 3.x
Flask
PyPDF2
pdf2image
Pillow
Poppler (for Windows)
Directory Structure
markdown
Copy code
mergePDF/
│
├── app.py
└── templates/
    └── upload.html
Installation
Clone the Repository:

bash
Copy code
git clone <repository-url>
cd mergePDF
Set Up the Virtual Environment:

bash
Copy code
python -m venv venv
venv\Scripts\activate  # For Windows
# source venv/bin/activate  # For macOS/Linux
Install Required Packages:

bash
Copy code
pip install Flask PyPDF2 pdf2image Pillow
Install Poppler:

Download and install Poppler for Windows from this GitHub repository.
Extract the contents and add the path to the bin directory to your system PATH.
Running the Application
Ensure the Directory Structure is Correct.
Run Your Flask Application:
bash
Copy code
python app.py
Open Your Web Browser and Navigate to:
arduino
Copy code
http://127.0.0.1:5000/
This should now correctly display the upload form and allow you to merge PDFs. If you encounter any issues, please let me know!

Deployment on Windows Server
Install Required Software on the Server:

Install Python, Pip, and Virtualenv.
Install IIS and configure FastCGI.
Install and configure WFastCGI.
Set Up Your Flask Application:

Create a project directory on the server.
Create a virtual environment and install dependencies.
Copy your Flask application files to the project directory.
Configure IIS to Serve the Flask Application:

Create a Web Application in IIS.
Configure Handler Mappings.
Configure the web.config file.
Start and Test Your Application:

Start IIS.
Open a web browser and navigate to http://your-server-ip/flaskapp.
Author
Ali Khaled
License
This project is licensed under the MIT License - see the LICENSE file for details.
