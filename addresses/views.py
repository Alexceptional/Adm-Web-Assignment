from django.shortcuts import render
from addresses.models import Person, Organisation

# Create your views here.


def homepage(request):

    people = Person.objects.all()
    orgs = Organisation.objects.all()

    return render(request, 'home.html', {'people': people, 'orgs': orgs})


def view_person(request):

    return


def update_person(request):

    return


def view_org(request):

    return


def update_org(request):

    return
