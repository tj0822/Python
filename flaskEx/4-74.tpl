<dl>
    {% for field in form %}
        <dt>{{ field.label }}</dt>
        <dd>{{ field }}</dd>
    {% endfor %}
</dl>