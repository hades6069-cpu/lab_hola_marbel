from django.urls import path

from infrastructure.web.views import home


urlpatterns = [
    path('', home, name='home'),
]