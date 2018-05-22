{% for loop_item in zips.items() %}
    {{ loop_item[0] }} / {{ loop_item[1] }} <br>
{% endfor %}