from flask import Flask, render_template, request
from flask import Response
import os
from werkzeug.datastructures import Headers

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/var/www/jpub/attach'

@app.route('/file_download')
def generate_large_csv():
    download_file = request.args.get('filename')
   
    full_path = os.path.join(app.config['UPLOAD_FOLDER'], download_file)

    headers = Headers()
    headers.add('Content-Disposition', 'attachment', filename=download_file)
    headers['Content-Length'] = os.path.getsize(full_path)

    download_obj = open(full_path, 'rb')

    def generate():
        for block in iter(lambda: download_obj.read(4096), b''):
            yield block
        download_obj.close()
   return Response(generate(), mimetype='application/octet-stream', headers=headers)