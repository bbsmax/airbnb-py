from django.contrib import admin
from room.models import Room, RoomType

# Register your models here.

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass

@admin.register(RoomType)
class RoomType(admin.ModelAdmin):
    pass