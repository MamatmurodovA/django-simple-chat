from django import forms

from chat.models import Conversation

class ConversationForm(forms.ModelForm):

	class Meta:
		model = Conversation
		fields = ['text']	