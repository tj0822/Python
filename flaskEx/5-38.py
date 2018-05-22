@app.route("/file_download")
def send_helper_file():
    download_file = request.args.get('filename')

    if file_src_name:
        # 사용자가 업로드한 것이 있으면 그 이름을 조합한다.
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file_src_name)

        if not os.path.exists(filename):
            # 파일이 없는 경우는 임의의 파일 객체를 만들고 파일이 없다는 내용을 써서 전송하게 한다.
            from io import BytesIO
            strIO = StringIO()
            strIO.write(b"요청하신 파일을 찾을 수 없습니다.")
            strIO.seek(0)

            # 호환성 유지를 위한 파일 객체 덮어쓰기
            filename = strIO

    return send_file(filename, as_attachment=True, attachment_filename=file_src_name)