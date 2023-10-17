from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_delete
from tinymce.models import HTMLField



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
    
    
    
class News(models.Model):
    NewsTitle=models.CharField(max_length=1000,unique=True)
    Details=HTMLField()
    NewsNumber=models.IntegerField(primary_key=True)
    Posting_Time=models.DateTimeField()
    Channel_Name=models.CharField(max_length=500)
    Reporter_Name=models.CharField(max_length=500)
    ViewDoneList=models.JSONField()
    TotalView=models.IntegerField()
    
    def __str__(self):
        return str(self.NewsTitle)
    
    
    
class PublicOpinions(models.Model):
    UserID=models.IntegerField()
    Opinion=models.TextField(primary_key=True)
    
    def __str__(self):
        return str(self.Opinion)