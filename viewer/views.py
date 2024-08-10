from django.shortcuts import render

from django.http import HttpResponse
from .forms import SignUpForm, ProductForm
from viewer import forms, models
from viewer import views
from viewer.models import Product
from django.views.generic import CreateView, FormView, TemplateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from logging import getLogger
from django.urls import reverse_lazy


LOGGER = getLogger()


class main(TemplateView):
    template_name = 'main_page.html'

class form(TemplateView):
    template_name = 'form.html'

class test(TemplateView):
    template_name = 'test.html'

class form(TemplateView):
    template_name = 'form.html'

class contact(TemplateView):
    template_name = 'contact.html'

class Candle(TemplateView):
    template_name = 'candles.html'
    extra_context = {'candles': models.Candle.objects.all()}

class Diffusor(TemplateView):
    template_name = 'diffusers.html'
    extra_context = {'diffusers': models.Diffusor.objects.all()}

class Gift_Card(TemplateView):
    template_name = 'gift_cards.html'
    extra_context = {'gift_cards': models.Gift_Card.objects.all()}

class Himalayan_Lavender_Oil(TemplateView):
    template_name = 'Himalayan_Lavender_Oil.html'
    extra_context = {'Himalayan_Lavender_Oil': models.Essential_Oil.objects.all()}
class User_Product(TemplateView):
    template_name = 'user_product.html'
    extra_context = {'user_product': models.User_Product.objects.all()}

class Essential_Oil_Guide(TemplateView):
    template_name = 'essential_oil_guide.html'

class Himalayan_Lavender_Oil(TemplateView):
    template_name = 'Himalayan_Lavender_Oil.html'

class SignUpView(CreateView):
    template_name = 'form.html'
    form_class = forms.SignUpForm
    success_url = reverse_lazy('index')

class ProductTable(TemplateView):
    template_name = 'product_table.html'
    extra_context = {'oils': models.Essential_Oil.objects.all()}

class ProductCreateView(FormView):
    template_name = 'form.html'
    form_class = forms.ProductForm
    success_url = reverse_lazy('product_table')

    def form_valid(self, form):
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data
        models.Product.objects.create(
            title=cleaned_data['title'],
        )
        return result

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data.')
        return super().form_invalid(form)
#
# class ProductTable(LoginRequiredMixin, ListView):
#     template_name = 'product_table.html'
#     model = Product
#     permission_required='viewer.add_movie'

class StuffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff

class ProductView(LoginRequiredMixin, ListView):
    template_name = 'product_table.html'
    model = Product

class ProductUpdateView(UpdateView):
    template_name = 'form.html'
    form_class = ProductForm
    success_url = reverse_lazy('product_table')
    model = Product

class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'form.html'
    form_class = ProductForm
    success_url = reverse_lazy('index')
    permission_required = 'viewer.change_product'

class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'delete.html'
    form_class = ProductForm
    success_url = reverse_lazy('index')
    permission_required = 'viewer.delete_product'

class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff
