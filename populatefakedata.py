import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proTwo.settings')

import django


django.setup()

from first_app.models import RealUser
from faker import Faker

fake = Faker()
for i in range(20):
    e = fake.email()
    a = fake.name().split()
    RealUser.objects.get_or_create(email_id=e, first_name=a[0], last_name=a[1])
