from django.contrib import admin
from .Models import venue
from .Models import MyClubUser
from .Models import Event


admin.site.register(venue)
admin.site.register(MyClubUser)
admin.site.register(Event)
# Register your models here.


