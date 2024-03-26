from datetime import date

from rest_framework import serializers


class StatisticsSerializer(serializers.Serializer):
    date_from = serializers.DateField(default=date(year=2020, month=1, day=1), input_formats=['%Y-%m-%d'])
    date_to = serializers.DateField(default=date.today(), input_formats=['%Y-%m-%d'])

    def validate(self, data):
        """
        Check that date_from is before date_to.
        """
        if data['date_from'] > data['date_to']:
            raise serializers.ValidationError('date_from must be before date_to')

        return data
