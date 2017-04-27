from django.shortcuts import render
from django import forms
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from account.models import User

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
            passworld = uf.cleaned_data['password']
            email = uf.cleaned_data['email']
            user = User()
            user.username = username
            user.passworld = passworld
            user.email = email
            user.save()
            #return render_to_response('success.html',{'username':username})
	    return render(request, 'success.html',{'username':username})
    else:
        uf = UserForm()
    #return render_to_response('register.html',{'uf':uf})
    return render(request, 'register.html',{'uf':uf})
