"""
  All models for the 'addresses' app:

  - Address (abstract base class)
  - Organisation(Address)
  - Person(Address)

"""

from django.db import models


class Address(models.Model):

    """
    Abstract base class for address/contact details; this will be used for both the 'Person' and 'Organisation'
    model as both require these common fields.
    """

    address_line1 = models.CharField(
        help_text='Address 1', max_length=100
    )

    address_line2 = models.CharField(
        help_text='Address 2', max_length=100, blank=True
    )

    address_line3 = models.CharField(
        help_text='Address 3', max_length=100, blank=True
    )

    address_city = models.CharField(
        help_text='City', max_length=50
    )

    address_county = models.CharField(
        help_text='County', max_length=50, blank=True
    )

    address_postcode = models.CharField(
        help_text='Postcode', max_length=10
    )

    telephone = models.CharField(
        help_text='Telephone Number', max_length=12, blank=True
    )

    email = models.EmailField(
        help_text='Email Address', max_length=100, blank=True
    )

    def composite_addr(self):

        """
        Return the first three lines of the address as a single string, with each line seperated
        by the '\n' line seperator.

        :return: str
        """

        addr = self.address_line1

        if self.address_line2:
            addr += '\n' + str(self.address_line2)

        if self.address_line3:
            addr += '\n' + str(self.address_line3)

        return addr

    class Meta:
        abstract = True


class Organisation(Address):

    """
    Organisation model - stores a single instance of an organisation. Inherits from 'Address' base class.
    """

    org_name = models.CharField(
        help_text='Organisation Name', max_length=50
    )

    def __str__(self):
        return self.org_name


class Person(Address):

    """
    Person Model - stores a single instance of a person/contact. Inherits from 'Address' base class.
    """

    title_choices = [
        ('Ms', 'Ms'),
        ('Miss', 'Miss'),
        ('Mrs', 'Mrs'),
        ('Mr', 'Mr'),
        ('Master', 'Master'),
        ('Mx', 'Mx'),
    ]

    title = models.CharField(
        help_text='Title', max_length=6, choices=title_choices, blank=True
    )

    firstname = models.CharField(
        help_text='First Name', max_length=50
    )

    middlename = models.CharField(
        help_text='Middle Name(s)', max_length=100, blank=True
    )

    surname = models.CharField(
        help_text='Surname', max_length=50
    )

    # Organisation foreign key (many-to-one relationship). Delete mode is set to 'SET_NULL' which sets this
    # field to null if the related organisation is deleted:

    organisation = models.ForeignKey(
        Organisation, help_text='Organisation Name', blank=True, null=True, on_delete=models.SET_NULL
    )

    def get_fullname(self):

        """
        This method returns the persons formatted full name, rather than just first name, surname etc.

        :return: str
            full name, formatted
        """

        fullname = self.firstname

        if self.middlename:
            fullname += ' ' + self.middlename

        return fullname + ' ' + self.surname

    def __str__(self):
        return self.get_fullname()
