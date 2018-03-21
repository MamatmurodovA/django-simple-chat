from django.contrib import admin

# Register your models here.
from chat.models import *


class  ConversationAdmin(admin.ModelAdmin):
	list_display = ['sender', 'receiver', 'created_time']

admin.site.register(Conversation, ConversationAdmin)