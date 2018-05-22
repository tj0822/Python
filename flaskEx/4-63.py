@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
  
    if request.method == 'POST' and form.validate():
        # DB에 회원 정보 추가 후 저장
        return "login ok"
    return render_template('register.html', form=form)