{% macro form_input(name, first='first args') -%}
    <input type="{{ kwargs['type'] or 'text' }}" name="{{ name }}" value="{{ kwargs['value']|e or '' }}" size="{{ kwargs['size'] or 20 }}" class="{{ varargs[0] }}">
    <ul>
        <li>macro name: {{ form_input.name }}</li>
        <li>arguments: {{ form_input.arguments }}</li>
        <li>defaults: {{ form_input.defaults }}</li>
        <li>catch_kwargs: {{ form_input.catch_kwargs }}</li>
        <li>catch_varargs: {{ form_input.catch_varargs }}</li>
        <li>caller: {{ form_input.caller }}</li>
    </ul>
{%- endmacro %}

<p>{{ form_input('username') }}</p>