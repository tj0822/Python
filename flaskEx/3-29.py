from jinja2 import Markup

markup_value = Markup("<strong>%s</strong>")
strong_value = markup_value % "<em>이탤릭 태그는 이스케이프 처리될 것입니다.</em>"
striptags_value = strong_value.striptags()