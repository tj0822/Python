>>> form.errors
{'username': [u'This field is required.'], 'password': [u'This field is required.'], 'email': ['not is valid', u'Field must be between 6 and 35 characters long. How!'], 'accept_tos': [u'This field is required.'], 'confirm': [u'This field is required.']}
>>> form.data
{'username': None, 'password': None, 'email': None, 'accept_tos': False, 'confirm': None}