from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from shop import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('', views.cart, name='cart'),
    path('shop/', views.shop, name='shop'),
    path('shop/<str:category>/', views.category_products, name='category_products'),
    path('faq/', views.faq, name='faq'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)