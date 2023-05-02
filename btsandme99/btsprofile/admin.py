from django.contrib import admin
from btsprofile.models import BTSprofile_TBL

# Register your models here.
@admin.register(BTSprofile_TBL)
class BTSprofile_TBLAdmin(admin.ModelAdmin):
    list_display=('id','name','group')