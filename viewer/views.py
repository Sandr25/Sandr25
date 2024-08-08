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

class SignUpView(CreateView):
    template_name = 'form.html'
    form_class = forms.SignUpForm
    success_url = reverse_lazy('index')

class ProductTable(TemplateView):
    template_name = 'product_table.html'
    extra_context = {'product': models.Product.objects.all()}

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

class ProductTable(LoginRequiredMixin, ListView):
    template_name = 'product_table.html'
    model = Product
    permission_required='viewer.add_movie'

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
