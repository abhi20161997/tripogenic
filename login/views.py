from django.shortcuts import render, redirect
from .forms import  UserForm
from django.contrib.auth import authenticate, login, logout
from .forms import AuthenticateForm, UserForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views import generic
from django.views.generic import View

@csrf_exempt
def index(request):
	user = request.user

	if user.is_authenticated():

		return render(request, 'login/tripogenic3.html', {'user':user})
	else:

		return render(request, 'login/tripogenic3.html', {'user':user})

@csrf_exempt
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
             
                return HttpResponseRedirect('/')
            else:
                return render(request, 'login/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'login/login.html', {'error_message': 'Invalid login'})
    return render(request, 'login/login.html')

@login_required
def logout_view(request):
	logout(request)
	return redirect('/')


class UserFormView(View):
	form_class = UserForm
	template_name = "login/login.html"
	def get(self,request):
		form = self.form_class(None)
		return render(request, self.template_name,{'form':form})

	def post(self,request):
		form = self.form_class(request.POST)

		if form.is_valid():

			user =form.save(commit=False)
			first_name = form.cleaned_data['first_name']
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()



			user = authenticate(username=username,password=password)
			if user is not None:
				login(request, user)
				return redirect('/')

		return render(request, self.template_name, {'form':form})


def howitworks(request):
	return render(request, "login/howitworks.html")

def whytripogenic(request):
	return render(request, "login/whytripogenic.html")

def faqs(request):
	return render(request, "login/faqs.html")