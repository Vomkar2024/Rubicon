from django.db import models

# Create your models here.
class Contact(models.Model):
    name : models.CharField(max_length=122)
    email : models.EmailField()
    phone : models.PhoneNumberField(_("Enter your phone number"))
    message : models.TextField()
    date : models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
