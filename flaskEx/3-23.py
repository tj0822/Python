from jinja2 import Markup

markup_value = Markup("<markup>이 값은 신뢰할 수 있는 HTML 입니다.</markup>")
return render_template("markup_test.html", markup=markup_value)