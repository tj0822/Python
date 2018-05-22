from jinja2 import Markup, escape

markup_escape_method_using = Markup.escape("<b>Markup 클래스의 escape 클래스 메서드를 사용합니다.</b>")
escape_function_using = escape("<b>Markup 클래스의 escape 클래스 메서드를 사용합니다.</b>")