from django import forms 
from . models import Pizza, Topping, Comment

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['name']
        labels = {'name':''}

class ToppingForm(forms.ModelForm):
    class Meta:
        model = Topping
        fields = ['topping']
        labels = {'topping': ''}
        widgets = {'topping': forms.Textarea(attrs={'cols': 80})}

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols':80})}