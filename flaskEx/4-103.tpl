<html>
    <body>
        <form method="post">
            <dl>
                <dt>제목</dt>
                <dd><input type="text" name="title" value="{{ title }}">
                <dt>내용</dt>
                <dd><textarea name="content" rows="10" cols="80">{{ content }}</textarea>
            </dl>
            <input type="submit" value="전송">
        </form>
    </body>
</html>