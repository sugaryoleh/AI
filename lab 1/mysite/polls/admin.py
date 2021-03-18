from django.contrib import admin

from polls.models import Question, Choice, PollResult, Poll

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(PollResult)
admin.site.register(Poll)
