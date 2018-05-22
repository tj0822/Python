import re

def email_validator(value):
    email = re.compile(r'(?:^|\s)[-a-z0-9_.]+@(?:[-a-z0-9]+\.)+[a-z]{2,6}(?:\s|$)',re.IGNORECASE)
    if not bool(email.match(value))
        raise ValidationError('%s is not a valid email')

class MyDoc(Document):
    structure = {
        'email': basestring,
        'foo': {
            'eggs': int,
        }
    }

    validators = {
        'email': email_validator,
        'foo.eggs': lambda x: x > 10
    }