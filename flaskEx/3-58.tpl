{% macro dump_users(users) -%}
    <ul>
    {%- for user in users %}
        <li><p>{{ user['username']|e }}</p>{{ caller(user_info=user) }}</li>
    {%- endfor %}
    </ul>
{%- endmacro %}

{% call(user_info) dump_users(list_of_user) %}
    <dl>
        <dl>Realname</dl>
        <dd>{{ user_info['realname']|e }}</dd>
        <dl>Description</dl>
        <dd>{{ user_info['description'] }}</dd>
    </dl>
{% endcall %}