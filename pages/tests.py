from django.test import SimpleTestCase , TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
class Home_page(SimpleTestCase):
    def test_home_page(self):
        resp = self.client.get(reverse("home"))
        self.assertEqual(resp.status_code,200)
        self.assertTemplateUsed(resp ,"home.html")
class Signuppage(TestCase):
    username="testuser"
    email="test@gmail.com"
    def test_sign_up_status(self):
        resp =self.client.get("/users/signup/")
        self.assertEqual(resp.status_code,200)
    def test_sign_up_page(self):
        resp =self.client.get(reverse("signup"))
        self.assertEqual(resp.status_code,200)
        self.assertTemplateUsed(resp,"signup.html")
    def test_sign_form(self):
        new_user = get_user_model().objects.create_user(self.username,self.email)
        self.assertEqual(get_user_model().objects.all().count(),1)
        self.assertEqual(get_user_model().objects.all()[0].username,self.username)
        self.assertEqual(get_user_model().objects.all()[0].email,self.email)
        