import django.forms as f
from django.contrib.auth.forms import UserCreationForm
import viewer.models as models
from django.forms import (CharField, DateField, Form, IntegerField, ModelChoiceField, Textarea)
from viewer.models import Product

class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ("username", "first_name", "last_name")

    def save(self, commit=True):
        self.instance.is_active = False
        return super().save(commit)

def validate_capitalized(s):
    if s[0].islower():
        raise f.ValidationError('Value must be capitalized')

class ProductForm(Form):
    name = CharField(max_length=255)
    price = IntegerField(min_value=1, max_value=1000)
    stock = IntegerField(min_value=1, max_value=1000)
    product = ModelChoiceField(queryset=Product.objects.all())