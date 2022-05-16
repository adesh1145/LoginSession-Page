from django.contrib import admin
from signup_page.models import signup_detail
# Register your models here.

class signup_admin(admin.ModelAdmin):
    list_display=('uname','id','email_name','fname','lname','pass1',)

admin.site.register(signup_detail,signup_admin)
