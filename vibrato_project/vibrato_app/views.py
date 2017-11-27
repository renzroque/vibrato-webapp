from django.shortcuts import render
from django.http import HttpResponse
from vibrato_app.models import User

# Create your views here.

def index(request):
	users_list = User.objects.all()
	search = request.GET.get('q')

	if search:
		users_list = users_list.filter(firstname__icontains=search)
	
	users_dict = { "users": users_list }

	return render(request, 'index.html', context=users_dict)


