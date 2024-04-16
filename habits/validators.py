
from rest_framework.exceptions import ValidationError


class ExclusiveFieldsValidator:
    def __init__(self, field1, field2, error_message):
        self.field1 = field1
        self.field2 = field2
        self.error_message = error_message

    def __call__(self, value):
        if value.get(self.field1) is not None and value.get(self.field2) is not None:
            raise ValidationError(self.error_message)


class MaxTimeToCompleteValidator:
    MAX_SECONDS = 120

    def __call__(self, value):
        if value.total_seconds() > self.MAX_SECONDS:
            raise ValidationError(f'Максимально время на выполнение должно быть не больше {self.MAX_SECONDS} секунд.')


class RelatedHabitValidator:

    def __call__(self, value):
        if value and not value.is_pleasant:
            raise ValidationError("Связанная привычка должна быть приятной.")


class PleasantHabitValidator:

    def __call__(self, value):
        if value.reward:
            raise ValidationError("Приятная привычка не может иметь вознаграждения.")
        if value.related_habits.exists():
            raise ValidationError("Приятная привычка не может иметь связанной привычки.")


class FrequencyValidator:
    MIN_FREQUENCY = 1
    MAX_FREQUENCY = 7

    def __call__(self, value):
        if value < self.MIN_FREQUENCY or value > self.MAX_FREQUENCY:
            raise ValidationError(
                f'Периодичность должна быть в диапазоне от {self.MIN_FREQUENCY} до {self.MAX_FREQUENCY} дней.'
            )
