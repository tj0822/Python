from jinja2 import Markup

class Foo:
    def __init__(self, foo_str):
        self.foo_str = foo_str

    def __html__(self):
        return "<em>%s</em>" % self.foo_str

foo_inst = Foo("이탤릭체로 Foo 객체를 생성합니다")
markup_value = Markup(foo_inst)