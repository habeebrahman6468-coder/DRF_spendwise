from django.urls import path

from spending.views import SignUpview
from spending.views import GetmeView
from spending.views import ExpenselistCreateView
from spending.views import ExpenseRetrieveUpdateDeleteView


urlpatterns=[

    path('register/',SignUpview.as_view()),
    path('user/',GetmeView.as_view()),
    path('expense/',ExpenselistCreateView.as_view()),
    path('expense/<int:pk>/',ExpenseRetrieveUpdateDeleteView.as_view()),

]