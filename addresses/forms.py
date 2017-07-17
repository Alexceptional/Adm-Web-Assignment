from addresses.models import Person, Organisation
from django import forms


class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = (
            'title',
            'firstname',
            'middlename',
            'surname',
            'address_line1',
            'address_line2',
            'address_line3',
            'address_city',
            'address_county',
            'address_postcode',
            'telephone',
            'email',
            'organisation',
        )


class OrganisationForm(forms.ModelForm):

    class Meta:
        model = Organisation
        fields = (
            'org_name',
            'org_address_line1',
            'org_address_line2',
            'org_address_line3',
            'org_address_city',
            'org_address_county',
            'org_address_postcode',
            'contact_telephone',
            'contact_email',
        )