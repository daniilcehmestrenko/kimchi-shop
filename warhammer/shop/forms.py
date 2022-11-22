from django import forms

from .models import Comments


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
                choices=PRODUCT_QUANTITY_CHOICES,
                coerce=int,
            )
    update = forms.BooleanField(
                required=False,
                initial=True,
                widget=forms.HiddenInput,
            )


class AddCommentForm(forms.ModelForm):
    
    class Meta:
        model = Comments
        fields = ('user_name', 'email', 'content')
