from django.contrib import admin

# Register your models here.

from .models import *
from .views import AddAdminView

@admin.register(ModelExample)
class ModelExampleAdmin(admin.ModelAdmin):
    actions = [AddAdminView.as_admin_view()]
