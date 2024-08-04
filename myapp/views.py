from django.shortcuts import render,redirect
from django.http import HttpResponse
from .import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required


# Create your views here.


def home(request):
    # print(request.GET)
    # print(request.POST)
    # print(request.method)

    data = {'students':[{'name':'musa','age':19},{'name':'suhail','age':20},{'name':'mehtab','age':19}]}
    return render(request,'home.html',data)



def home1(request):
    data = {'numbers':[2,3,4,5,6,7,8,9,10]}
    return render(request,'home.html',data)



def home2(request):
    data = {'prime':[9]}
    return render(request,'home.html',data)




def information(request):
    # student1 = models.Student(1,'musa',19)
    # student1.save()
    student2 = models.Student(2,'shahab',24)
    student2.save()
    return  HttpResponse("this is info page")






# <------------------------------------------ student management system --------------------------------------->




def students(request):
    # data1 = models.Student.objects.all().values()  # ye tables ke sara values browers par show kar dega

    # data2 = models.Student.objects.filter(std_name = 'musa').values() #or ye jaha name musa hoga usi column ko

    # data2 = models.Student.objects.filter(std_id = 1,std_name = 'musa').values() #or ye dono sahi hoga tabhi return

    data3 = list(models.Student.objects.filter(std_id = 2).values())# in mai se koe ek/dono sahi hona chahiye
    data4 = list(models.Student.objects.filter( std_name= 'musa').values())# in mai se koe ek/dono sahi hona chahiye
    data = data3 + data4

    return HttpResponse(data)



def update(request):
    std = models.Student.objects.all()
    # models.Student.objects.filter(std_id = 2).update(std_name = 'mehtab',std_age = 15)
    models.Student.objects.filter(std_id = 2).delete()

    return HttpResponse('update successfully')




def addstudent(request):

    return render(request,'addstudents.html')



def submitstudent(request):
    data = dict(request.GET)
    
    id = int(data['id'][0])
    name = data['name'][0]
    age = int(data['age'][0])

    std = models.Student(id,name,age)
    std.save()

    return redirect('/allstudents')



def allstudents(request):
    data = list(models.Student.objects.all().values())

    return render(request,'allstudents.html',{'students':data})










# <------------------------------------------ library management system --------------------------------------->




def library(request):

    return render(request,'library.html')



@login_required(login_url="/userlogin")
def addbook(request):
    data = dict(request.GET)
    
    B_id = int(data['B_id'][0])
    B_name = data['B_name'][0]
    Subject = data['Subject'][0]
    Description = data['Description'][0]
    Semester = int(data['Semester'][0])
    Quantity = int(data['Quantity'][0])
    Price = int(data['Price'][0])

    data = models.Book(B_id,B_name,Subject,Description,Semester,Quantity,Price)
    data.save()

    return HttpResponse("<h1>ADD BOOK SUCCESSFULLY</h1>")



@login_required(login_url="/userlogin")
def updatebook(request):
    data = dict(request.GET)
    
    uB_id = int(data['uB_id'][0])
    uB_name = data['uB_name'][0]
    uSubject = data['uSubject'][0]
    uDescription = data['uDescription'][0]
    uSemester = int(data['uSemester'][0])
    uQuantity = int(data['uQuantity'][0])
    uPrice = int(data['uPrice'][0])

    data = models.Book.objects.filter(B_id=uB_id).update(B_id=uB_id,B_name=uB_name,Subject=uSubject,Description=uDescription,Semester=uSemester,Quantity=uQuantity,Price=uPrice)

    return redirect('/seeallbook',{'update':data})


@login_required(login_url="/userlogin")
def deletebook(request):
    data = dict(request.GET)
    uB_id = int(data['uB_id'][0])

    models.Book.objects.filter(B_id = uB_id).delete()

    return redirect('/seeallbook')




@login_required(login_url="/userlogin")
def seeallbook(request):
    data = list(models.Book.objects.all().values())

    return render(request,'seeallbook.html',{'books':data})






@login_required(login_url="/userlogin")
def addmember(request):
    data = dict(request.GET)
    
    M_id = int(data['M_id'][0])
    M_name = data['M_name'][0]
    Mobile_number = int(data['Mobile_number'][0])
    Semester = int(data['Semester'][0])
    Branch = data['Branch'][0]
    

    data = models.Members(M_id,M_name,Mobile_number,Semester,Branch)
    data.save()

    return HttpResponse("<h1>ADD MEMBER SUCCESSFULLY </h1>")






@login_required(login_url="/userlogin")
def updatemember(request):
    data = dict(request.GET)
    
    uM_id = int(data['uM_id'][0])
    uM_name = data['uM_name'][0]
    uMobile_number = int(data['uMobile_number'][0])
    uSemester = int(data['uSemester'][0])
    uBranch = data['uBranch'][0]
    

    data = models.Members.objects.filter(M_id=uM_id).update(M_id=uM_id,M_name=uM_name,Mobile_number=uMobile_number,Semester=uSemester,Branch=uBranch)

    

    return redirect('/seeallmember')






@login_required(login_url="/userlogin")
def deletemember(request):
    data = dict(request.GET)

    uM_id = int(data['uM_id'][0])

    models.Members.objects.filter(M_id = uM_id).delete()

    return redirect('/seeallmember')





@login_required(login_url="/userlogin")
def seeallmember(request):
    data = list(models.Members.objects.all().values())

    return render(request,'seeallmember.html',{'members':data})








@login_required(login_url="/userlogin")
def addrecord(request):
    data = dict(request.GET)
    
    R_id = int(data['R_id'][0])
    Member_id = int(data['Member_id'][0])
    Member_Name = data['Member_Name'][0]
    Book_id = int(data['Book_id'][0])
    Book_name = data['Book_name'][0]
    B_issue_date = data['B_issue_date'][0]
    B_return_date = data['B_return_date'][0]
    Status = data['Status'][0]
    
    book1=models.Book.objects.filter(B_id = Book_id).first()
    book1.Quantity = book1.Quantity-1
    book1.save()

    data = models.Records(R_id,Member_id,Member_Name,Book_id,Book_name,B_issue_date,B_return_date,Status)
    data.save()

    return HttpResponse("<h1> ADD RECORDS SUCCESSFULLY </h1>")






@login_required(login_url="/userlogin")
def updaterecord(request):
    data = dict(request.GET)

    uR_id = int(data['uR_id'][0])
    uMember_id = int(data['uMember_id'][0])
    uMember_Name = data['uMember_Name'][0]
    uBook_id = int(data['uBook_id'][0])
    uBook_name = data['uBook_name'][0]
    uB_issue_date = data['uB_issue_date'][0]
    uB_return_date = data['uB_return_date'][0]
    uStatus = data['uStatus'][0]

    book1=models.Book.objects.filter(B_id = uBook_id).first()
    book1.Quantity = book1.Quantity+1
    book1.save()
    

    data = models.Records.objects.filter(R_id=uR_id).update(R_id = uR_id, Member_id = uMember_id, Member_Name = uMember_Name, Book_id=uBook_id, Book_name=uBook_name, B_issue_date=uB_issue_date, B_return_date=uB_return_date, Status=uStatus)



    return redirect('/seeallrecord')





@login_required(login_url="/userlogin")
def deleterecord(request):
    data = dict(request.GET)

    uR_id = int(data['uR_id'][0])

    models.Records.objects.filter(R_id = uR_id).delete()

    return redirect('/seeallrecord')






@login_required(login_url="/userlogin")
def seeallrecord(request):
    data = list(models.Records.objects.all().values())

    return render(request,'seeallrecord.html',{'records':data})














# <------------------------------------------ AUTHENTICATE AUTHENTICATION  --------------------------------------->








def usersignup(request):
    signupform = UserCreationForm()
    return render(request,'signup.html',{'signupform':signupform})



def handlesignup(request):
    data = request.POST
    user = UserCreationForm(data)

    if user.is_valid():
        user.save()
        return redirect('/userlogin')
    else:
        return redirect('/usersignup')
    
    



def userlogin(request):
    return render(request,'login.html')



def handlelogin(request):
    data = request.POST
    username = data['username']
    password = data['password']

    user = authenticate(request=request,username=username,password=password)

    if user:
        login(request,user)
        return redirect('/library')
    else:
        return redirect('/userlogin')
    


def userlogout(request):
    logout(request)

    return HttpResponse("<h1 style='color:blue'>logged out <span style='color:green'>successfully<span></h1>")
