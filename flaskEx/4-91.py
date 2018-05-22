class KoreaSocialNumberValidator:
    def __init__(self, ksn2_field, message=None):
        if not message:
            messsage = "올바른 주민등록번호가 아닙니다"
        self.message = message
        self.ksn2_field = ksn2_field

    def __call__(self, form, field):
        ksn1_value = field.data
        ksn2_value = form[self.ksn2_field].data
       
        ksn2_value, check_digit = ksn2_value[:-1], ksn2_value[-1]
       
        ksn_number = "{0}{1}".format(ksn1_value, ksn2_value)
        check_magic_number = "234567892345"
       
        ksn_magic_number = sum([int(real) * int(check) for real, check in zip(ksn_number, check_magic_number)])
       
        check_prg1 = (11 - (ksn_magic_number % 11)) % 10
        if check_prg1 != int(check_digit):
            validators.ValidationError(self.message)