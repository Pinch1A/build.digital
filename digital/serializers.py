from django.forms import widgets
from rest_framework import serializers
from digital.models import Field, LANGUAGE_CHOICES, STYLE_CHOICES


class FieldSerializer(serializers.ModelSerializer):
    
    class Meta:
       model = Field
       fields = ('id','image_path', 'price', 'desc_text', 'stock_number', 'available_text')
    
    
