from django.test import Client, TestCase
from django.urls import reverse
from unittest.mock import patch
from .models import Url
from .views import get_short_url


class UrlShortenerTest(TestCase):
    def setUp(self):
        self.client = Client()

        #for test_shorten_url_existing
        self.long_url1 = 'https://www.example.com/'
        self.short_url1 = '7'
        self.url1 = Url.objects.create(long_url=self.long_url1, short_url=self.short_url1)

        #for test_shorten_url_new
        self.long_url2 = 'https://www.example123.com/'

        self.long_url3 = 'https://www.example12345.com/'
        self.short_url3 = '9'
        self.url3 = Url.objects.create(long_url=self.long_url3, short_url=self.short_url3)

        self.long_url4 = 'https://www.google.com/'
        self.short_url4 = 'a'
        self.url4 = Url.objects.create(long_url=self.long_url4, short_url=self.short_url4)

    def test_shorten_url_get(self):
        # Test GET request to shorten_url view
        response = self.client.get(reverse('shorten'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shorten.html')

    def test_shorten_url_existing(self):
        # Test if the short url exists in the database
        response = self.client.post(reverse('shorten'), {'long_url': self.long_url1})
        self.assertContains(response, '7')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shorten.html')

    def test_shorten_url_new(self):
        # Test if a new short url is created and saved to the database
        response = self.client.post(reverse('shorten'), {'long_url': self.long_url2})
        self.assertEqual(response.status_code, 200)
        self.assertRegex(response.content.decode(), r'[0-9a-zA-Z]+')
        self.assertTemplateUsed(response, 'shorten.html')

        # Check if the url is saved to the database
        urls = Url.objects.filter(long_url=self.long_url2)
        self.assertEqual(urls.count(), 1)
        self.assertRegex(urls[0].short_url, r'[0-9a-zA-Z]+')
        self.assertTemplateUsed(response, 'shorten.html')

        #check if the url in db is the same to the response from shorten_url in views
        self.assertContains(response, urls[0].short_url)

    @patch('url_shortener.views.Url.objects.all')
    def test_get_short_url(self, mock_objects_all):

        #when there is no data, max_id = None, num = 1
        mock_objects_all.return_value.aggregate.return_value = {'max_id': None}
        short_url = get_short_url()
        self.assertEqual(short_url, '0')

        #max_id = i, num = num+1
        mock_objects_all.return_value.aggregate.return_value = {'max_id': 2}
        short_url = get_short_url()
        self.assertEqual(short_url, '2')

        mock_objects_all.return_value.aggregate.return_value = {'max_id': 9}
        short_url = get_short_url()
        self.assertEqual(short_url, '9')

        mock_objects_all.return_value.aggregate.return_value = {'max_id': 35}
        short_url = get_short_url()
        self.assertEqual(short_url, 'z')

        mock_objects_all.return_value.aggregate.return_value = {'max_id': 35}
        short_url = get_short_url()
        self.assertEqual(short_url, 'z')

        mock_objects_all.return_value.aggregate.return_value = {'max_id': 123}
        short_url = get_short_url()
        self.assertEqual(short_url, '1Z')

        mock_objects_all.return_value.aggregate.return_value = {'max_id': 12345}
        short_url = get_short_url()
        self.assertEqual(short_url, '3d7')
        

    
    def test_redirect_url(self):
        
        response = self.client.get(reverse('redirect', args=[self.short_url3]))
        self.assertRedirects(response, self.long_url3, fetch_redirect_response=False)

        
        response = self.client.get(reverse('redirect', args=[self.short_url4]), follow=True)
        self.assertEqual(response.redirect_chain[0][0], self.long_url4)


        '''
        The test client is not capable of retrieving web pages that are not powered by your Django project. 
        If you need to retrieve other web pages, use a Python standard library module such as urllib.
        '''
        
        invalid_short_url = "www.not_in_db"
        response = self.client.get(reverse('redirect', args=[invalid_short_url]))
        self.assertEqual(response.status_code, 404)

        


       

        

 