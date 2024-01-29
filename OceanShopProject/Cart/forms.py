from django import forms

class CartAddProductForm(forms.Form):
    # PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, self.test)]
    # quantity_a = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    quantity = forms.FloatField(min_value=.0, initial=1.0, localize=False)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

    def __init__(self, *args, **kwargs) -> None:
        super(CartAddProductForm, self).__init__(*args, **kwargs)
        self.fields["quantity"].widget.attrs.update({"class": "quantitySelectionField"})