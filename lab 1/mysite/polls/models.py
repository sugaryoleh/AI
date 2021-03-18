import uuid

from django.contrib.auth.models import User
from django.db import models
from django.db.models import ForeignKey, CASCADE, CharField, DateTimeField, IntegerField, UUIDField
from django.utils import timezone

class Poll(models.Model):
    name = CharField(max_length=30, name='name')
    description = CharField(max_length=15000, name='description', default='')
    def __str__(self):
        return "id: {} name: {} ".format(self.id, self.name)

    @property
    def questions(self):
        return self.question_set.all()
    # def __call__(self, *args, **kwargs):
    #     try:
    #         obj = Poll.objeсts.get(pk=0)
    #     except:
    #         obj = Poll(id=0, name='default')
    #         obj.save()
    #     return obj

class Question(models.Model):
    poll = ForeignKey(Poll, on_delete=CASCADE)
    question_text = CharField('question_text', max_length=100)
    pub_date = DateTimeField('pub_date')

    @property
    def choices(self):
        return self.choice_set.all()

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - timezone.timedelta(days=1)

class Choice(models.Model):
    question = ForeignKey(Question, on_delete=CASCADE)
    choice_text = CharField('choice_text', max_length=100)
    choice_val = IntegerField('choice_val', default=2, null=True)
    votes = IntegerField('votes', default=0)

    def __str__(self):
        return self.choice_text

class PollResult(models.Model):
    user = ForeignKey(User, on_delete=CASCADE)
    novice = IntegerField(default=0, name='novice')
    advanced_beginner = IntegerField(default=0, name='advanced_beginner')
    competent = IntegerField(default=0, name='competent')
    proficient = IntegerField(default=0, name='proficient')
    expert = IntegerField(default=0, name='expert')

    # def __str__(self):
    #     return "{} {}: {} {}: {} {}: {} {}: {} {}: {}".format(str(self.user), self.novice.name,
    #                                                              self.novice, self.advanced_beginner.name, self.advanced_beginner,
    #                                                              self.competent.name, self.competent, self.proficient.name,
    #                                                              self.proficient, self.expert.name, self.expert)