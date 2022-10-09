from django.shortcuts import render, redirect, HttpResponse
from .forms import RegForm, LoginForm
from .models import registration_details, login_details
from django.contrib import messages, auth

# Create your views here.

def indexView(request):
	if request.method == 'GET':
		form = RegForm()
	else:
		form = RegForm(request.POST)
		if form.is_valid():
			Registration_details = registration_details()
			name = form.cleaned_data['Name']
			email = form.cleaned_data['your_email']
			passwd = form.cleaned_data['password']
			phone = form.cleaned_data['Phone']
			try:
				Registration_details.Name=name
				Registration_details.your_email=email
				Registration_details.password=passwd
				Registration_details.Phone=phone
				Registration_details.save()
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect('success')
	args = {'form':form}
	return render(request, 'base.html', args)

def loginView(request):
	if request.method == 'GET':
		form = LoginForm()
	else:
		form = LoginForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data['your_email']
			passwd = form.cleaned_data['password']
			#print(email)
			#print(passwd)
			test = registration_details.objects.all()
			for t in test:
				email1 = t.your_email
				passwd1 = t.password
				print(email1)
				print(passwd1)
				if email == email1 and passwd == passwd1:
					return redirect('logged-in') 
				else:
					messages.info(request, 'Invalid Credentials')
					#return render(r 'login.html')
	args = {'form':form}
	return render(request, 'login.html', args)

def SuccessView(request):
	return render(request, 'success.html')

def loggedinView(request):
	return render(request, 'logged.html')

def logout(request):
    auth.logout(request)
    return render(request,'logout.html')
    
