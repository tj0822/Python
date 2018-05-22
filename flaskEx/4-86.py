post1 = TextField('우편번호1', [validators.InputRequired(), KoreaPostValidator(‘post2’)])
post2 = TextField('우편번호2', [validators.InputRequired()])