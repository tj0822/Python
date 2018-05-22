from jinja2 import Markup

escaped_markup_value = Markup.escape("<b>Markup 클래스의 escape 클래스 메서드를 사용합니다.</b>")
unescape_markup_value = escaped_markup_value.unescape()