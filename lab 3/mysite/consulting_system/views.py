from django.http import HttpResponse
from django.shortcuts import render

from consulting_system.calc.calc import *

from django import template


register = template.Library()

@register.filter
def _index(indexable, i):
    return indexable[i]

def register(request):
    abilities = get_abilities()
    return render(request, 'consulting_system/register.html', context=
    {'abilities': abilities})


def index(request):
    abilities = get_abilities()
    specialities = get_specialities()
    candidates = get_candidates()
    ab_s_table = get_ability_speciality_table(abilities)
    ab_c_table = get_ability_candidate_table(abilities)
    return render(request, 'consulting_system/index.html', {
        'abilities':abilities,
        'specialities': specialities,
        'candidates':candidates,
        'ab_s_table':ab_s_table,
        'ab_c_table':ab_c_table
    })
    # return HttpResponse("Hello, world. You're at the polls index.")