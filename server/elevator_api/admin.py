from django.contrib import admin


from elevator_api.models import carmodel,ownermodel

admin.site.register(carmodel)
admin.site.register(ownermodel)
