"""
URL configuration for shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from store.views import index, product_detail, add_to_cart, cart, delete_cart
from shop import settings
from accounts.views import inscription, deconnexion, connexion

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('inscription/', inscription, name="inscription"),
    path('connexion/', connexion, name="connexion"),
    path('deconnexion/', deconnexion, name="deconnexion"),
    path('cart/', cart, name="cart"),
    path('cart/delete/', delete_cart, name="delete_cart"),
    path('product/<str:slug>/', product_detail, name="product"),
    path('product/<str:slug>/add_to_cart/', add_to_cart, name="add_to_cart"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
