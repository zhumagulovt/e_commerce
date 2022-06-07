from django.urls import path

from .views import LoginView, RegistrationView, PasswordChangeView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('signup/', RegistrationView.as_view()),
    path('change-password', PasswordChangeView.as_view())
]