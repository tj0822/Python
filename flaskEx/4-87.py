class KoreaRegionTelValidator:
    def __init__(self, message=None):
        if not message:
            messsage = "올바른 지역번호가 아닙니다"
        self.message = message
       
        self.area_title_number = (
            "02", "031", "032", "033",
            "041", "042", "043", "044", "049",
            "051", "052", "053", "054", "055",
            "061", "062", "063", "064", "070"
        )
   
   
    def  __call__(self, form, field):
        if field.data not in self.area_title_number:
            validators.ValidationError(self.message)