from django.shortcuts import render
from django.http import HttpResponse
from vibrato_app.models import User

# Create your views here.

def index(request):
	users_list = User.objects.all()
	users_dict = { "users": users_list }

	return render(request, 'index.html', context=users_dict)


