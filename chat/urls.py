from django.contrib import admin
from django.urls import path
from chat.views import ChatView, ConversationView

app_name = 'chat'
urlpatterns = [
    path('chat/', ChatView.as_view(), name='chat_page'),
    path('chat/<str:sender>/', ConversationView.as_view(), name='chat_conversation'),
]