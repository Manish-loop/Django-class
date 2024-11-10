from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    address = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(unique=True)
    website = models.URLField(null=True, blank=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    phone = models.PositiveBigIntegerField()
    date_joined = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # return self.name if self.name is not None else "New User"
        return self.name


class SchoolClass(models.Model):
    name = models.CharField(max_length=15)
    teacher=models.ManyToManyField(Teacher, blank=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        # return self.name if self.name is not None else "New User"
        return self.name

# from faker import Faker
# fake = Faker()
# for i in range(1,50):
#     Teacher.objects.create(
#         name=fake.name(),
#         address=fake.address(),
#         email = fake.email(),
#         website=fake.url(),
#         salary=fake.pydecimal(3,2),
#         phone=fake.msisdn(),
#         is_active = fake.boolean(),
#         date_joined= fake.date_time()
#     ) 