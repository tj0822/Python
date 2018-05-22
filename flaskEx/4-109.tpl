{% with messages = get_flashed_messages(category_filter=[‘error']) %}
     {% if messages %}
         <ul>
         {% for message in messages %}
             <li>{{ message }}</li>
         {% endfor %}
         </ul>
     {% endif %} 
{% endwith %}