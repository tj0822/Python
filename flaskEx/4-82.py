class MyForm(Form):
    name = StringField('Name', [InputRequired()])

    def validate_name(form, field):
        if len(field.data) > 50:
            raise ValidationError('Name must be less than 50 characters')