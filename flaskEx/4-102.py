from flask import Flask, flash, request

app = Flask(__name__)
app.config.update(SECRET_KEY='F34TF$#$e34D')

@app.route("/board_write", methods=["POST"])
def board_write():
    title = request.form.get("title")
    content = request.form.get("content")

    … 처리로직
    
    if error:
        flash("게시판 작성에 오류가 발생하였습니다")
        return render_template("board_write.html", title=title, content=content)
    else:
        return render_template("board_write_complete.html")