import json
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Author, Articles
from django.urls import reverse
from rest_framework.test import force_authenticate





class TestCase(APITestCase):

    def setUp(self):
        self.authenticate()

        Author.objects.create(name="Louis")
        self.response = self.client.get('/api/admin/authors', follow=True)
        self.author_id = self.response.data[0]["id"]
        
        self.author_detail = self.client.get('/api/admin/authors/', args=[self.author_id], follow=True)

        

    def test_registration(self):
        
        data = {'username': 'testcase2', 
                'password':'strongpassword123', 
                'password2':'strongpassword123', 
                'email': 'teste2@gmail.com', 
                'first_name': 'test', 
                'last_name': 'case'}

        # import ipdb; ipdb.set_trace()
        response = self.client.post(reverse('sign_up'), data)
        self.assertEqual(response.status_code, 201)


    def test_registration_invalid_password(self):
        
        data = {'username': 'testcase2', 
                'password':'strongpassword123', 
                'password2':'strongpassword142', 
                'email': 'teste2@gmail.com', 
                'first_name': 'test', 
                'last_name': 'case'}

        # import ipdb; ipdb.set_trace()
        response = self.client.post(reverse('sign_up'), data)
        self.assertEqual(response.status_code, 400)


    def authenticate(self):
        data = {'username': 'testcase', 
                'password':'strongpassword123', 
                'password2':'strongpassword123', 
                'email': 'teste@gmail.com', 
                'first_name': 'test', 
                'last_name': 'case'
                }

        self.client.post("/api/sign-up/", data)

        data2 = {'username': 'testcase',
                'password':'strongpassword123'
                }

        response = self.client.post("/api/login/", data2 )
        
        self.login_response = self.client.post('/api/login/', data2)
        self.token = self.login_response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)

    
    def test_articles_user_list(self):
        response = self.client.get('/api/articles', follow=True)
        self.assertEqual(response.status_code, 200)


    def test_articles_admin_list(self):
        self.authenticate()
        response = self.client.get('/api/admin/articles/', follow=True)
        self.assertEqual(response.status_code, 200)



    def test_articles_admin_list(self):
        self.client.logout()
        response = self.client.get('/api/articles/', follow=True)
        self.assertEqual(response.status_code, 200)


    def test_create_author(self):
        self.authenticate()

        data = {
            "name":"Luiz"     
        }
        response = self.client.post('/api/admin/authors/', data, follow=True)
        self.assertEqual(response.status_code, 201)


    def test_create_articles(self):
      
        self.authenticate() 
    
        data = {'author_id': Author.objects.first().id ,
                'category': 'Python',
                'title': 'Api',
                'summary': 'Jungle Devs Challenge',
                'firstParagraph': 'Ok',
                'body': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed posuere sagittis gravida. Proin sodales urna ipsum, dapibus faucibus diam elementum at. Aliquam faucibus sapien at eleifend malesuada. Pellentesque non sem tristique, varius nulla at, varius nunc.'
                }
        response = self.client.post('/api/admin/articles/', data, follow=True)
        self.assertEqual(response.status_code, 201)



    def test_create_articles_without_50_digits_body(self):
      
        self.authenticate() 
    
        data = {'author_id': Author.objects.first().id ,
                'category': 'Python',
                'title': 'Api',
                'summary': 'Jungle Devs Challenge',
                'firstParagraph': 'Ok',
                'body': 'body without 50 digits'
                }
        response = self.client.post('/api/admin/articles/', data, follow=True)
        self.assertEqual(response.status_code, 400)



