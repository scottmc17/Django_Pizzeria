from django.shortcuts import render,redirect
from .models import Pizza, Topping, Comment 
from .forms import PizzaForm, ToppingForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.
def index(request):
    return render(request, 'pizzas/index.html')

@login_required
def pizzas(request):
    pizzas = Pizza.objects.order_by('date_added')

    context = {'pizzas':pizzas}

    return render(request, 'pizzas/pizzas.html', context)

@login_required
def pizza(request,p_id):
    pizza = Pizza.objects.get(id=p_id)



    toppings = pizza.topping_set.order_by('-date_added')
    
    context = {'pizza':pizza, 'toppings':toppings}

    return render(request, 'pizzas/pizza.html',context)

@login_required
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

@login_required
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

@login_required
def edit_topping(request, topping_id):
    topping = Topping.objects.get(id=topping_id)
    pizza = topping.pizza

    if request.method != 'POST':
        form = ToppingForm(instance=topping)
    else:
        form = ToppingForm(instance=topping, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('pizzas:pizza', p_id=pizza.id)

    context = {'topping':topping, 'pizza':pizza, 'form':form}
    return render(request, 'pizzas/edit_topping.html', context)

        
# def new_comment(request,pizza_id):
#     pizza = Pizza.objects.get(id=pizza_id)
    
    
#     if request.method != 'POST':
#         form = CommentForm()
#     else:
#         form = CommentForm(data=request.POST)

#         if form.is_valid():
#             new_comment = form.save(commit=False)
#             new_comment.pizza = pizza
#             new_comment.save()
#             form.save()
#             return redirect('pizzas:pizza', p_id=pizza_id)

#     context = {'form': form, 'pizza': pizza}
#     return render(request, 'pizzas/new_comment.html', context)


