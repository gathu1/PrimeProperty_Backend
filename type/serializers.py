from rest_framework import serializers
from type.models import *

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['id','name','houseRange','totalAmount']


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ['id', 'category', 'description', 'location', 'price', 'total', 'remaining']        


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','name', 'username', 'password', 'user_type']   

class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = ['id','lname', 'fname', 'mname', 'email', 'contact', 'house', 'date']   

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id','tenant', 'invoice', 'amount']          


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ['id','fname', 'lname', 'email','contact', 'company', 'units']          


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id','yname', 'email', 'contact', 'department', 'company']          

class MaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintenance
        fields = ['name', 'contact', 'house', 'date', 'description']           