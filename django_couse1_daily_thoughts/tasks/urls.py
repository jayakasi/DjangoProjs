from django.urls import path
from . import views

urlpatterns = [
    path("",views.index),
    path("<int:day>",views.daily_thoughts_by_number),
    path("<str:day>",views.daily_thoughts, name="daily-thoughts")
]