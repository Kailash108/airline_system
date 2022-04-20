from django.shortcuts import render,redirect, HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate
from .models import Flightdetails,leaves
import datetime
x = datetime.datetime.now()


def logins(request):

    if request.method == "POST":
        username =request.POST['username']
        password =request.POST['pass']

        user = authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print('User logged in successful')
            return redirect('/login/booking')
        else:
            messages.info(request,'invalid credentials')
            print('Invalid credentials')
            return redirect('/login/login')    
    else:
        return render(request,'login/login.html')

def register(request):
    
    if request.method == "POST":
        first_name =request.POST['firstname']
        last_name =request.POST['lastname']
        username =request.POST['username']
        password =request.POST['pass']
        password1 =request.POST['pass1']
        email =request.POST['email']
        if password == password1:
            if User.objects.filter(username=username).exists():

                print('Username Exists or taken')
                messages.info(request,'Username already Exits')
                return redirect('/login/register')
                
                

            elif User.objects.filter(email=email).exists():
                print('Email already Exists')
                messages.info(request,'Email already Exits')
                return redirect('/login/register')
                
            else:
                user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print('Account created') 
                return redirect('/login/booking')

        else:
            print('password not matching')
            messages.info(request,'password not matching')
            return redirect('/login/register')
            
    
    else:
        return render(request,'login/register.html')
    

def logout(request):
    auth.logout(request)
    return render(request,'login/booking.html')
       

def feedback(request):
    return render(request,'login/feedback.html')

def explore(request):
    return render(request,'login/Explore.html')

    
def flightdetails(request):
    
    if request.method == 'POST':
        flightDetails=Flightdetails()
        flightDetails.Fnumber= request.POST.get('Fnumber')
        flightDetails.coname= request.POST.get('coname')
        flightDetails.fromdestination= request.POST.get('fromdest')
        flightDetails.todestination= request.POST.get('todest')
        flightDetails.nooftickets= request.POST.get('nooftickets')
        flightDetails.save();    
        print('Flight details saved')    
        
        # return render(request,'login/flightdetails.html')     

    else:
        print('flight details not yet saved 1')
        return render(request,'login/flightdetails.html')
           
    return render(request,'login/flightdetails.html')     

def booking(request):

    return render(request,'login/booking.html')  


def faq(request):
    return render(request,'login/faq.html')        

def contact(request):
    return render(request,'login/contact.html')    

def leave(request):
    if request.method == 'POST':
        Leaves= leaves()
        Leaves.Username= request.POST.get('username')
        Leaves.User_Id= request.POST.get('userid')
        Leaves.Mobile= request.POST.get('Mobilenumber')
        Leaves.Email= request.POST.get('Email')
       
        Leaves.Start_date= request.POST.get('sdate')
        Leaves.End_date= request.POST.get('edate')
        Leaves.comments= request.POST.get('comments')
        Leaves.save()
        print('leave details saved')
        return render(request,'login/leave.html') 
    else:
        print('leave details not updated')
        return render(request,'login/leave.html') 
         

def payment(request):    
    return render(request,'login/payment.html')     
    


def getFlights(request):
    if request.method == 'POST':
        flighttable = Flightdetails.objects.all()
        origin = request.POST.get('from')
        destination = request.POST.get('to')
        date = request.POST.get('departure')
        print(origin, destination)
        return render(request, 'login/flights.html',{
            'origin': origin, 
            'destination': destination,
            'date': date,
            'flighttable': flighttable
        })
    else: 
        return render(request,'login/flights.html') 

def book(request):
    flightNumber = request.POST.get('fID')
    flightDate = request.POST.get('fDate')
    flightCompany = request.POST.get('fCompany')
    flightFrom = request.POST.get('fFrom')
    flightTo = request.POST.get('fTo')
    flightFare = request.POST.get('fFare')
    flightBoarding = request.POST.get('fBoardingTime')
    flightArrival = request.POST.get('fArrivalTime')
    flightFee = 300
    request.session['flightNumber'] = flightNumber
    request.session['flightDate'] = flightDate
    request.session['flightCompany'] = flightCompany
    request.session['flightFrom'] = flightFrom
    request.session['flightTo'] = flightTo
    request.session['flightFare'] = flightFare
    request.session['flightBoarding'] = flightBoarding
    request.session['flightArrival'] = flightArrival
    request.session['flightFee'] = flightFee
    return render(request, 'login/book.html', {
        'flightNumber': flightNumber, 
        'flightDate': flightDate, 
        'flightCompany': flightCompany, 
        'flightFrom': flightFrom, 
        'flightTo': flightTo, 
        'flightFare': flightFare, 
        'flightBoarding':flightBoarding, 
        'flightArrival': flightArrival,
        'flightFee': flightFee,
        'flightFareTotal': float(flightFare) + float(flightFee),
    })

def ticket(request):
    fN = request.session.get('flightNumber')
    bD = x.strftime("%H")+':'+x.strftime("%M")
    bT = x.strftime("%d")+'-'+x.strftime("%m")+'-'+x.strftime("%Y")
    fD = request.session.get('flightDate')
    fC = request.session.get('flightCompany')
    fF = request.session.get('flightFrom')
    fT = request.session.get('flightTo')
    fFare = request.session.get('flightFare')
    fB = request.session.get('flightBoarding')
    fA = request.session.get('flightArrival')
    fFee = request.session.get('flightFee')
    return render(request, 'login/ticket.html', {
        'flightNumber': fN, 
        'bookingDate': bD,
        'bookingTime': bT,
        'flightDate': fD, 
        'flightCompany': fC, 
        'flightFrom': fF, 
        'flightTo': fT, 
        'flightFare': fFare, 
        'flightBoarding':fB, 
        'flightArrival': fA,
        'flightFee': fFee,
    })


      