from django.db import models

# Create your models here.


class Organisation(models.Model):

    """
    Organisation class. Field names for address are kept distinct from those of the person to
    avoid conflicts with HTML element IDs.

    """

    org_name = models.CharField(
        'Organisation Name', max_length=50
    )

    org_address_line1 = models.CharField(
        'Address 1', max_length=100
    )

    org_address_line2 = models.CharField(
        'Address 2', max_length=100, blank=True
    )

    org_address_line3 = models.CharField(
        'Address 3', max_length=100, blank=True
    )

    org_address_city = models.CharField(
        'City', max_length=50
    )

    org_address_county = models.CharField(
        'County', max_length=50
    )

    org_address_postcode = models.CharField(
        'Postcode', max_length=10
    )

    contact_telephone = models.CharField(
        'Telephone Number', max_length=12, blank=True
    )

    contact_email = models.EmailField(
        'Email Address', max_length=100, blank=True
    )

    def __str__(self):
        return self.org_name


class Person(models.Model):

    title_choices = [
        ('Ms', 'Ms'),
        ('Miss', 'Miss'),
        ('Mrs', 'Mrs'),
        ('Mr', 'Mr'),
        ('Master', 'Master'),
        ('Mx', 'Mx'),
    ]

    title = models.CharField(
        'Title', max_length=3, choices=title_choices, blank=True
    )

    firstname = models.CharField(
        'First Name', max_length=50
    )

    middlename = models.CharField(
        'Middle Name(s)', max_length=100, blank=True
    )

    surname = models.CharField(
        'Surname', max_length=50
    )

    address_line1 = models.CharField(
        'Address 1', max_length=100
    )

    address_line2 = models.CharField(
        'Address 2', max_length=100, blank=True
    )

    address_line3 = models.CharField(
        'Address 3', max_length=100, blank=True
    )

    address_city = models.CharField(
        'City', max_length=50
    )

    address_county = models.CharField(
        'County', max_length=50
    )

    address_postcode = models.CharField(
        'Postcode', max_length=10
    )

    telephone = models.CharField(
        'Telephone Number', max_length=12, blank=True
    )

    email = models.EmailField(
        'Email Address', max_length=100, blank=True
    )

    organisation = models.ForeignKey(Organisation)

    def __str__(self):
        return '{0} {1} {2}'.format(self.firstname, self.middlename, self.surname)
