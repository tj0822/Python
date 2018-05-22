{% for product_name, product_money in zips.items() %}
    {{ product_name }} / {{ product_money }} <br>
{% endfor %}