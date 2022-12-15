from products.models import Product
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser
from rest_framework import filters

from .serializers import ProductGetSerializer, ProductPostSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    parser_classes = (MultiPartParser, )
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('name', 'code')
    filterset_fields = ('status', )

    def get_serializer_class(self):
        if self.action == 'create':
            return ProductPostSerializer
        return ProductGetSerializer
