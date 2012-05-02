from django.db import models

# Create your models here.


class SingletonModel(models.Model):
        
    class Meta:
        abstract = True
    

    def save(self, *args, **kwargs):
        self.id=1
        #import pdb;pdb.set_trace()
        if kwargs.has_key('force_insert'):
            del kwargs['force_insert']

        super(SingletonModel, self).save(*args, force_insert=False, **kwargs)

    def delete(self, *args, **kwargs):
        pass

class Info(SingletonModel):
    name = models.CharField("Author's first name.", max_length=30)
    surname = models.CharField("Author's surname.", max_length=30)
    date_of_birth = models.DateField("Authors birth date")
    bio = models.TextField()
    email = models.EmailField("Author's email")
    jabber = models.EmailField("Author's jabber id")
    skype = models.CharField("Skype id", max_length=30)
    other_contacts = models.TextField()
