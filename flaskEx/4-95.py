class CreditCardExpiresValidator:
    def __init__(self, expire_month_field, message=None):
        # 참고: https://github.com/formencode/formencode/blob/master/formencode/validators.py
        if not message:
            messsage = "올바른 신용카드 유효일자가 아닙니다."
        self.message = message
        self.expire_month_field = expire_month_field
   
    def __call__(self, form, field):
        ccExpiresMonth = int(form[self.expire_month_field].data)
        ccExpiresYear = int(field.data)
       
        now = datetime.datetime.now()
        today = datetime.date(now.year, now.month, now.day)
       
        next_month = ccExpiresMonth % 12 + 1
        next_month_year = ccExpiresYear
       
        if next_month == 1:
            next_month_year += 1
       
        expires_date = datetime.date(next_month_year, next_month, 1)
       
        # 신용카드 유효일자가 시스템의 오늘날짜보다 작으면 유효한 날짜가 아니다.
        if expires_date < today:
            validators.ValidationError(self.message)