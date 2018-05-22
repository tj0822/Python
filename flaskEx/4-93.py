class CreditCardNumValidator:
    def __init__(self, message=None):
        # 참고: http://enie.edunet.net/index.do?mn=news&mode=view&nlk=41058&gk=41020
        if not message:
            messsage = "올바른 신용카드 번호가 아닙니다"
        self.message = message
   
    def __call__(self, form, field):
        hol = 0
        jjak = 0
       
        credit_card_num = field.data.replace(" ", "")
       
        for i, value in enumerate(credit_card_num, 1):
            if i % 2 == 1:
                tmp =  int(value) * 2
                # 2배수 한 값이 10보다 크면 2배수 한 값을 나누어서 더해야 정상적인 결과 보장함
                if tmp >= 10:
                    str_tmp = str(tmp)
                    tmp = int(str_tmp[0]) + int(str_tmp[1])
                hol += tmp
            if i % 2 == 0:
                jjak += int(value)
       
        if ((hol+jjak) % 10) != 0:
            validators.ValidationError(self.message)