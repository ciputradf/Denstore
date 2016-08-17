from django.views import View
from django.shortcuts import render

class IndexView(View):

    def get(self, request):
        return render(request, 'staffsite/login.html')


    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_staff:
                return HttpResponse('<b>YOU ARE STAFF</b>')
            else:
                return HttpResponse('<b>YOU ARE NOT STAFF</b>')
        else:
            return HttpResponse('<b>YOU DONT HAVE ACCOUNT</b>')