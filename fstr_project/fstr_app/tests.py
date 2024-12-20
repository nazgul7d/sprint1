from django.test import TestCase
from .models import CustomUser, Pass

from django.urls import reverse
from rest_framework.test import APITestCase
from unittest.mock import patch, MagicMock

from .models import Pass
from .serializers import PassSerializer
from .views import SubmitDataView

class TestPassModel(TestCase):

    def setUp(self):
        # Create a test user
        self.user = CustomUser.objects.create_user(
            username='testuser', 
            password='testpassword', 
            name='Test User', 
            city='Test City'
        )

    def test_pass_creation(self):
        # Create a Pass instance
        pass_obj = Pass.objects.create(
            beauty_title='Beautiful Pass', 
            title='Test Pass', 
            other_titles='Other Titles', 
            connect='Connect', 
            latitude=12.345, 
            longitude=54.321, 
            height=1000, 
            winter_level='Easy', 
            summer_level='Moderate', 
            autumn_level='Difficult', 
            spring_level='Easy', 
            user=self.user, 
            images=[]  # Example empty list for images
        )

        # Assertions
        self.assertEqual(pass_obj.beauty_title, 'Beautiful Pass')
        self.assertEqual(pass_obj.title, 'Test Pass')
        self.assertEqual(pass_obj.status, 'new') 
        self.assertEqual(pass_obj.user, self.user)
        self.assertIsNotNone(pass_obj.created_at)

    def test_status_choices(self):
        # Check if the status choices are defined correctly
        self.assertEqual(Pass.STATUS_CHOICES, [
            ('new', 'Новый'),
            ('pending', 'На модерации'),
            ('accepted', 'Принят'),
            ('rejected', 'Отклонен'),
        ])

    def test_str_method(self):
        pass_obj = Pass.objects.create(
            title='Test Pass', 
            user=self.user
        )
        self.assertEqual(str(pass_obj), 'Test Pass')

class TestSubmitDataView(APITestCase):

    def setUp(self):
        self.user = self.client.force_authenticate(username='testuser', password='testpassword')
        self.pass_data = {
            "beauty_title": "Beautiful Pass",
            "title": "Test Pass",
            "other_titles": "Other Titles",
            "connect": "Connect",
            "latitude": 12.345,
            "longitude": 54.321,
            "height": 1000,
            "winter_level": "Easy",
            "summer_level": "Moderate",
            "autumn_level": "Difficult",
            "spring_level": "Easy",
        }

    def test_post_valid_data(self):
        url = reverse('submit-data')
        response = self.client.post(url, self.pass_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_CREATED)
        self.assertEqual(response.data['message'], 'Отправлено успешно')
        self.assertIn('id', response.data)

        # Check if Pass object is created
        pass_obj = Pass.objects.get(pk=response.data['id'])
        self.assertEqual(pass_obj.beauty_title, self.pass_data['beauty_title'])

    @patch.object(SubmitDataView, 'get_serializer_class')
    def test_post_invalid_data(self, mock_get_serializer_class):
        mock_serializer = MagicMock()
        mock_serializer.is_valid.raise_exception.side_effect = serializers.ValidationError('Invalid data')
        mock_get_serializer_class.return_value = mock_serializer
        url = reverse('submit-data')
        response = self.client.post(url, self.pass_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)

    @patch.object(SubmitDataView, 'get_object')
    def test_get_by_id(self, mock_get_object):
        mock_pass = MagicMock(spec=Pass)
        mock_get_object.return_value = mock_pass
        url = reverse('submit-data', kwargs={'id': 1})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_by_nonexistent_id(self):
        url = reverse('submit-data', kwargs={'id': 100})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_by_email(self):
        # Create a Pass object with the user
        pass_obj = Pass.objects.create(user=self.user, **self.pass_data)
        url = reverse('submit-data', kwargs={'email': self.user.email})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], pass_obj.title)

    def test_get_by_invalid_request(self):
        url = reverse('submit-data')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)

    @patch.object(SubmitDataView, 'get_object')
    def test_patch_valid_data(self, mock_get_object):
        mock_pass = MagicMock(spec=Pass)
        mock_get_object.return_value = mock_pass
        update_data = {'beauty_title': 'Updated Pass'} 
        url = reverse('submit-data', kwargs={'id': self.pass_obj.id})
        response = self.client.patch(url, update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['state'], 1)
        self.assertEqual(response.data['message'], 'Запись успешно обновлена')

    @patch.object(SubmitDataView, 'get_object')
    def test_patch_invalid_data(self, mock_get_object):
        mock_pass = MagicMock(spec=Pass)
        mock_get_object.return_value = mock_pass
        update_data = {'invalid_field': 'invalid_value'} 
        url = reverse('submit-data', kwargs={'id': self.pass_obj.id})
        response = self.client.patch(url, update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['state'], 0)
        self.assertIn('invalid_field', response.data['message'])