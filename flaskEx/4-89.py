class KoreaMobileTelValidator:
    def __init__(self, message=None):
        if not message:
            messsage = "올바른 이동통신 번호가 아닙니다"
        self.message = message
       
        self.mobile_title_number = ( "010", "011", "016", "017", "018", "019" )
   
    def  __call__(self, form, field):
        if field.data not in self.mobile_title_number:
            validators.ValidationError(self.message)