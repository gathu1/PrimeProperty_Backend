from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from type.serializers import *
from type.models import *

from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from django.http import JsonResponse, HttpResponseNotFound
from django.views.decorators.http import require_http_methods

class AddType(generics.ListCreateAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = [AllowAny]

class TypeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    permission_classes = [AllowAny]

class AddHouse(generics.ListCreateAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    permission_classes = [AllowAny]  

class HouseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = House.objects.all()
    serializer_class = HouseSerializer
    permission_classes = [AllowAny]

class AddUser(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny] 

class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]    

class AddTenant(generics.ListCreateAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
    permission_classes = [AllowAny]      

class TenantRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
    permission_classes = [AllowAny]

class AddPayment(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [AllowAny] 

class PaymentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [AllowAny]    

class AddPrice(generics.ListCreateAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
    permission_classes = [AllowAny]    

class AddContact(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [AllowAny]    

class AddMaintenance(generics.ListCreateAPIView):
    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceSerializer
    permission_classes = [AllowAny]      

# class AddType(APIView):

#     def post(self, request, *args, **kwargs):
#         serializer = TypeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()

#             return Response({'status': 'success', 'name': serializer.data}, status=status.HTTP_201_CREATED)
        
#         return Response({'status': 'error', 'name': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
#     def get(self, request, *args, **kwargs):
#         serializer = TypeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()

#             return Response({'status': 'success', 'name': serializer.data}, status=status.HTTP_201_CREATED)
        
#         return Response({'status': 'error', 'name': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
# class AddHouse(APIView):

#     def post(self, request, *args, **kwargs):
#         serializer = HouseSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()

#             return Response({'status': 'success', 'house': serializer.data}, status=status.HTTP_201_CREATED)
        
#         return Response({'status': 'error', 'house': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)    

#     def get(self, request, *args, **kwargs):
#         serializer = HouseSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()

#             return Response({'status': 'success', 'house': serializer.data}, status=status.HTTP_201_CREATED)
        
#         return Response({'status': 'error', 'house': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)    