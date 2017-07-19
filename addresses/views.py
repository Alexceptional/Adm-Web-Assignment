from django.shortcuts import render, redirect
from addresses.models import Person, Organisation
from addresses.forms import PersonForm, OrganisationForm

# Create your views here.


def homepage(request):

    people = Person.objects.all()
    orgs = Organisation.objects.all()

    return render(request, 'home.html', {'people': people, 'orgs': orgs})


def view_person(request, **kwargs):

    person = Person.objects.get(id=kwargs['page_id'])

    return render(request, 'person.html', {'person': person})


def create_person(request):

    if request.method == 'POST':
        personform = PersonForm(request.POST)

        if personform.is_valid():
            newperson = personform.save()

            response = redirect(view_person, page_id=newperson.id)

        else:
            # MESSAGE?
            response = render(request, 'edit_person.html', {'form': personform})

    else:
        personform = PersonForm()

        response = render(request, 'edit_person.html', {'form': personform})

    return response


def update_person(request, **kwargs):
    person_inst = Person.objects.get(id=kwargs['page_id'])

    if request.method == 'POST':
        personform = PersonForm(request.POST, instance=person_inst)

        if personform.is_valid():
            newperson = personform.save()

            response = redirect(view_person, page_id=newperson.id)

        else:
            # MESSAGE?
            response = render(request, 'edit_person.html', {'form': personform, 'person': person_inst})

    else:
        if request.GET.get('delete'):
            person_inst.delete()

            response = redirect(homepage)

        else:
            person_inst = Person.objects.get(id=kwargs['page_id'])
            personform = PersonForm(instance=person_inst)

            response = render(request, 'edit_person.html', {'form': personform, 'person': person_inst})

    return response


def view_org(request, **kwargs):

    org = Organisation.objects.get(id=kwargs['page_id'])
    people = Person.objects.filter(organisation=org)

    return render(request, 'organisation.html', {'org': org, 'people': people})


def create_org(request):

    if request.method == 'POST':
        orgform = OrganisationForm(request.POST)

        if orgform.is_valid():
            neworg = orgform.save()

            response = redirect(view_org, page_id=neworg.id)

        else:
            # MESSAGE?
            response = render(request, 'edit_organisation.html', {'form': orgform})

    else:
        orgform = OrganisationForm()

        response = render(request, 'edit_organisation.html', {'form': orgform})

    return response


def update_org(request, **kwargs):
    org_inst = Organisation.objects.get(id=kwargs['page_id'])

    if request.method == 'POST':
        orgform = OrganisationForm(request.POST, instance=org_inst)

        if orgform.is_valid():
            neworg = orgform.save()

            response = redirect(view_org, page_id=neworg.id)

        else:
            # MESSAGE?
            response = render(request, 'edit_organisation.html', {'form': orgform, 'org': org_inst})

    else:
        if request.GET.get('delete'):
            org_inst.delete()

            response = redirect(homepage)

        else:
            org_inst = Organisation.objects.get(id=kwargs['page_id'])
            orgform = OrganisationForm(instance=org_inst)

            response = render(request, 'edit_organisation.html', {'form': orgform, 'org': org_inst})

    return response
