from django.views import View
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

class IndexView(View):

    def get(self, request):
        return render(request, 'staffsite/login.html')


    # Login
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        # Checking user
        if user is not None:
            if user.is_staff and user.is_active :
                login(request, user)
                email = request.user.email
                return HttpResponse('<b>YOU ARE STAFF WITH EMAIL ' + email + '</b>')
            else:
                return render(request, 'staffsite/login.html')
        else:
            return render(request, 'staffsite/login.html')