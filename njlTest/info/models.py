from django.db import models

# Create your models here.


class InfoSingleton(models.Model):
    name = models.CharField("Author's first name.", max_length=30, primary_key=True)
    surname = models.CharField("Author's surname.", max_length=30)
    date_of_birth = models.DateField("Authors birth date")
    bio = models.TextField()
    email = models.EmailField("Author's email")
    jabber = models.EmailField("Author's jabber id")
    skype = models.CharField("Skype id", max_length=30)
    other_contacts = models.TextField()

    def save(self, *args, **kwargs):
        "Updated save method to store only single item in the db"

        if self.__class__.objects.all().count(): 
        #There exists another object in the DB 
            obj = self.__class__.objects.all()[0] 
            for field in self._meta.fields: 
                if not field.name == self._meta.auto_field.name:
                    setattr(obj, field.name, getattr(self, field.name)) 
            super(InfoSingleton, obj).save(*args, **kwargs) 
        else: 
            super(InfoSingleton, self).save(*args, **kwargs) 

