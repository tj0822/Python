ksn1 = TextField('주민등록번호 앞 자리', [validators.InputRequired(), KoreaSocialNumberValidator('ksn2')])
ksn2 = TextField('주민등록번호 뒷 자리', [validators.InputRequired()])