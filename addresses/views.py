from django.shortcuts import render
from addresses.models import Person, Organisation

# Create your views here.


def homepage(request):

    people = Person.objects.all()
    orgs = Organisation.objects.all()

    return render(request, 'home.html', {'people': people, 'orgs': orgs})


def view_person(request, **kwargs):

    return render(request, 'person.html', {})


def update_person(request, **kwargs):

    return render(request, 'edit_person.html', {})


def view_org(request, **kwargs):

    return render(request, 'organisation.html', {})


def update_org(request, **kwargs):

    return render(request, 'edit_organisation.html', {})
