from django import forms

PRODUCT_QUANTITY_CHOISES = [(i, str(i)) for i in range(0, 51)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices = PRODUCT_QUANTITY_CHOISES,
        coerce=int, initial = 1
    )
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)    
