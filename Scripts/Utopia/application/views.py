import random
from django.utils.html import strip_tags
from django.urls import reverse
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib import messages
from django.db.models import Q
from .forms import *
from application.models import *

from itertools import chain
import os
import json
import pytz
import datetime
from datetime import date
# Create your views here.


def EntryPage(request):
    if request.method == 'POST':
        name = request.POST.get('button_name')
        if name == 'signup':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('pswd')
            form = RegisterForm(request.POST)
            if form.is_valid():
                my_usr = User.objects.create_user(username, email, password)
                my_usr.save()
                user = authenticate(request, username=username,
                                    password=password, email=email)
                login(request, user)
                return redirect('RegistrationFormPage')
            else:
                messages.error(request, 'This Username has already been taken')
        elif name == 'login':
            username = request.POST.get('username')
            password = request.POST.get('pswd')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(HomePage)
            else:
                messages.error(
                    request, ' The username or password you entered is incorrect')
        elif name == 'Guest':
            username = '1234'
            email = '1234@uap-bd.edu'
            password = 'AYONGHOSHAJOYGHOSH'
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(HomePage)
    request.session.clear()
    return render(request, 'EntryPage.html')


@login_required
def RegistrationFormPage(request):
    if request.method == 'POST':
        UserID = request.user.username
        UserEmail = request.user.email
        UserFullName = request.POST.get('full_name')
        UserGender = request.POST.get('gender')
        UserOccupation = request.POST.get('occupation')
        UserDateOfBirth = request.POST.get('date_of_birth')
        UserMobileNum = request.POST.get('mobile_number')
        UserPoints = 1000
        UserImageFilename = request.FILES.get('image')
        UserRole = request.POST.get('role')
        name = request.POST.get('save')
        birthday = date.fromisoformat(UserDateOfBirth)
        today = date.today()
        UserAge = today.year - birthday.year - \
            ((today.month, today.day) < (birthday.month, birthday.day))
        if UserImageFilename:
            UserImageFilename.name = f'{UserID}.jpg'
            with open(f'media/', 'wb') as f:
                f.write(UserImageFilename.read())
        if name == 'confirm':
            user_details = UsersPrimaryDetails(UserID, UserEmail, UserFullName, UserGender, UserOccupation,
                                               UserDateOfBirth, UserRole, UserMobileNum, UserPoints, UserImageFilename, UserAge)
            user_details.save()
            userocp = str(UserOccupation)
            if userocp.__contains__("Politician"):
                print(UserID)
                politician_details = PoliticiansPrimaryDetails(
                    UserID, UserRole, UserFullName, 0, 0, 0, UserID, False, False)
                politician_details.save()
            return redirect(HomePage)
    return render(request, 'RegistrationFormPage.html')


@login_required
def HomePage(request):
    UserID = request.user.username
    user = UsersPrimaryDetails.objects.get(UserID=UserID)
    host = user.UserImageFilename.url
    host = "http://127.0.0.1:8000/"+host
    context = {
        'user': user,
    }
    return render(request, 'HomePage.html', context)


@login_required
def VotingPage(request):
    if request.method == 'POST':
        UserID = request.user.username
        vote_setup = request.POST.get('save')
        now = datetime.datetime.now(pytz.timezone('UTC'))
        if vote_setup == 'setup':
            return redirect(ElectionSetupPage)
        Election = MPElection.objects.filter(EndTime__gte=now)
        for voteo in Election:
            one = json.loads(voteo.VoteDoneList)
            if str(UserID) not in one:
                if vote_setup == 'Cd1v':
                    voteo.Candidate1Vote += 1
                    one += str(UserID)
                    one = json.dumps(one, separators=(",", ","))
                    voteo.VoteDoneList = one
                if vote_setup == 'Cd2v':
                    voteo.Candidate2Vote += 1
                    one += str(UserID)
                    one = json.dumps(one, separators=(",", ","))
                    voteo.VoteDoneList = one
                voteo.save()
            else:
                messages.error(
                    request, 'You have already voted in this election.')
    timenow = datetime.datetime.now(pytz.timezone('UTC'))
    voting = MPElection.objects.filter(EndTime__lte=timenow)
    elc = MPElection.objects.filter(EndTime__gte=timenow)
    check = elc.exists()
    userid = int(request.user.username)
    ss = 00000000
    vc1 = 1
    vc2 = 1
    for vote in voting:
        vote.ElectionStatus = False
        vote.save()
        vc1 = 1
        vc2 = 1
    for vote in elc:
        vc1 = vote.Candidate1Vote
        vc2 = vote.Candidate2Vote
        vc3 = vc1+vc2
        if vc3 != 0:
            vc1 = vc1*100/vc3

            vc2 = vc2*100/vc3
            vc1 = round(vc1, 2)
            vc2 = round(vc2, 2)
    context = {
        'Elections': elc,
        'UserID': userid,
        'Check': check,
        'President': ss,
        'vc1': vc1,
        'vc2': vc2,
    }
    return render(request, 'VotingPage.html', context)


@login_required
def MinistryPage(request):
    if request.method == 'POST':
        minister_setup = request.POST.get('save')
        if minister_setup == 'setup':
            return redirect(MinistrySetupPage)
    UserID = int(request.user.username)
    objMinisterList = CountryMinistries.objects.exclude(MinisterName='1')
    ministerids = []
    for mid in objMinisterList:
        ministerids.append(mid.MinisterID)
    objUserPrimaryDetails = []
    objMinisterPrimaryDetails = []
    for id in ministerids:
        objUserPrimaryDetails += (UsersPrimaryDetails.objects.filter(UserID=id))
        objUserPrimaryDetails = list(objUserPrimaryDetails)
        objMinisterPrimaryDetails += (
            MinisterPrimaryDetails.objects.filter(MinisterNumberID=id))
        objMinisterPrimaryDetails = list(objMinisterPrimaryDetails)
    ss = 00000000
    context = {
        'UserID': UserID,
        'President': ss,
        'MinisterList': objMinisterPrimaryDetails,
        'MinisterDetails': objUserPrimaryDetails,
    }
    return render(request, 'MinistryPage.html', context)


@login_required
def ElectionSetupPage(request):
    if request.method == 'POST':
        Candidate1 = request.POST.get('Candidate1')
        Candidate2 = request.POST.get('Candidate2')
        Constituency = request.POST.get('Constituency')
        name = request.POST.get('save')
        Cd1 = int(Candidate1)
        Cd2 = int(Candidate2)
        findCandidate = PoliticiansPrimaryDetails.objects.filter(
            PoliticianID=Cd1)
        findCandidate1 = findCandidate.exists()
        findCandidate = PoliticiansPrimaryDetails.objects.filter(
            PoliticianID=Cd2)
        findCandidate2 = findCandidate.exists()
        findconstituency = CountryConstituency.objects.filter(
            ConstituencyName=Constituency)
        findconstituency0 = findconstituency.exists()
        print(findconstituency0, findCandidate1, findCandidate2)
        if (findCandidate1 is False or findCandidate2 is False or findconstituency0 is False):
            messages.error(
                request, 'could not find any matches for your input')
        elif Cd1 == Cd2:
            messages.error(
                request, 'Please select two different candidates.')
        else:
            time = datetime.datetime.now(pytz.timezone('UTC'))
            starttime = time
            time = increase_hour(time)
            endtime = time
            votedonelist = json.dumps("", separators=(",", ","))
            if name == "confirm":
                Election = MPElection(Candidate1, Candidate2,
                                      0, 0, True, starttime, endtime, Constituency, Cd1, Cd2, votedonelist)
                Election.save()
            return redirect(VotingPage)
    AfterElection = MPElection.objects.filter(ElectionStatus=False)
    for Ae in AfterElection:
        Constituency = Ae.Constituency
        Ca1 = Ae.Candidate1Vote
        Ca2 = Ae.Candidate2Vote
        Cd1 = Ae.Cd1
        Cd2 = Ae.Cd2
        if Ca1 > Ca2:
            WinnerID = Cd1
        elif Ca1 < Ca2:
            WinnerID = Cd2
        else:
            WinnerID = -800
            AePPd1 = PoliticiansPrimaryDetails.objects.get(Pid=Ae.Cd1)
            AePPd2 = PoliticiansPrimaryDetails.objects.get(Pid=Ae.Cd2)
            AePPd1.ElectionRun += 1
            AePPd2.ElectionRun += 1
            AePPd1.save()
            AePPd2.save()
        if Cd1 < Cd2 or Cd1 > Cd2:
            AePPd = PoliticiansPrimaryDetails.objects.get(Pid=WinnerID)
            AePPd.TimeLeft = 1
            AePPd.ElectionRun += 1
            AePPd.ElectionWon += 1
            AePPd.PoliticianRole = f'MP({Constituency})'
            AePPd.IsMP = True
            AePPd.save()
            AeUpd = UsersPrimaryDetails.objects.get(UserID=WinnerID)
            AeUpd.UserRole = f'MP({Constituency})'
            AeUpd.UserPoints += 1000
            AeUpd.save()
            obj_constituency = CountryConstituency.objects.get(
                ConstituencyName=Constituency)
            obj_constituency.TimeLeft = 1
            obj_constituency.save()
            Ae.ElectionStatus = True
            Ae.save()
    ConstituencyList = CountryConstituency.objects.filter(TimeLeft='0')
    PoliticiansList = PoliticiansPrimaryDetails.objects.filter(TimeLeft='0')
    context = {}
    context.update({"ConstituencyList": ConstituencyList})
    context.update({"PoliticiansList": PoliticiansList})
    return render(request, 'ElectionSetupPage.html', context)


@login_required
def MinistrySetupPage(request):
    if request.method == 'POST':
        MinistryName = request.POST.get('Ministry')
        MinisterName = request.POST.get('MP')
        name = request.POST.get('save')
        MinisterID = get_number_from_string(MinisterName)
        MinisterName = get_text_from_string(MinisterName)
        if name == 'confirm':
            ObjCountryMinistry = CountryMinistries.objects.get(
                MinistryName=MinistryName)
            ObjCountryMinistry.MinisterName = MinisterName
            ObjCountryMinistry.MinisterID = MinisterID
            objPoliticianPrimaryDetails = PoliticiansPrimaryDetails.objects.get(
                PoliticianID=MinisterID)
            objPoliticianPrimaryDetails.IsMinister = True
            tmpConstitutionName = extract_district_from_mp(
                objPoliticianPrimaryDetails.PoliticianRole)
            objMinisterPrimaryDetails = MinisterPrimaryDetails(
                MinistryName, MinisterID, tmpConstitutionName, MinisterID)
            objMinisterPrimaryDetails.save()
            objPoliticianPrimaryDetails.save()
            ObjCountryMinistry.save()
            return redirect(MinistryPage)

    PoliticiansList = PoliticiansPrimaryDetails.objects.filter(
        Q(IsMP=True) & Q(IsMinister=False))
    MinistriesList = CountryMinistries.objects.filter(MinisterName='1')
    context = {}
    context.update({"MpList": PoliticiansList})
    context.update({'MinistryList': MinistriesList})
    return render(request, 'MinistrySetupPage.html', context)


@login_required
def TransportationPage(request):
    return render(request, 'TransportationPage.html')


@login_required
def HealthcarePage(request):
    return render(request, 'HealthcarePage.html')


@login_required
def EducationPage(request):
    return render(request, 'EducationPage.html')


@login_required
def EntertainmentPage(request):
    return render(request, 'EntertainmentPage.html')


@login_required
def Am_I_A_CitizenPage(request):
    if request.method == 'POST':
        news = request.POST.get('save')
        if news == "confirm":
            userOpinion = request.POST.get('Opinions')
            opinion = PublicOpinions(request.user.username,userOpinion)
            opinion.save()
        else:
            return redirect(NewsDetailsPage, news)
    news = News.objects.all()
    opinions = PublicOpinions.objects.all()
    context = {
        'NEWS': news,
        'PublicOpinion': opinions
    }
    return render(request, 'Am-I-A-CitizenPage.html', context)


@login_required
def NewsDetailsPage(request, NewsNumber):
    newsDetails = News.objects.get(NewsNumber=NewsNumber)
    newsDetails.Details = strip_tags(newsDetails.Details)
    newsDetails.save()
    UserId = request.user.username
    one = json.loads(newsDetails.ViewDoneList)
    if str(UserId) not in one:
        one += str(UserId)
        newsDetails.TotalView += 1
        one = json.dumps(one, separators=(",", ","))
        newsDetails.ViewDoneList = one
    newsDetails.save()
    newsDetails = {
        'newsDetails': newsDetails,
    }
    return render(request, 'NewsDetailsPage.html', newsDetails)


@login_required
def AboutPage(request):
    return render(request, 'AboutPage.html')


@login_required
def ContactPage(request):
    return render(request, 'ContactPage.html')


@login_required
def HelpPage(request):
    return render(request, 'HelpPage.html')


@login_required
def TicketsPage(request):
    return render(request, 'TicketsPage.html')


def Undefine(request, undefined_path):
    # You can log the undefined_path if needed
    # Log the undefined_path variable or handle it in your preferred way
    # For now, we'll simply redirect to the homepage
    return redirect(HomePage)
