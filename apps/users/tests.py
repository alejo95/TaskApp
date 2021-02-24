from django.test import TestCase
from apps.users.models import User

class UserTestClase(TestCase):

    def setUp(self):
        print('setUp actiti')
        User.objects.create(username ='testunit', name = 'usuari', email='testunit@corre.com', password= '1234')
    
    def test_user_info(self):
        print('testing usuarios informacion')
        reponse = User.objects.all()
        self.assertEqual(reponse.count(),1)
        user1 = User.objects.get(username = 'testunit')
        
