from django.contrib import admin
from .models import Contact
from .models import Images


# Register your models here.

class Comments(admin.ModelAdmin):
  admin.site.site_header = "Kitan cleaning"
  admin.site.site_title ="Cleaning service"
  admin.site.index_title ="Cleaning service"
  list_display = ('name','email','phone','message')
  list_editable =  ('email','phone','message')


class Image_comment(admin.ModelAdmin):
  list_display = ('image',)

admin.site.register(Contact,Comments)
admin.site.register(Images,Image_comment)
