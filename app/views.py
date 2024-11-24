from rest_framework import generics , permissions 
from rest_framework.permissions import IsAuthenticated
from .models import Product,CustomUser
from .serializers import ProductSeralizer,CustomUserSerializer
from .permissions import IsVendor 
# Create your views here.


class UserRegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]
    
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSeralizer
    permission_classes = [IsAuthenticated,IsVendor]
    
    def perform_create(self, serializer):
        serializer.save(vendor=self.request.user)
        
class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSeralizer 
    permission_classes = [IsAuthenticated]
    
    def get_permissions(self):
        if self.request.method in ['PUT','PATCH','DELETE']:
            self.permission_classes = [IsAuthenticated,IsVendor]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()
    
    class ProductByNameView(generics.ListAPIView):
        serializer_class = ProductSeralizer
        permission_classes = [IsAuthenticated]
        def get_queryset(self):
            name = self.kwargs['name']
            return Product.objects.filter(name=name)
    
    
    
    