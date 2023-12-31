from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.views.generic import RedirectView
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('EntryPage/', views.EntryPage, name='EntryPage'),
    path('RegistrationFormPage/',views.RegistrationFormPage,name='RegistrationFormPage'),
    path('',views.HomePage, name='HomePage'),
    path('VotingPage/',views.VotingPage,name='VotingPage'),
    path('ElectionSetupPage/',views.ElectionSetupPage,name='ElectionSetupPage'),
    path('MinistryPage/',views.MinistryPage,name='MinistryPage'),
    path('MinistySetupPage/',views.MinistrySetupPage,name='MinistrySetupPage'),
    path('TransportationPage/',views.TransportationPage,name='TransportationPage'),
    path('HealthcarePage/',views.HealthcarePage,name='HealthcarePage'),
    path('Education',views.Education,name='Education'),
    path('EntertainmentPage/',views.EntertainmentPage,name='EntertainmentPage'),
    path('Am_I_A_Citizen/',views.Am_I_A_CitizenPage,name='Am_I_A_CitizenPage'),
    path('NewsDetailsPage/<path:news>/',views.NewsDetailsPage, name='NewsDetailsPage'),
    path('AboutPage/',views.AboutPage,name='AboutPage'),
    path('ContactPage/',views.ContactPage,name='ContactPage'),
    path('HelpPage/',views.HelpPage,name='HelpPage'),
    path('TicketsPage/',views.TicketsPage,name='TicketsPage'),
    path('<path:undefined_path>/', views.Undefine),
    path('StudentLogin', views.StudentLogin, name='StudentLogin'),
    path('student-dashboard/', views.student_dashboard, name='student_dashboard'),

    path('Collage/', views.Collage,name='Collage'),
    path('Masters/', views.Masters,name='Masters'),
    path('Honours/', views.Honours,name='Honours'),
    path('Form/', views.Form,name='Form'),
    path('seat_availability/', views.seat_availability_view, name='seat_availability'),
    
 
    path('TransportationMain',views.TransportationMain,name='TransportationMain'), 
    path('BikeCategory',views.Bikecategory,name='BikeCategory'),
    path('CarCategory',views.Carcategory,name='CarCategory'),
    path('BusCategory',views.Buscategory,name='BusCategory'),
    path('TrainCategory',views.Traincategory,name='TrainCategory'),
    path('PlaneCategory',views.Planecategory,name='PlaneCategory'),
    path('PrivateBike', views.PrivateBike, name='PrivateBike'),
    path('PublicBike', views.PublicBike, name='PublicBike'),
    path('PrivateCar', views.PrivateCar, name='PrivateCar'),
    path('PublicCar', views.PublicCar, name='PublicCar'),
    path(' BusT', views.BusT, name='BusT'),
    path('PrivateTrain', views.PrivateTrain, name='PrivateTrain'),
    path('PublicTrain', views.PublicTrain, name='PublicTrain'),
    path('PrivatePlane', views.PrivatePlane, name='PrivatePlane'),
    path('PublicPlane', views.PublicPlane, name='PublicPlane'),
    path('HealthcareMain',views.HealthcareMain,name='HealthcareMain'), 
    path('Clinic',views.Clinic,name='Clinic'),
    path('Hospital',views.Hospital,name='Hospital'),
    path('Eyeclinic',views.Eyeclinic,name='Eyeclinic'),
    path('Diagnostic',views.Diagnostic,name='Diagnostic'),
    path('Pharmacy',views.Pharmacy,name='Pharmacy'),
    path('PrivateClinic', views.PrivateClinic, name='PrivateClinic'),
    path('PublicClinic', views.PublicClinic, name='PublicClinic'),
    path('PrivateHospital', views.PrivateHospital, name='PrivateHospital'),
    path('PublicHospital', views.PublicHospital, name='PublicHospital'),
    path('PrivateDiagnostic', views.PrivateDiagnostic, name='PrivateDiagnostic'),
    path('PublicDiagnostic', views.PublicDiagnostic, name='PublicDiagnostic'),
    path('PrivateEyeclinic', views.PrivateEyeclinic, name='PrivateEyeclinic'),
    path('PublicEyeclinic', views.PublicEyeclinic, name='PublicEyeclinic'),
    path('HospitalAppointmentPage', views.HospitalAppointmentPage, name='HospitalAppointmentPage'),
    path('PharmacyBookingPage', views.PharmacyBookingPage, name='PharmacyBookingPage'),
    path('DiagnosticAppointmentPage', views.DiagnosticAppointmentPage, name='DiagnosticAppointmentPage'),
    path('ClinicAppointmentPage', views.ClinicAppointmentPage, name='ClinicAppointmentPage'),
    path('EyeclinicAppointmentPage', views.EyeclinicAppointmentPage, name='EyeclinicAppointmentPage'),
    path('book_clinicappointment', views.book_clinicappointment, name='book_clinicappointment'),
    path('book_diagappointment', views.book_diagappointment, name='book_diagappointment'),
    path('book_eyeappointment', views.book_eyeappointment, name='book_eyeappointment'),
    path('book_hospitalappointment', views.book_hospitalappointment, name='book_hospitalappointment'),
    path('book_pharmacyappointment', views.book_pharmacyappointment, name='book_pharmacyappointment'),
    path('book_CAR', views.book_CAR, name='book_CAR'),
    path('book_PLANE', views.book_PLANE, name='book_PLANE'),
    path('book_TRAIN', views.book_TRAIN, name='book_TRAIN'),
    path('ThankYou', views.ThankYou, name='ThankYou'),
    path('PlaneTickets', views.PlaneTickets, name='PlaneTickets'),
    path('TrainTickets', views.TrainTickets, name='TrainTickets'),
    path('CarTickets', views.CarTickets, name='CarTickets'),
    path('BikeTickets', views.BikeTickets, name='BikeTickets'), 
    path('homebus', views.homebus, name="homebus"),
    path('findbus', views.findbus, name="findbus"),
    path('bookings', views.bookings, name="bookings"),
    path('cancellings', views.cancellings, name="cancellings"),
    path('seebookings', views.seebookings, name="seebookings"),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)