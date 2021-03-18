from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic

from polls.models import Question, Choice, Poll, PollResult

values = []
steps = []
cnt = 1

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'poll_list'

    def get_queryset(self):
        return Poll.objects.all()[1:]

# shouldn't be here at all
def get_question(questions, id):
    i = 0
    for question in questions:
        if i == id:
           return question
        i+= 1

# shouldn't be here at all
def get_poll_result(user):
    try:
        pr = PollResult.objects.get(user=user)
    except:
        pr = PollResult(user=user)
        pr.save()
    else:
        return pr

# shouldn't be here at all
def nulify_poll_result(pr, poll_id):
    global values
    global steps
    global cnt
    cnt = 1
    values = []
    steps = []
    if poll_id == 1:
        pr.novice = 0
    elif poll_id == 2:
        pr.advanced_beginner = 0
    elif poll_id == 3:
        pr.competent = 0
    elif poll_id == 4:
        pr.proficient = 0
    elif poll_id == 5:
        pr.expert = 0
    pr.save()

@login_required
def detail_redirect(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    poll_result = get_poll_result(request.user)
    nulify_poll_result(poll_result, poll_id)
    print(poll_result)
    return HttpResponseRedirect(reverse('polls:detail', args=(poll_id, 0,)))

@login_required
def detail(request, poll_id, question_id):
    try:
        poll = Poll.objects.get(pk=poll_id)
        question = get_question(poll.question_set.all(), question_id)
    except:
        poll = None
    else:
        if question:
            context = { 'question': question,
                       'poll_id': poll_id,
                        'question_id': question_id
                    }
            return render(request, 'polls/detail.html', context)
        else:
            context = {
                'steps': steps,
                'values': values,
            }
            return render(request, 'charts/dyn_chart.html', context)
            #return HttpResponseRedirect(reverse('polls:index'))


# class DetailView(generic.DetailView):
#     model = Poll
#     template_name = 'polls/detail.html'
#
#
# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = 'polls/results.html'

@login_required
def vote(request, poll_id, question_id):
    global values
    global steps
    global cnt
    def update_res(user, poll_id, val):
        pr = get_poll_result(user)
        if poll_id == 1:
            pr.novice += val
        elif poll_id == 2:
            pr.advanced_beginner += val
        elif poll_id == 3:
            pr.competent += val
        elif poll_id == 4:
            pr.proficient += val
        elif poll_id == 5:
            pr.expert += val
        pr.save()

    poll = Poll.objects.get(pk=poll_id)
    question = get_question(poll.question_set.all(), question_id)
    print(question)
    # question = get_object_or_404(Question, pk=question_id)
    selected_choice = question.choice_set.get(pk=request.POST['choice'])
    print(selected_choice.choice_val)
    values.append(selected_choice.choice_val)
    steps.append('Question'+str(cnt))
    cnt+=1
    update_res(request.user, poll_id, selected_choice.choice_val)
    # try:
    #     selected_choice = question.choice_set.get(pk=request.POST['choice'])
    #     update_res(request.user, poll_id, selected_choice.choice_val)
    # except (KeyError, Choice.DoesNotExist):
    #     # Redisplay the question voting form.
    #     return render(request, 'polls/detail.html', {
    #         'question': question,
    #         'error_message': "You didn't select a choice.",
    #     })
    # else:
    #     selected_choice.votes += 1
    #     selected_choice.save()
    #     # Always return an HttpResponseRedirect after successfully dealing
    #     # with POST data. This prevents data from being posted twice if a
    #     # user hits the Back button.
    #     return HttpResponseRedirect(reverse('polls:results', args=(poll_id, question.id,)))
    return HttpResponseRedirect(reverse('polls:detail', args=(poll_id, question_id+1,)))

@login_required
def chart(request):
    if request.user.is_superuser:
        return superuser_chart(request)
    else:
        return common_user_chart(request)

def define_level(names, values):
    z = zip(values, names)
    mv = max(z)
    if mv[1] == 'Novice':
        return Poll.objects.get(pk=1)
    elif mv[1] == 'Advanced beginner':
        return Poll.objects.get(pk=2)
    elif mv[1] == 'Competent':
        return Poll.objects.get(pk=3)
    elif mv[1] == 'Proficient':
        return Poll.objects.get(pk=4)
    elif mv[1] == 'Expert':
        return Poll.objects.get(pk=5)
    return Poll.objects.get(pk=0)


@login_required
def common_user_chart(request):
    pr = get_poll_result(request.user)
    names = ['Novice', 'Advanced beginner', 'Competent', 'Proficient', 'Expert']
    values = [pr.novice, pr.advanced_beginner, pr.competent, pr.proficient, pr.expert]
    lvl = define_level(names, values)
    cur_lvl = lvl.name
    description = lvl.description

    context = {
        'names': names,
        'values': values,
        'cur_lvl':cur_lvl,
        'description':description
    }
    return render(request, 'charts/chart.html', context)

@login_required
def superuser_chart(request):
    values = [0, 0, 0, 0, 0]
    for obj in PollResult.objects.all():
        values[0]+=obj.novice
        values[1]+=obj.advanced_beginner
        values[2]+=obj.competent
        values[3]+=obj.proficient
        values[4]+=obj.expert
    names = ['Novice', 'Advanced beginner', 'Competent', 'Proficient', 'Expert']
    context = {
        'names': names,
        'values': values
    }
    return render(request, 'charts/chart.html', context)

