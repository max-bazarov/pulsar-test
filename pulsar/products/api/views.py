from django_filters.rest_framework import DjangoFilterBackend
from products.models import Product
from rest_framework import filters, viewsets
from rest_framework.parsers import MultiPartParser

from .serializers import ProductGetSerializer, ProductPostSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    parser_classes = (MultiPartParser, )
    filter_backends = (filters.SearchFilter, DjangoFilterBackend,)
    search_fields = ('name', 'code')
    filterset_fields = ('status', )

    def get_serializer_class(self):
        if self.action == 'create':
            return ProductPostSerializer
        return ProductGetSerializer
