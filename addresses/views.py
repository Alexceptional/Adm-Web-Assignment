"""
  All views for the 'address' app:

  - homepage
  - view_person
  - create_person
  - update_person
  - view_org
  - create_org
  - update_org

"""

from django.shortcuts import render, redirect
from addresses.models import Person, Organisation
from addresses.forms import PersonForm, OrganisationForm


def homepage(request):

    """
    Homepage - renders main page, including list of people and organisations in the
    address book.
    """

    # Query all entries from the database and add to context:
    people = Person.objects.all()
    orgs = Organisation.objects.all()

    return render(request, 'home.html', {'people': people, 'orgs': orgs})


def view_person(request, **kwargs):

    """
    View a single contact - fetch a person my their ID (passed as a keyword argument) and render
    with context.
    """

    person = Person.objects.get(id=kwargs['page_id'])

    return render(request, 'person.html', {'person': person})


def create_person(request):

    """
    Create a new person from a blank form. Either produces a blank form and renders, or takes a POST
    from a form submission, validates and either redirects if valid or re-renders form with errors
    if not valid.
    """

    # Handle form submission
    if request.method == 'POST':
        personform = PersonForm(request.POST)

        if personform.is_valid():
            # Save new instance of object and redirect to the person page.
            newperson = personform.save()

            response = redirect(view_person, page_id=newperson.id)

        else:
            # Re-render form with errors
            response = render(request, 'edit_person.html', {'form': personform})

    else:
        # Initialise blank form and render
        personform = PersonForm()

        response = render(request, 'edit_person.html', {'form': personform})

    return response


def update_person(request, **kwargs):

    """
    Update or delete a person. This function can accept either:

    - POST request, which initiates form validation and object update (or re-renders if errors)

    - GET request, which can either render the object instance as the form to edit/update the person, or
      reads a URL parameter 'delete' if a delete operation is required (will delete the object instance and
      redirect to home page).
    """

    person_inst = Person.objects.get(id=kwargs['page_id'])

    if request.method == 'POST':
        personform = PersonForm(request.POST, instance=person_inst)

        if personform.is_valid():
            newperson = personform.save()

            response = redirect(view_person, page_id=newperson.id)

        else:
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

    """
    View a single organisation - fetch an organisation by its ID (passed as a keyword argument), along with
    a list of people in that organisation, and render with context.
    """

    org = Organisation.objects.get(id=kwargs['page_id'])  # fetch organisation
    people = Person.objects.filter(organisation=org)  # fetch people in the organisation

    return render(request, 'organisation.html', {'org': org, 'people': people})


def create_org(request):

    """
    Create a new organisation from a blank form. Either produces a blank form and renders, or takes a POST
    from a form submission, validates and either redirects if valid or re-renders form with errors
    if not valid.
    """

    if request.method == 'POST':
        orgform = OrganisationForm(request.POST)

        if orgform.is_valid():
            neworg = orgform.save()

            response = redirect(view_org, page_id=neworg.id)

        else:
            response = render(request, 'edit_organisation.html', {'form': orgform})

    else:
        orgform = OrganisationForm()

        response = render(request, 'edit_organisation.html', {'form': orgform})

    return response


def update_org(request, **kwargs):

    """
    Update or delete an organisation. This function can accept either:

    - POST request, which initiates form validation and object update (or re-renders if errors)

    - GET request, which can either render the object instance as the form to edit/update the organisation, or
      reads a URL parameter 'delete' if a delete operation is required (will delete the object instance and
      redirect to home page).

    NOTE: based on settings in the Organisation model, deleting an organisation will not also delete all the
        related objects (people) via the foreignkey relationship; they will instead set the Organisation reference
        in the Person objects to NULL. This behaviour can be changed.
    """

    org_inst = Organisation.objects.get(id=kwargs['page_id'])

    if request.method == 'POST':
        orgform = OrganisationForm(request.POST, instance=org_inst)

        if orgform.is_valid():
            neworg = orgform.save()

            response = redirect(view_org, page_id=neworg.id)

        else:
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
