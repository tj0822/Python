{% with messages = get_flashed_messages(with_categories=True) %}
     {% if messages %}
         <ul>
         {% for category, message in messages %}
             <li class="{{ category }}">{{ message }}</li>
         {% endfor %}
         </ul>
     {% endif %}
{% endwith %}