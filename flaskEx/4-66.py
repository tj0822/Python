# POST 요청 값 사용하기
form = RegistrationForm(formdata=request.form)

# GET 요청 값 사용하기
form = RegistrationForm(formdata=request.args)

# POST, GET 요청 종류에 상관없이 값 사용하기
form = RegistrationForm(formdata=request.values)