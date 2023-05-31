from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from inventory_management.models import Category, Product, Supplier
from inventory_management.api.serializers import CategorySerializer, ProductSerializer, SupplierSerializer

class ProductList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class ProductDetail(APIView):
    def get(self, request, id=None):
        products = Product.objects.filter(id=id)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class CategoryListView(APIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SupplierListView(APIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


