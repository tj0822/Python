from jinja2 import Markup

bold_markup_value = Markup.escape("<b>볼드처리를 위한 태그를 제거합니다.</b>")
striptags_markup_value = bold_markup_value.striptags()