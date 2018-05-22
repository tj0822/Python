@app.route("/board_write", methods=["POST"])
def board_write():
    … 처리로직
    
    if error:
        return """<script>alert('게시판 작성에 오류가 발생하였습니다');history.back();</script>"""
    else:
        return render_template("board_write_complete.html")