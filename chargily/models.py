from django.db import models

class Client(models.Model):
    created= models.DateTimeField(auto_now_add=True)
    username= models.CharField(max_length=30)
    email= models.CharField(max_length=50)
    
class Invoice(models.Model):
    invoiceNumber = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    backUrl = models.CharField(max_length=200)
    webhookUrl = models.CharField(max_length=200)
    client= models.ForeignKey(Client, on_delete=models.CASCADE)
    amount =models.FloatField(max_length=75)
    discount = models.IntegerField()
    comment= models.TextField(max_length=255,blank=True,null=True)
    CIB ='CIB'
    EDAHABIA ='EDAHABIA'
    MODE_CHOICES= [
        (CIB, 'CIB'),
        (EDAHABIA, 'EDAHABIA'),
    ]
    mode = models.CharField(max_length=15, choices=MODE_CHOICES, default=EDAHABIA,)
    
    def __str__(self):
        return f"Invoire(id={self.invoiceNumber})"