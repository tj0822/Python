class MyDoc(Document):
    structure = {
        'bar': basestring,
        'foo':{
            'spam': basestring,
            'eggs': int,
        }
    }
    default_values = { 'bar': 'hello', 'foo.eggs': 4 }