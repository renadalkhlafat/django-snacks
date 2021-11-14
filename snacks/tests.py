from django.http import response
from django.test import SimpleTestCase
from django.urls import reverse
# Create your tests here.


class HomeTests(SimpleTestCase):
    def test_home_page_status_code(self):
        url = reverse("home")
        response=self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_home_page_template(self):
        url = reverse("home")
        response=self.client.get(url)

        self.assertTemplateUsed(response,"home.html")  

class AboutUsTests(SimpleTestCase):
    def test_about_us_page_status_code(self):
        url = reverse("about_us")
        response=self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_about_us_page_template(self):
        url = reverse("about_us")
        response=self.client.get(url)
        self.assertTemplateUsed(response,"about_us.html")  