from django.contrib import admin

# Register your models here.
#* Importamos el modelo de post
from .models import Post
#* Registramos el modelo de post
admin.site.register(Post)