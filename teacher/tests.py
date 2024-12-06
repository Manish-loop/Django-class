# from django.test import TestCase
# from .models import *
# from faker import Faker
# fake = Faker() 
# # Create your tests here.


# class FirstTestCase(TestCase):
    
#     def setUp(self):
#         print('setup called')
    
#     # def test_equal(self):
#     #     self.assertEqual(1, 1)
    
    
#     def test_teacher(self):
#         names = ['Anish', 'Ram']
        
#         for name in names:
#             obj = Teacher.objects.create(
#                 name = name
#             )
            
#             self.assertEquals(name, obj.name)
        
#         objs = Teacher.objects.all()
        
#         self.assertEqual(objs.count(),2)