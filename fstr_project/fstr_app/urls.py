from django.urls import path
from . import views

urlpatterns = [
    path('submit_data/', views.SubmitDataView.as_view()),
]