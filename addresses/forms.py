from addresses.models import Person, Organisation
from django import forms


class PersonForm(forms.ModelForm):

    """
    ModelForm for creating/updating Person instances. All field properties are inherited from
    the Person model.
    """

    class Meta:
        model = Person
        fields = (
            'title',
            'firstname',
            'middlename',
            'surname',
            'telephone',
            'email',
            'organisation',
            'address_line1',
            'address_line2',
            'address_line3',
            'address_city',
            'address_county',
            'address_postcode',
        )


class OrganisationForm(forms.ModelForm):

    """
    ModelForm for creating/updating Organisation instances. All field properties are inherited from
    the Organisation model.
    """

    class Meta:
        model = Organisation
        fields = (
            'org_name',
            'telephone',
            'email',
            'address_line1',
            'address_line2',
            'address_line3',
            'address_city',
            'address_county',
            'address_postcode',
        )
