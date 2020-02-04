from django.conf.urls import url
from .views import view_cart, add_to_cart, adjust_cart


urlpatterns = [
    url(r'^$', view_cart, name='view_cart'),
    url(r'^add', add_to_cart, name='add_to_cart'),
    url(r'^adjust', adjust_cart, name='adjust_cart'),
]
