{{ form.radios.label }} :
{% for radio_f in form.radios %}
    {{ radio_f() }} {{radio_f.label}}
{% endfor %}