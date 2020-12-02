import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Pizzeria.settings")

import django
django.setup()

from pizzas.models import Pizza

pizzas = Pizza.objects.all()

for pizza in pizzas:
    print("Pizza ID:", pizza.id,"Pizza:", pizza)

p = Pizza.objects.get(id=1)
print(p.name)
print(p.date_added)

toppings = p.topping_set.all()

for topping in toppings:
    print(topping)