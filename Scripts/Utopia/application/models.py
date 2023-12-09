from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_delete
from tinymce.models import HTMLField
from decimal import Decimal



class UsersPrimaryDetails(models.Model):
    UserID = models.IntegerField(primary_key=True)
    UserEmail = models.EmailField(max_length=254)
    UserFullName = models.CharField(max_length=255)
    UserGender = models.CharField(max_length=255)
    UserOccupation = models.CharField(max_length=255)
    UserDateOfBirth = models.DateField()
    UserRole = models.CharField(max_length=255)
    UserMobileNum = models.CharField(max_length=255)
    UserPoints = models.IntegerField()
    UserImageFilename = models.ImageField()
    UserAge=models.IntegerField()
    
    def __str__(self):
        return str(self.UserID)
    
class PoliticiansPrimaryDetails(models.Model):
    PoliticianID = models.OneToOneField(UsersPrimaryDetails,on_delete=models.CASCADE, primary_key=True)
    PoliticianRole = models.CharField(max_length=255)
    PoliticianName = models.CharField(max_length=256)
    TimeLeft = models.IntegerField()
    ElectionRun = models.IntegerField()
    ElectionWon = models.IntegerField()
    Pid=models.IntegerField()
    IsMP=models.BooleanField()
    IsMinister=models.BooleanField()
    
    def __str__(self):
        return str(self.PoliticianName)
    


class CountryConstituency(models.Model):
    ConstituencyName = models.CharField(max_length=255)
    TimeLeft = models.IntegerField()
    
    def __str__(self):
        return str(self.ConstituencyName)
    
    
class MPElection(models.Model):
    Candidate1ID= models.ForeignKey(UsersPrimaryDetails,on_delete=models.CASCADE,related_name="Candidate1ID")
    Candidate2ID= models.ForeignKey(UsersPrimaryDetails,on_delete=models.CASCADE,related_name="Candidate2ID")
    Candidate1Vote=models.IntegerField()
    Candidate2Vote=models.IntegerField()
    ElectionStatus=models.BooleanField()
    StartTime = models.DateTimeField(primary_key=True)
    EndTime=models.DateTimeField()
    Constituency=models.CharField(max_length=254)
    Cd1=models.IntegerField()
    Cd2=models.IntegerField()
    VoteDoneList=models.JSONField()
    
    def __str__(self):
        return str(self.StartTime)
    
    
    
class CountryMinistries(models.Model):
    MinistryName=models.CharField(max_length=300,primary_key=True)
    MinisterName=models.CharField(max_length=255)
    MinisterID=models.IntegerField()
    def __str__(self):
        return str(self.MinistryName)
    
    
class MinisterPrimaryDetails(models.Model):
    MinistryName=models.OneToOneField(CountryMinistries,on_delete=models.CASCADE)
    MinisterID=models.OneToOneField(PoliticiansPrimaryDetails,on_delete=models.CASCADE,primary_key=True)
    MinisterConstituency=models.CharField(max_length=254)
    MinisterNumberID=models.IntegerField()
    def __str__(self):
        return str(self.MinisterID)
    
    
    
class PublicOpinions(models.Model):
    UserID=models.IntegerField()
    Opinion=models.TextField(primary_key=True)
    
    def __str__(self):
        return str(self.Opinion)
    
class ImportantNotice(models.Model):
    Serial = models.IntegerField(primary_key=True)
    Title = models.CharField(max_length=255)
    Publish_date = models.DateField()

    def __str__(self):
        return str(self.Title)

class SeatAvailability(models.Model):
    UniversityName = models.CharField(max_length=255)
    DueTime = models.DateTimeField()
    AvailableSeats = models.IntegerField()

    def __str__(self):
        return str(self.UniversityName)
    
class Student(models.Model):
    student_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=128)

    def __str__(self):
        return str(self.name)
class Collage(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20)

    def __str__(self):
        return str(self.Name)
    
class Honours(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20)

    def __str__(self):
        return str(self.Name)
    
class Masters(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)

    def __str__(self):
        return str(self.Name)
class Appointment(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    facility = models.CharField(max_length=255)
    date = models.DateField()

class Bus(models.Model):
    bus_name = models.CharField(max_length=30)
    source = models.CharField(max_length=30)
    dest = models.CharField(max_length=30)
    nos = models.DecimalField(decimal_places=0, max_digits=2)
    rem = models.DecimalField(decimal_places=0, max_digits=2)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.bus_name


class UserB(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField()
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.email


class Book(models.Model):
    BOOKED = 'B'
    CANCELLED = 'C'

    TICKET_STATUSES = ((BOOKED, 'Booked'),
                       (CANCELLED, 'Cancelled'),)
    email = models.EmailField()
    name = models.CharField(max_length=100)
    bus_name = models.CharField(max_length=30)
    source = models.CharField(max_length=30)
    dest = models.CharField(max_length=30)
    nos = models.DecimalField(decimal_places=0, max_digits=2)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(choices=TICKET_STATUSES, default=BOOKED, max_length=2)

    def __str__(self):
        return self.email
class CarBook(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    facility = models.CharField(max_length=255)
    date = models.DateField()
    
class PlaneBook(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    facility = models.CharField(max_length=255)
    date = models.DateField()
    
class TrainBook(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    facility = models.CharField(max_length=255)
    date = models.DateField()