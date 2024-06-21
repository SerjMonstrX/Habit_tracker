from django.db import models
from django.contrib.auth import get_user_model

from habits.validators import ExclusiveFieldsValidator, MaxTimeToCompleteValidator, RelatedHabitValidator, \
    FrequencyValidator, PleasantHabitValidator

User = get_user_model()
NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='автор привычки')
    name = models.CharField(max_length=100, verbose_name='название привычки')
    place = models.CharField(max_length=100, verbose_name='место')
    time = models.TimeField(verbose_name='время выполнения привычки')
    action = models.TextField(verbose_name='Действие для выполнения')
    is_pleasant = models.BooleanField(default=False, verbose_name='Признак приятности',
                                      validators=[PleasantHabitValidator()])
    related_habits = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='связанные привычки',
                                       validators=[RelatedHabitValidator()], **NULLABLE)
    frequency = models.PositiveSmallIntegerField(default=1, validators=[FrequencyValidator()],
                                                 verbose_name='периодичность')
    reward = models.CharField(max_length=100, verbose_name='вознаграждение', **NULLABLE)
    time_to_complete = models.TimeField(verbose_name='время на выполнение', validators=[MaxTimeToCompleteValidator()])
    is_public = models.BooleanField(default=False, verbose_name='признак публичности')
    last_reminded = models.DateTimeField(null=True, blank=True, verbose_name='Последнее напоминание')

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'

    def __str__(self):
        return self.name

    def clean(self):
        validator = ExclusiveFieldsValidator('reward', 'related_habits',
                                             'Нельзя указывать связанную приятную привычку и вознаграждение вместе')
        validator({'reward': self.reward, 'related_habits': self.related_habits})
