from rest_framework import serializers
from habits.models import Habit
from habits.validators import (
    ExclusiveFieldsValidator, MaxTimeToCompleteValidator,
    RelatedHabitValidator, PleasantHabitValidator, FrequencyValidator
)


class HabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = '__all__'
        read_only_fields = ['creator']

    def validate(self, data):
        # Применение валидатора ExclusiveFieldsValidator
        exclusive_validator = ExclusiveFieldsValidator('reward', 'related_habits')
        exclusive_validator(data)

        # Применение валидатора MaxTimeToCompleteValidator
        max_time_validator = MaxTimeToCompleteValidator()
        max_time_validator(data.get('time_to_complete'))

        # Применение валидатора RelatedHabitValidator
        related_habit_validator = RelatedHabitValidator()
        related_habit_validator(data)

        # Применение валидатора PleasantHabitValidator
        pleasant_habit_validator = PleasantHabitValidator()
        pleasant_habit_validator(data)

        # Применение валидатора FrequencyValidator
        frequency_validator = FrequencyValidator()
        frequency_validator(data.get('frequency'))

        return data
