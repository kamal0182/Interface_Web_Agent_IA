from django.db import models
class User(models.Model)
    firstname = models.CharField(max_length=70)
    lastname  = models.CharField(max_length=70)
    email  = models.EmailField(unique=true)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
 
    def __str__(self) :
        return  "firstname :    " self.firstname , "lastname  :  " , self.lastname , "email : " self.email  
