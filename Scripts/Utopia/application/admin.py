from django.contrib import admin
from application.models import *



# Register your models here.
admin.site.register(UsersPrimaryDetails)
admin.site.register(PoliticiansPrimaryDetails)
admin.site.register(CountryConstituency)
admin.site.register(MPElection)
admin.site.register(MinisterPrimaryDetails)
admin.site.register(CountryMinistries)
admin.site.register(PublicOpinions)


class SeatAvailabilityAdmin(admin.ModelAdmin):
    list_display = ('UniversityName', 'DueTime', 'AvailableSeats')

admin.site.register(SeatAvailability, SeatAvailabilityAdmin)
admin.site.register(ImportantNotice)
admin.site.register(Student)
admin.site.register(Collage)
admin.site.register(Honours)
admin.site.register(Masters)
admin.site.register(Appointment)
admin.site.register(Bus)
admin.site.register(UserB)
admin.site.register(Book)
admin.site.register(CarBook)
admin.site.register(TrainBook)
admin.site.register(PlaneBook)
