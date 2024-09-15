from django.test import TestCase
from django.shortcuts import reverse

class HomePageTest(TestCase):

    def test_status_code(self):
        res = self.client.get(reverse('home'))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'home_page.html')