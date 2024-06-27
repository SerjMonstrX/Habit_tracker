from rest_framework.exceptions import ValidationError

from habits.models import Habit


class ExclusiveFieldsValidator:
    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2
        self.error_message = 'Нельзя указывать связанную приятную привычку и вознаграждение вместе'

    def __call__(self, value):
        if value.get(self.field1) is not None and value.get(self.field2) is not None:
            raise ValidationError(self.error_message)


class MaxTimeToCompleteValidator:
    MAX_SECONDS = 120

    def __call__(self, value):
        if value > self.MAX_SECONDS:
            raise ValidationError(f'Максимально время на выполнение должно быть не больше {self.MAX_SECONDS} секунд.')


class RelatedHabitValidator:

    def __call__(self, value):
        related_habit = value.get('related_habits')
        if related_habit:
            try:
                related_habit = Habit.objects.get(id=related_habit.id)
                if not related_habit.is_pleasant:
                    raise ValidationError("Связанная привычка должна быть приятной.")
            except Habit.DoesNotExist:
                raise ValidationError("Связанная привычка не существует.")


class PleasantHabitValidator:

    def __call__(self, value):
        if value.get('is_pleasant') and value.get('reward'):
            raise ValidationError("Приятная привычка не может иметь вознаграждения.")
        if value.get('is_pleasant') and value.get('related_habits'):
            raise ValidationError("Приятная привычка не может иметь связанной привычки.")


class FrequencyValidator:
    MIN_FREQUENCY = 1
    MAX_FREQUENCY = 7

    def __call__(self, value):
        if value < self.MIN_FREQUENCY or value > self.MAX_FREQUENCY:
            raise ValidationError(
                f'Периодичность должна быть в диапазоне от {self.MIN_FREQUENCY} до {self.MAX_FREQUENCY} дней.'
            )
