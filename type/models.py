from django.db import models
from django.core.mail import send_mail
class Type(models.Model):
    name = models.CharField(max_length=100)
    houseRange = models.CharField(max_length=100)
    totalAmount = models.IntegerField()

    def __str__(self):
        return self.name
    
class House(models.Model):
    category = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='house')
    description = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    price = models.IntegerField()
    total = models.IntegerField()
    remaining = models.IntegerField()

    def __str__(self):
        return self.category
    
class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    user_type = models.CharField(max_length=100)

    def __str__(self):
        return self.name    
    
class Tenant(models.Model):
    lname = models.CharField(max_length=100)
    fname = models.CharField(max_length=100)
    mname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200) 
    contact = models.IntegerField()
    house = models.ForeignKey(Type, on_delete=models.CASCADE, related_name='tenant')
    date = models.DateField()

    def __str__(self):
        return self.fname      
    
class Payment(models.Model):
    tenant = models.CharField(max_length=100)
    invoice = models.CharField(max_length=100)
    amount = models.IntegerField()

    def __str__(self):
        return self.tenant     
    
class Price(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(max_length=200) 
    contact = models.IntegerField()
    company = models.CharField(max_length=200)
    units = models.IntegerField()

    def __str__(self):
        return self.fname      

class Contact(models.Model):
    yname = models.CharField(max_length=100)
    email = models.EmailField(max_length=200) 
    contact = models.IntegerField()
    department = models.CharField(max_length=200)
    company = models.CharField(max_length=200)

    def __str__(self):
        return self.yname  
              
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        send_mail(
            'New Contact Form Submission',
            f'Name: {self.yname} Email: {self.email} Contact: {self.contact} Department: {self.department} Company: {self.company}',
            '',
            ['gathu1.mar11n@gmail.com'],
            fail_silently=False,
        )
class Maintenance(models.Model):
    name = models.CharField(max_length=100)
    contact = models.IntegerField()
    house = models.CharField(max_length=200)
    date = models.DateField()
    description = models.CharField(max_length=500) 
    

    def __str__(self):
        return self.name     
    
class Vacancy(models.Model):
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    price = models.IntegerField()
    Remaining = models.IntegerField() 
    

    def __str__(self):
        return self.name    