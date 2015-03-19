from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Field(models.Model):
   
    id = models.AutoField(primary_key=True)

    image_path = models.CharField(max_length=20)
    
    price = models.IntegerField(default=0)

    desc_text = models.CharField(max_length=200)

    stock_number = models.IntegerField(default=0)

    available_text = models.BooleanField( default = False )

    def __unicode__(self):
        #return str(self.id)
	return u"%s" % self.id

