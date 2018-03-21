from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, View, CreateView
from django.views.generic.edit import ModelFormMixin
from django.db.models import Q
from django.contrib.auth.models import User

from chat.models import Conversation
from chat.forms import ConversationForm

class ChatView(TemplateView):
	template_name = 'chat.html'

	def get_context_data(self, **kwargs):
	    context = super(ChatView, self).get_context_data(**kwargs)
	    context['users'] = User.objects.all()
	    return context

class ConversationView(ListView):
	template_name = 'conversation_list.html'
	model = Conversation
	# form_class = ConversationForm

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context['users'] = User.objects.all()
		return context

	def get_queryset(self):
		sender = get_object_or_404(User, username=self.kwargs.get('sender'))
		messages = self.model.objects.filter(Q(sender=self.request.user, receiver=sender) | Q(sender=sender, receiver=self.request.user)).order_by('-created_time')

		return messages
	
	def post(self, request, *args, **kwargs):
		sender = get_object_or_404(User, username=kwargs.get('sender'))
		instance = self.model.objects.create(**{
				'sender': request.user,
				'receiver': sender,
				'text': request.POST.get('text')
			})


		self.object_list = self.get_queryset()
		context = self.get_context_data()
		return self.render_to_response(context)