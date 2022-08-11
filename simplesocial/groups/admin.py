from django.contrib import admin
from . import models
# Register your models here.

# in admin config, we can edit group member in the group object
class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember

admin.site.register(models.Group)
