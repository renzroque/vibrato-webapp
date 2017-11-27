import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','vibrato_project.settings')

import django
django.setup()

from vibrato_app.models import User
from faker import Faker

fakegen = Faker()

def generate_data(N):

	for entry in range(N):
		fake_firstname = fakegen.first_name()
		fake_lastname = fakegen.last_name()
		fake_email = fakegen.email()

		insert_data = User.objects.get_or_create(firstname=fake_firstname, lastname=fake_lastname, email=fake_email)[0]

if __name__ == '__main__':
	print('Generating Data...')
	generate_data(20)
	print('Done.')