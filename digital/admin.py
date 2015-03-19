from django.contrib import admin
from digital.models import Field

class FieldAdmin(admin.ModelAdmin):
    # ...
    list_display = ('id','image_path','price','desc_text','stock_number','available_text')

admin.site.register(Field)
# Register your models here.
