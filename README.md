<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PDF Merger Application</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: #333;
        }
        h1, h2, h3 {
            color: #007bff;
        }
        pre {
            background-color: #f8f9fa;
            padding: 10px;
            border-radius: 5px;
        }
        code {
            color: #d63384;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>PDF Merger Application</h1>
        <p><strong>Created by Ali Khaled</strong></p>

        <h2>Overview</h2>
        <p>This project provides a simple web interface to merge two PDF files. Users can upload two PDF files, and the application will merge them into one PDF, which can then be downloaded.</p>

        <h2>Features</h2>
        <ul>
            <li>Upload two PDF files.</li>
            <li>Merge the uploaded PDFs into a single file.</li>
            <li>Download the merged PDF.</li>
            <li>Simple and intuitive web interface.</li>
        </ul>

        <h2>Prerequisites</h2>
        <ul>
            <li>Python 3.x</li>
            <li>Flask</li>
            <li>PyPDF2</li>
            <li>pdf2image</li>
            <li>Pillow</li>
            <li>Poppler (for Windows)</li>
        </ul>

        <h2>Directory Structure</h2>
        <pre>
<code>mergePDF/
│
├── app.py
└── templates/
    └── upload.html
</code>
        </pre>

        <h2>Installation</h2>
        <ol>
            <li><strong>Clone the Repository:</strong>
                <pre><code>git clone &lt;repository-url&gt;
cd mergePDF</code></pre>
            </li>
            <li><strong>Set Up the Virtual Environment:</strong>
                <pre><code>python -m venv venv
venv\Scripts\activate  # For Windows
# source venv/bin/activate  # For macOS/Linux</code></pre>
            </li>
            <li><strong>Install Required Packages:</strong>
                <pre><code>pip install Flask PyPDF2 pdf2image Pillow</code></pre>
            </li>
            <li><strong>Install Poppler:</strong>
                <p>Download and install Poppler for Windows from <a href="https://github.com/oschwartz10612/poppler-windows/releases/">this GitHub repository</a>.</p>
                <p>Extract the contents and add the path to the <code>bin</code> directory to your system PATH.</p>
            </li>
        </ol>

        <h2>Running the Application</h2>
        <ol>
            <li><strong>Ensure the Directory Structure is Correct.</strong></li>
            <li><strong>Run Your Flask Application:</strong>
                <pre><code>python app.py</code></pre>
            </li>
            <li><strong>Open Your Web Browser and Navigate to:</strong>
                <pre><code>http://127.0.0.1:5000/</code></pre>
            </li>
        </ol>
        <p>This should now correctly display the upload form and allow you to merge PDFs. If you encounter any issues, please let me know!</p>

        <h2>Deployment on Windows Server</h2>
        <ol>
            <li><strong>Install Required Software on the Server:</strong>
                <ul>
                    <li>Install Python, Pip, and Virtualenv.</li>
                    <li>Install IIS and configure FastCGI.</li>
                    <li>Install and configure WFastCGI.</li>
                </ul>
            </li>
            <li><strong>Set Up Your Flask Application:</strong>
                <ul>
                    <li>Create a project directory on the server.</li>
                    <li>Create a virtual environment and install dependencies.</li>
                    <li>Copy your Flask application files to the project directory.</li>
                </ul>
            </li>
            <li><strong>Configure IIS to Serve the Flask Application:</strong>
                <ul>
                    <li>Create a Web Application in IIS.</li>
                    <li>Configure Handler Mappings.</li>
                    <li>Configure the <code>web.config</code> file.</li>
                </ul>
            </li>
            <li><strong>Start and Test Your Application:</strong>
                <ul>
                    <li>Start IIS.</li>
                    <li>Open a web browser and navigate to <code>http://your-server-ip/flaskapp</code>.</li>
                </ul>
            </li>
        </ol>

        <h2>Author</h2>
        <p><strong>Ali Khaled</strong></p>

        <h2>License</h2>
        <p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>
    </div>
</body>
</html>
