from django.contrib import admin
from viewer import models
from django.urls import path
from viewer import views
import django.contrib.auth.views as auth_views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/sign_up/', views.SignUpView.as_view(), name='sign_up'),
    path('product_table/', views.ProductTable.as_view(), name='product_table'),
    path('product_create_view/', views.ProductCreateView.as_view(), name='product_create'),
    path('main_page/', views.main.as_view(), name='main_page'),
    path('form/', views.form.as_view(), name='form'),
    path('test/', views.test.as_view(), name='test'),
    path('contact/', views.contact.as_view(), name='contact'),
    path('candles/', views.Candle.as_view(), name='candles'),
    path('diffusers/', views.Diffusor.as_view(), name='diffusers'),
    path('gift_cards/', views.Gift_Card.as_view(), name='gift_cards'),
    path('user_product/', views.User_Product.as_view(), name='user_product'),
    path('essential_oil_guide/', views.Essential_Oil_Guide.as_view(), name='essential_oil_guide'),
    path('Himalayan_Lavender_Oil/', views.Himalayan_Lavender_Oil.as_view(), name='Himalayan_Lavender_Oil'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
