from django.views.decorators.csrf import csrf_exempt

from rest_framework.viewsets import ModelViewSet
from rest_framework import generics, permissions

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer, CategoryRetrieveSerializer
from .permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryRetrieveSerializer
    permission_classes = [IsAdminOrReadOnly]
