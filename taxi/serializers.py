from rest_framework import serializers

from .models import Report


class ReportSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Report
        fields = [(field.name) for field in Report._meta.fields]
