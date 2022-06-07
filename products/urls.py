from django.urls import path, include

from .views import CategoryDetailView, CategoryListCreateView
from .routers import router

urlpatterns = [
    path('', include(router.urls)),
    path('cat/', CategoryListCreateView.as_view()),
    path('cat/<int:pk>/', CategoryDetailView.as_view())
]