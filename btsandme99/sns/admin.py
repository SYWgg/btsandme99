from django.contrib import admin
from sns.models import SNS

# Register your models here.
@admin.register(SNS)
class SNSAdmin(admin.ModelAdmin):
    list_display=('id','title','url')