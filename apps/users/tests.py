import json

from django.test import TestCase, Client
from rest_framework.test import APITestCase
from django.urls import reverse
from apps.users.models import User
from apps.users.api.api import user_api_view, user_detail_api_view

class UserTestClase(TestCase):

    def setUp(self):
        print('setUp actiti')
        User.objects.create(username ='testunit', name = 'usuari', email='testunit@corre.com', password= '1234')
    
    def test_user_info(self):
        print('testing usuarios informacion')
        reponse = User.objects.all()
        self.assertEqual(reponse.count(),1)
        user = User.objects.get(username = 'testunit')


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.list_url = reverse('usuario_api')
        self.detail_url = reverse('usuario_detail_api_view', args=['1'])
        self.user1 = User.objects.create(
                name = 1
        )


    def test_user_api_view_GET(self): 
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)

    def test_user_detail_GET(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)

    def test_user_detaill_POST_no_data(self):
        response = self.client.post(self.detail_url)
        self.assertEqual(response.status_code,405)


        




 
