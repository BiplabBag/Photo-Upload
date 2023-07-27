# 1. Import necessary modules
import os
from flask import Flask, request, render_template, redirect, url_for

# 2. Create an instance of the Flask class
app = Flask(__name__)

# 3. Define a route to handle the main page
@app.route('/')
def index():
    return render_template('index.html')

# 4. Define a route to handle the photo upload
@app.route('/upload', methods=['POST'])
def upload():
    # Check if a file was uploaded
    if 'photo' not in request.files:
        return "No file part"
    
    file = request.files['photo']
    
    # Check if the file has a valid filename
    if file.filename == '':
        return "No selected file"
    
    # Check if the file is allowed (optional)
    allowed_extensions = {'jpg', 'jpeg', 'png', 'gif'}
    if '.' not in file.filename or file.filename.rsplit('.', 1)[1].lower() not in allowed_extensions:
        return "Invalid file type"
    
    # Save the file to a secure location
    base_path = os.path.abspath(os.path.dirname(__file__))
    upload_folder = os.path.join(base_path, 'uploads')
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)
    
    file.save(os.path.join(upload_folder, file.filename))
    
    return redirect(url_for('upload_successful'))

# 5. Define a route to handle the upload success page
@app.route('/upload_successful')
def upload_successful():
    return render_template('upload.html')

# 6. Run the app if executed directly
if __name__ == '__main__':
    app.run(debug=True)
