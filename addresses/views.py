from django.shortcuts import render
from addresses.models import Person, Organisation

# Create your views here.


def homepage(request):

    people = Person.objects.all()
    orgs = Organisation.objects.all()

    return render(request, 'home.html', {'people': people, 'orgs': orgs})


def view_person(request, **kwargs):

    person = Person.objects.get(id=kwargs['page_id'])

    return render(request, 'person.html', {'person': person})


def update_person(request, **kwargs):

    return render(request, 'edit_person.html', {})


def view_org(request, **kwargs):

    org = Organisation.objects.get(id=kwargs['page_id'])
    people = Person.objects.filter(organisation=org)

    return render(request, 'organisation.html', {'org': org, 'people': people})


def update_org(request, **kwargs):

    return render(request, 'edit_organisation.html', {})
