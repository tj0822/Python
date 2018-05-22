class DataSet:
    def __init__(self):
        self.username = "test"

ds = DataSet()
form = RegistrationForm(formdata=request.form, obj=ds)

print(form.username.data)