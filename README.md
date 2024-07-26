# PDF Merger Application

Created by Ali Khaled

## Overview

This project provides a simple web interface to merge two PDF files. Users can upload two PDF files, and the application will merge them into one PDF, which can then be downloaded.

## Features

- Upload two PDF files.
- Merge the uploaded PDFs into a single file.
- Download the merged PDF.
- Simple and intuitive web interface.

## Prerequisites

- Python 3.x
- Flask
- PyPDF2
- pdf2image
- Pillow
- Poppler (for Windows)

## Directory Structure

mergePDF/
│
├── app.py
└── templates/
└── upload.html

markdown
Copy code

## Installation

1. **Clone the Repository**:
    ```bash
    git clone <repository-url>
    cd mergePDF
    ```

2. **Set Up the Virtual Environment**:
    ```bash
    python -m venv venv
    venv\Scripts\activate  # For Windows
    # source venv/bin/activate  # For macOS/Linux
    ```

3. **Install Required Packages**:
    ```bash
    pip install Flask PyPDF2 pdf2image Pillow
    ```

4. **Install Poppler**:
    - Download and install Poppler for Windows from [this GitHub repository](https://github.com/oschwartz10612/poppler-windows/releases/).
    - Extract the contents and add the path to the `bin` directory to your system PATH.

## Running the Application

1. **Ensure the Directory Structure is Correct**.
2. **Run Your Flask Application**:
    ```bash
    python app.py
    ```
3. **Open Your Web Browser and Navigate to**:
    ```
    http://127.0.0.1:5000/
    ```

This should now correctly display the upload form and allow you to merge PDFs. If you encounter any issues, please let me know!

## Deployment on Windows Server

1. **Install Required Software on the Server**:
    - Install Python, Pip, and Virtualenv.
    - Install IIS and configure FastCGI.
    - Install and configure WFastCGI.

2. **Set Up Your Flask Application**:
    - Create a project directory on the server.
    - Create a virtual environment and install dependencies.
    - Copy your Flask application files to the project directory.

3. **Configure IIS to Serve the Flask Application**:
    - Create a Web Application in IIS.
    - Configure Handler Mappings.
    - Configure the `web.config` file.

4. **Start and Test Your Application**:
    - Start IIS.
    - Open a web browser and navigate to `http://your-server-ip/flaskapp`.

## Author

**Ali Khaled**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
By using Markdown, GitHub will automatically render the content in a nicely formatted way.
