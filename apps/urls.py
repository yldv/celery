from django.urls import path

from .views import EmailMessageView

urlpatterns = [
    path('email/', EmailMessageView.as_view(), name='emailmessage'),
]