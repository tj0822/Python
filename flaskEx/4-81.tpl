<select name="{{form.select.name}}" id="{{form.select.id}}">
    {% for option in form.select %}
        {{ option() }}
    {% endfor %}
</select>