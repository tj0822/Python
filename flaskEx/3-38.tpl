{% for user in users if not user.hidden %}
    <li>{{ user.username|e }}</li>
{% endfor %}