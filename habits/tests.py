from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import Habit
from django.urls import reverse

User = get_user_model()


class HabitTestCase(APITestCase):
    """
    Тесты для операций CRUD на модели Habit с использованием DRF API.
    """

    def setUp(self) -> None:
        """
        Подготовка тестовых данных и аутентификация клиента.
        """
        self.user = User.objects.create(email='testuser@example.com', password='testpass123412')
        self.client.force_authenticate(user=self.user)
        self.habit_data_1 = {
            'name': 'Test Habit',
            'place': 'Дома',
            'time': '12:00:00',
            'action': 'Почитать книгу',
            'is_pleasant': False,
            'frequency': 1,
            'reward': 'Скушать конфету',
            'time_to_complete': 30,
            'is_public': False,
        }
        self.habit_data_2 = {
            'name': 'Test Habit 2',
            'place': 'Улица',
            'time': '17:00:00',
            'action': 'Погулять',
            'is_pleasant': True,
            'frequency': 1,
            'reward': None,
            'time_to_complete': 30,
            'is_public': True,
        }

    def test_create_habit_1(self):
        """
        Тест на создание привычки без связанных привычек.
        """
        url = reverse('habits:habit_create')
        self.habit_data_1['creator'] = self.user.id
        response = self.client.post(url, self.habit_data_1, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.count(), 1)
        self.assertEqual(Habit.objects.get().name, 'Test Habit')

    def test_create_habit_with_related_habit(self):
        """
        Тест на создание привычки с связанной привычкой.
        """
        habit_data_2 = {
            'name': 'Test Habit 2',
            'place': 'Офис',
            'time': '15:00:00',
            'action': 'Прогуляться',
            'is_pleasant': True,
            'frequency': 2,
            'reward': None,
            'time_to_complete': 20,
            'is_public': True,
        }
        url = reverse('habits:habit_create')
        response = self.client.post(url, habit_data_2, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        habit_2 = Habit.objects.get(id= 2)
        habit_data_3 = {
            'name': 'Test Habit 3',
            'place': 'Спортзал',
            'time': '18:00:00',
            'action': 'Тренировка',
            'is_pleasant': False,
            'frequency': 3,
            'reward': None,
            'time_to_complete': 45,
            'is_public': True,
            'related_habits': habit_2.id,
        }
        response = self.client.post(url, habit_data_3, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.count(), 2)
        self.assertEqual(Habit.objects.get(name='Test Habit 3').related_habits, habit_2)

    def test_list_habits(self):
        """
        Тест на получение списка привычек.
        """
        Habit.objects.create(creator=self.user, **self.habit_data_1)
        url = reverse('habits:habit_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_retrieve_habit(self):
        """
        Тест на получение конкретной привычки по её ID.
        """
        habit = Habit.objects.create(creator=self.user, **self.habit_data_1)
        url = reverse('habits:habit_retrieve', args=[habit.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Habit')

    def test_update_habit(self):
        """
        Тест на обновление привычки.
        """
        habit = Habit.objects.create(creator=self.user, **self.habit_data_1)
        update_data = {
            'name': 'Updated Habit',
            'place': 'Улица',
            'time': '15:00:00',
            'action': 'Прогуляться',
            'is_pleasant': True,
            'frequency': 2,
            'reward': None,
            'time_to_complete': 25,
            'is_public': True,
            'creator': self.user.id
        }
        url = reverse('habits:habit_update', args=[habit.id])
        response = self.client.put(url, update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        habit.refresh_from_db()
        self.assertEqual(habit.name, 'Updated Habit')

    def test_delete_habit(self):
        """
        Тест на удаление привычки.
        """
        habit = Habit.objects.create(creator=self.user, **self.habit_data_1)
        url = reverse('habits:habit_delete', args=[habit.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.count(), 0)
