import xadmin
from .models import UserProfile


class UserProfileAdmin:
    list_display = ['user', 'phone']
    search_fields = ['phone']
    list_filter = ['user', 'phone']


xadmin.site.register(UserProfile, UserProfileAdmin)
