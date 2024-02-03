from django import forms
from .models import Category

PRODUCT_CATEGORY = list()

for i in range(Category.objects.all().count()):
    PRODUCT_CATEGORY.append((i, Category.objects.all()[i].name))

class AddProductForm(forms.Form):
    name = forms.CharField(max_length=60)
    price = forms.IntegerField()
    photo = forms.ImageField(required=False)
    description = forms.CharField()
    category = forms.TypedChoiceField(choices=PRODUCT_CATEGORY, coerce = str)

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email_address = forms.EmailField(max_length=150)
    message = forms.CharField(widget=forms.Textarea,
                              max_length=2000)
    

class DeleteProductForm(forms.Form):
    name = forms.CharField(max_length=60)
  




    







  

