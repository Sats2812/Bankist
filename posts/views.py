from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import *
from django.views.decorators.csrf import csrf_exempt
import random
from django.db.models import Q
userloggedin=0
def formatTransactions(transactions, type): 
    transactiontemp=[]
    for transaction in transactions:
        tran = {}
        tran["data"] = transaction
        tran["type"] = type
        transactiontemp.append(tran)
    return transactiontemp
def fetchAllTransactions(user):
    transactions=[]
    transactionsWithdraw=Transaction.objects.filter(fromid=user.id)
    transactions+=formatTransactions(transactionsWithdraw,"withdrawal")
    transactionDeposit=Transaction.objects.filter(toid=user.id)
    transactions+=formatTransactions(transactionDeposit,"deposit")
    return transactions
# Create your views here.
def index(request):
    return render(request,'index.html')

def form(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password==password2:
            if new_user.objects.filter(email=email).exists():
                messages.info(request,'Email already used')
                return redirect('/')
            elif new_user.objects.filter(username=username).exists():
                messages.info(request, 'Username already used')
                return redirect('/')
            else:
                new=new_user(username=username, email=email, password=password,password2=password2)
                new.save();
                return redirect('account')
        else:
            messages.info(request,'Passwords not the same')
            return redirect('/')
    else: 
        return render(request,'notfound')

def account(request):
    global userloggedin
    print("this is req: ",request)
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if new_user.objects.filter(username=username).exists():
            try:
                user = new_user.objects.get(username=username,password=password)
                if user.password == password:
                    print('Fetching transactions')
                    transactions=fetchAllTransactions(user)
                    print('Fetched transactions')
                    messages.info(request, '201')
                    userloggedin= user.id
                    if(user.debitcard_holder):
                        debitcardDetails = Debitcard.objects.get(userid=user)
                        return render(request,"account.html",{'transactions':transactions, "user_data":user, "debitcard":debitcardDetails})
                    return render(request,"account.html",{'transactions':transactions, "user_data":user})
                else: 
                    messages.info(request, 'username or password is wrong.')
                    return redirect("account")
            except:
                    messages.info(request, 'username or password is wrong.')
                    return redirect("account")

        else:
            messages.info(request, 'username or password is wrong.')
            return redirect("account")

    else:
        return render(request,'account.html')

def form(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password==password2:
            if new_user.objects.filter(email=email).exists():
                messages.info(request,'Email already used')
                return redirect('/')
            elif new_user.objects.filter(username=username).exists():
                messages.info(request, 'Username already used')
                return redirect('/')
            else:
                new=new_user(username=username, email=email, password=password)
                new.save();
                return redirect('account')
        else:
            messages.info(request,'Passwords not the same')
            return redirect('/')
    else: 
        return render(request,'notfound')

def contacts(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        new_contact=contact(name=name,subject=subject,message=message,email=email)
        new_contact.save();
        messages.info(request,'Thank you for contacting us , We will reach out to you soon')
        return redirect('contacts')
    else:
        return render(request,'contacts.html')

def getloan(request):
    if request.method =='POST':
        amount=request.POST['amount']
        user=new_user.objects.get(id=userloggedin)
        new_loan=Loan(amount=amount,uid=user)
        new_loan.save()
        user.balance+=int(amount)
        user.save()
        messages.info(request,'201')
        transactions = fetchAllTransactions(user)
        if(user.debitcard_holder):
            debitcardDetails = Debitcard.objects.get(userid=user)
            return render(request,"account.html",{'transactions':transactions, "user_data":user, "debitcard":debitcardDetails})
        return render(request,"account.html",{'transactions':transactions, "user_data":user})

def maketransaction(request):
    global userloggedin
    if request.method == 'POST':
        user = new_user.objects.get(id=userloggedin)
        touser=request.POST['touser']
        fromid=new_user.objects.get(id=userloggedin)
        toid=new_user.objects.get(username=touser)
        amount=request.POST['amount']
        transaction=Transaction(fromid=fromid, toid=toid, amount=amount)
        transaction.save()
        fromid.balance-=int(amount)
        toid.balance+=int(amount)
        fromid.save()
        toid.save()
        messages.info(request,'201')
        transactions = fetchAllTransactions(user)
        user = new_user.objects.get(id=userloggedin)
        if(user.debitcard_holder):
            debitcardDetails = Debitcard.objects.get(userid=user)
            return render(request,"account.html",{'transactions':transactions, "user_data":user, "debitcard":debitcardDetails})
        return render(request,"account.html",{'transactions':transactions, "user_data":user})

def getdebitcard(request):
    global userloggedin
    if request.method== 'POST':
        user_id=new_user.objects.get(id=userloggedin)
        card_no= ""
        for i in range(16):
            num=random.randint(1,9)
            card_no+=str(num)
        cvv=random.randint(100,999)
        debit=Debitcard(userid=user_id,card_no=card_no,cvv=cvv)
        debit.save()
        user_id.debitcard_holder=True
        user_id.save()
        transactions = fetchAllTransactions(user_id)
        debitcardDetails = Debitcard(userid=user_id)
        debitcardDetails.save()
        return render(request,"account.html",{'transactions':transactions, "user_data":user_id, "debitcard":debitcardDetails})