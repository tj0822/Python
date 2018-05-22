def validate(self, *args, **kwargs):
    assert self['foo'] > self['bar']
    super(MyDoc, self).validate(*args, **kwargs)