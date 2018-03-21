from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class  Conversation(models.Model):
	sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender', default=1)
	receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver', default=1)
	text = models.TextField()
	created_time = models.DateTimeField(auto_now_add=True,)

	def __str__(self):
		return "from {} to {}".format(self.sender, self.receiver)