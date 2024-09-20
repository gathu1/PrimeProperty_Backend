from django.urls import path

from type.views import *



urlpatterns = [
      path('api/type/', AddType.as_view(), name='add_type'),
      path('api/type/<int:pk>/', TypeRetrieveUpdateDestroyAPIView.as_view(), name='type-detail'),
      path('api/house/', AddHouse.as_view(), name='add_house'),
      path('api/house/<int:pk>/', HouseRetrieveUpdateDestroyAPIView.as_view(), name='house-detail'),
      path('api/user/', AddUser.as_view(), name='add_user'),
      path('api/user/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='user-detail'),
      path('api/tenant/', AddTenant.as_view(), name='add_tenant'),
      path('api/tenant/<int:pk>/', TenantRetrieveUpdateDestroyAPIView.as_view(), name='tenant-detail'),
      path('api/payment/', AddPayment.as_view(), name='add_payment'),
      path('api/payment/<int:pk>/', PaymentRetrieveUpdateDestroyAPIView.as_view(), name='payment-detail'),
      path('api/price/', AddPrice.as_view(), name='add_price'),
      path('api/contact/', AddContact.as_view(), name='add_contact'),
      path('api/maintenance/', AddMaintenance.as_view(), name='add_maintenance'),

]
