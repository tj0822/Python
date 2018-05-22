{% macro form_input() -%}
    <input type="{{ kwargs['type'] or 'text' }}" name="{{ varargs[0] }}" value="{{ kwargs['value']|e or '' }}" size="{{ kwargs['size'] or 20 }}">
{%- endmacro %}

<p>{{ form_input('username') }}</p>
<p>{{ form_input('password', type='password') }}</p>