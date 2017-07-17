from django.contrib import admin
from addresses.models import Organisation, Person

# Register your models here.


admin.site.register(Person)
admin.site.register(Organisation)
