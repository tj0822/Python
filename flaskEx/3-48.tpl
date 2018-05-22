{% extends "base.html" %}

{% block content %}
    <h1>Index</h1>
    <p class="important">
      {% block inner_content %}{% endblock %}
    </p>
{% endblock %}