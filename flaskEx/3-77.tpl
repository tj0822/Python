{% for item in iterable|sort %}
    ...
{% endfor %}

{% for item in iterable|sort(attribute='date') %}
    ...
{% endfor %}