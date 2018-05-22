<html>
    <body>
        {% with messages = get_flashed_messages() %}
            {% if messages %}
                <ul>
                {% for message in messages %}
                    <li>{{ message }}</li>
                {% endfor %}
                </ul>
            {% endif %}
        {% endwith %}

        <form method="post">
            <dl>
                <dt>제목</dt>
                <dd><input type="text" name="title">
                <dt>내용</dt>
                <dd><textarea name="content" rows="10" cols="80"></textarea>
            </dl>
            <input type="submit" value="전송">
        </form>
    </body>
</html>