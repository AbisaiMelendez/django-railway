from django.contrib import admin

# Register your models here.
from .models import Brand
from .models import Model
from .models import Series
from .models import Category
from .models import Inventory

admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(Series)
admin.site.register(Category)
admin.site.register(Inventory)