from django.shortcuts import render,redirect
from .models import Pizza, Topping
from .forms import PizzaForm, ToppingForm

# Create your views here.
def index(request):
    return render(request, 'pizzas/index.html')


def pizzas(request):
    pizzas = Pizza.objects.order_by('date_added')

    context = {'pizzas':pizzas}

    return render(request, 'pizzas/pizzas.html', context)

def pizza(request,p_id):
    pizza = Pizza.objects.get(id=p_id)
    toppings = pizza.topping_set.order_by('-date_added')
    
    context = {'pizza':pizza, 'toppings':toppings}

    return render(request, 'pizzas/pizza.html',context)

def new_pizza(request):
    if request.method != 'POST':
        form = PizzaForm()
    else:
        form = PizzaForm(data=request.POST)

        if form.is_valid():
            form.save()

            return redirect('pizzas:pizzas')
    
    context = {'form': form}

    return render(request, 'pizzas/new_pizza.html', context)

def new_topping(request,pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    
    if request.method != 'POST':
        form = ToppingForm()
    else:
        form = ToppingForm(data=request.POST)

        if form.is_valid():
            new_topping = form.save(commit=False)
            new_topping.pizza = pizza
            new_topping.save()
            form.save()
            return redirect('pizzas:pizza', p_id=pizza_id)

    context = {'form': form, 'pizza': pizza}
    return render(request, 'pizzas/new_topping.html', context)



