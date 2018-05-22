<ul>
{% for user in users %}
    <li>{{ user.username|e }}</li>
    {% set outer_loop = loop %}
    {% for certficate in certifates %}
        {{ certificate }}: {{ outer_loop.index }}
    {% endfor %}
{% endfor %}
</ul>