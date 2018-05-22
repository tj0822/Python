from wtforms import validators
import datetime

class KoreaPostValidator:
    def __init__(self, post2_field, message=None):
        self.post2_field = post2_field
        if not message:
            messsage = "올바른 우편번호가 아닙니다"
        self.message = message
   
   
    def __call__(self, form, field):
        post2_field_data = form[self.post2_field].data
       
        # 첫번째 우편번호이면서 우편번호는 0으로 시작하는 경우 예외를 발생시킨다.
        if field.data.startswith("0"):
            validators.ValidationError(self.message)
       
        # 우편번호는 앞, 뒤가 모두 3자리를 만족시키지 않으면 예외를 발생시켜야 합니다.
        if len(field.data) < 4:
            validators.ValidationError(self.message)
       
        if len(post2_field_data < 4):
            validators.ValidationError(self.message)