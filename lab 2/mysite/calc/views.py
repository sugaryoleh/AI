import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.http import FileResponse, Http404
from django.views.decorators.clickjacking import xframe_options_sameorigin

from calc.calc import get_table, get_values


def index(request):
    return render(request, 'calc/index.html')

def data(request):
    table = get_table()
    mytable = "<table class='table table-striped'>"
    mytable+= "<thead><tr>"
    values = get_values()
    mytable += "<th scope='col'></th>"
    for value in values:
        mytable += "<th scope='col'>" + str(value) + "</th>"
    mytable+= "</tr></thead>"
    mytable += "<tbody"
    for val, row in zip(values, table):
        mytable += "<tr><th scope='row'>" + str(val) + "</th>"
        for cell in row:
            mytable += "<td>" + str(cell) + "</td>"
        mytable += "</tr>"
    mytable += "</tbody"
    mytable += "</table>"
    return JsonResponse({'data':mytable})

def charts(request):
    table = get_table()
    l = len(table)
    calc_vals = table[l-1]
    values = get_values()

    return JsonResponse({ 'data':
                              {'values':values,
                               'calc_vals':calc_vals
                               }
    })

def info(request):
    pdf_view = "<iframe src='http://127.0.0.1:8000/info_view'></iframe>"
    pdf_view = "<div class='embed-responsive embed-responsive-21by9'><iframe src='/info_view/' class='embed-responsive-item'></iframe></div>"
    return JsonResponse({'data':pdf_view})

@xframe_options_sameorigin
def info_view(request):
    try:
        return FileResponse(open('calc\\info.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()