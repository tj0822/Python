import os
from flask import Flask, request, redirect, url_for, render_template
from werkzeug import secure_filename

UPLOAD_FOLDER = '/var/www/jpub/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
       filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/file_upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
       upload_file_name = request.values.get("name")
       if allowed_file(upload_file_name):
            chunk = int(request.values.get('chunk', 0))
            chunks = int(request.values.get('chunks', 0))

            filename = secure_filename(upload_file_name)

            temp_file_name = "%s/%s.part" % (app.config['UPLOAD_FOLDER'], filename)
            dest_file_name = "%s/%s" % (app.config['UPLOAD_FOLDER'], filename)

            upload_file = open(temp_file_name, "ab")
            for block in iter(lambda: request.stream.read(4096), b""):
                upload_file.write(block)
            upload_file.close()

            if chunk == (chunks - 1):
                os.rename(temp_file_name, dest_file_name)
               
            return "fileupload ok"
    return render_template("upload.html")