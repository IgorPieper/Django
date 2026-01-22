{{ imie }} - Zmienna w Templatach

<img src="{% static 'img/logo.png' %}"> - Dodawanie zdjęcia

{% if zalogowany %} - if w Templatach
  Witaj!
{% else %}
  Zaloguj się
{% endif %}

{% for produkt in produkty %} - For w Templatach
  <li>{{ produkt.nazwa }}</li>
{% endfor %}

{{ imie|upper }} - Proste operacje na zmiennych
{{ opis|truncatechars:50 }}
{{ cena|floatformat:2 }}

{% include "menu.html" %} - Dołączanie innego szablonu do obecnego

{% block content %} - Przetrzeń w szablonie którą indywidualnie edytujesz
  {% endblock %}