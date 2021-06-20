from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from .models import Sky

# Create your tests here.


class SkyModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='Adrian.Smith' ,password='pass')
        test_user.save()

        test_sky = Sky.objects.create(
            name = 'Burj khalifa',
            discription = '828m high and considerd the highst in the world',
            architect = test_user
        )
        test_sky.save()

    def test_blog_content(self):

        sky = Sky.objects.get(id=1)
        self.assertEqual(sky.name, 'Burj khalifa')
        self.assertEqual(str(sky.architect), 'Adrian.Smith')
        self.assertEqual(sky.discription, '828m high and considerd the highst in the world')


class APITest(APITestCase):
    
    def test_list(self):
        response = self.client.get(reverse('sky_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail(self):

        test_user = get_user_model().objects.create_user(username='Adrian.Smith',password='pass')
        test_user.save()

        test_post = Sky.objects.create(
            name = 'Burj khalifa',
            architect = test_user,
            discription = '828m high and considerd the highst in the world'
        )
        test_post.save()

        response = self.client.get(reverse('sky_detail', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            'id':1,
            'name': test_post.name,
            'discription': test_post.discription,
            'architect': test_user.id,
        })


    def test_create(self):
        test_user = get_user_model().objects.create_user(username='Adrian.Smith',password='pass')
        test_user.save()

        url = reverse('sky_list')
        data = {
            "name":"Burj Al Arab",
            "discription":"shroter that Burj khalifa",
            "architect":test_user.id,
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED, test_user.id)

        self.assertEqual(Sky.objects.count(), 1)
        self.assertEqual(Sky.objects.get().name, data['name'])

    def test_update(self):
        test_user = get_user_model().objects.create_user(username='Adrian.Smith',password='pass')
        test_user.save()

        test_post = Sky.objects.create(
            architect = test_user,
            name = 'Burj khalifa',
            discription = '828m high and considerd the highst in the world'
        )

        test_post.save()

        url = reverse('sky_detail',args=[test_post.id])
        data = {
            "name":"Burj Al Arab",
            "architect":test_post.architect.id,
            "discription":test_post.discription,
        }

        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK, url)

        self.assertEqual(Sky.objects.count(), test_post.id)
        self.assertEqual(Sky.objects.get().name, data['name'])


    def test_delete(self):
        """Test the api can delete a Sky."""

        test_user = get_user_model().objects.create_user(username='Adrian.Smith',password='pass')
        test_user.save()

        test_post = Sky.objects.create(
            name = 'Burj khalifa',
            architect = test_user,
            discription = '828m high and considerd the highst in the world'
        )

        test_post.save()

        sky = Sky.objects.get()

        url = reverse('sky_detail', kwargs={'pk': sky.id})


        response = self.client.delete(url)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT, url)
