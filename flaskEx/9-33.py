<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>JPUB 경품 추첨 프로그림 - 당첨자 리스트 -</title>
    <!-- Latest compiled and minified CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.0/css/bootstrap.min.css">
    <!-- Optional theme -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.0/css/bootstrap-theme.min.css">
    <link rel="stylesheet" href="/static/css/prize_winning.css">
    <script type="text/javascript" src="https://code.jquery.com/jquery-2.1.1.min.js"></script>
</head>
<body>
    <!-- Begin page content -->
    <div class="container">
        <div class="page-header">
            <h1>JPUB 경품 추첨 프로그램</h1>
        </div>
        <div class="page-body">
            <table border="1">
                <tr>
                    <th>경품추첨일</th>
                    <th>경품순위</th>
                    <th>응모자명</th>
                    <th>응모자이메일</th>
                    <th>경품명</th>
                </tr>
                {% for winning_item in winning_query %}
                <tr>
                    <td>{{winning_item.winning_date|date_format}}</td>
                    <td>{{winning_item.winning_rank}}</td>
                    <td>{{winning_item.winning_name}}</td>
                    <td>{{winning_item.winning_email}}</td>
                    <td>{{winning_item.winning_product}}</td>
                </tr>
                {% endfor %}
            </table>
        </div>
    </div>
    <div class="footer">
        <div class="container">
            <p class="text-muted">Copyright 2014 Lee Ji-Ho(search5@gmail.com)</p>
        </div>
    </div>
    <!-- Latest compiled and minified JavaScript -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.0/js/bootstrap.min.js"></script>
</body>
</html>