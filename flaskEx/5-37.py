@app.route("/file_download_directory")
def send_directory():
    download_file = request.args.get('filename')

    return send_from_directory(app.config['UPLOAD_FOLDER'], download_file)