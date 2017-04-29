from django.shortcuts import render
from django import forms
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

class UserForm(forms.Form):
    username = forms.CharField(label='Username: ',max_length=100)
    password = forms.CharField(label='Password: ',widget=forms.PasswordInput())
    email = forms.EmailField(label='Email: ')

# Create your views here.
def register(request):
    if request.method == "POST":
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            email = uf.cleaned_data['email']
       	    user = User.objects.create_user(username=username, password=password, email=email)
            #user = User()
            #user.username = username
            #user.passworld = passworld
            #user.email = email
            user.save()
            #return render_to_response('success.html',{'username':username}, RequestContext(request))
	    return render(request, 'success.html',{'username':username})
    else:
        uf = UserForm()
    #return render_to_response('register.html',{'uf':uf}, RequestContext(request))
    return render(request, 'register.html',{'uf':uf})

def login_site(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
	print "longjing: " + username + " " + password 
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)    # <==
            return HttpResponseRedirect('/')
        else:
            return render(request, 'login.html', {
                'login_err': 'Please recheck your username or password !'
            })
    return render(request, 'login.html')
