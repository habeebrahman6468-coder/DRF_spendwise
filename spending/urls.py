from django.urls import path

from spending.views import SignUpview
from spending.views import GetmeView


urlpatterns=[

    path('register/',SignUpview.as_view()),
    path('user/',GetmeView.as_view()),

]