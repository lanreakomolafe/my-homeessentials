from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializergit remote add origin https://github.com/lanreakomolafe/my-homeessentials.git
git branch -M main
git push -u origin main