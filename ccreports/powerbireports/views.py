from django.shortcuts import render

# Create your views here.

def login(request):

    if request.method == 'POST':
        usr = request.POST['user']
        password = request.POST['pass']
        if usr == 'antony' and password == '1testuser':
            return render(request,'reports.html')
        elif usr == 'antony2' and password == '2testuser':
            return render(request,'reports-2.html')
        else:
            return render(request, 'login.html')
    else:
        return render(request,'login.html')