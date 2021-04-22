import django
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.datetime_safe import datetime

from diseases._diseases import get_diseases
from diseases.forms import SignUpForm, DoctorSignUpForm
from diseases.models import Symptom, Speciality, Customer, Doctor, Disease, DiseaseHistory


def index(request):
    return render(request, 'diseases/index.html')

# not view
def get_customer_table(diseases):
    table = []
    symptoms = {s.name:i for s,i in zip(Symptom.objects.all(), range(1, len(Symptom.objects.all())+1))}
    _diseases = [d.name for d in Disease.objects.all()]
    table.append(['']+list(symptoms.keys()))
    for i, d in zip(range(len(diseases)), diseases):
        row = [_diseases[i]]
        row.extend([0 for i in range(len(symptoms))])
        for key, val in d.symptoms.items():
            row[symptoms[key.name]] = val
        table.append(row)
    return table


# not view
def diagnose(diseases, complains):
    l = []
    for d in diseases:
        s1 = set(s.name for s in d.symptoms)
        s2 = set(complains)
        print(s1)
        print(s2)
        if (s1 == s2):
            l.append(d.disease.name)
    return l



def complain(request, id):
    if request.method == 'POST':
        names = [s.name for s in Symptom.objects.all()]
        checked = []
        for name in names:
            try:
                if request.POST.get(name):
                    checked.append(name)
            except:
                pass
        diseases = get_diseases()
        table = get_customer_table(diseases)
        d = diagnose(diseases, checked)
        user = User.objects.get(pk=id)
        if d:
            for el in d:
                DiseaseHistory(disease=Disease.objects.get(name=el),
                customer=Customer.objects.get(user=user), date=django.utils.timezone.now()).save()

        return render(request, 'diseases/table.html', context={'table': table,
                                                               'diagnose': d})
    elif request.method == 'GET':
        user = User.objects.get(pk=id)
        print(user.username)
        customer = Customer.objects.get(user=user)
        print(customer.first_name)
        return render(request, 'diseases/complaint.html', context={'customer': customer,
                                                                   'symptoms': [obj.name for obj in
                                                                                Symptom.objects.all()]})

def signup(request, role):
    if role == 0:
        form = DoctorSignUpForm
    elif role == 1:
        form = SignUpForm
    if request.method == 'POST':
        form = form(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            if role == 0:
                Doctor(user=user, first_name=form['first_name'], last_name=form['last_name'], speciality=form['speciality']).save()
            elif role == 1:
                Customer(user=user, first_name=form['first_name'], last_name=form['last_name']).save()
            return redirect('login')
    else:
        form = form()
        context = {'form': form}
        if role == 0:
            context['specialities'] = (s.name for s in Speciality.objects.all())
    return render(request, 'auth/signup.html', context)

def _login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        print(user)
        if user in [obj.user for obj in Customer.objects.all()]:
            return redirect('complain/{}'.format(user.id))
        elif user in [obj.user for obj in Doctor.objects.all()]:
            return render(request, 'diseases/dr_table.html', context={'dh':DiseaseHistory.objects.all()})
        else:
            return HttpResponse('doesn\'t work')

