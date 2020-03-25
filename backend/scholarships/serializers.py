from rest_framework import serializers
from .models import Scholarship


class ScholarshipSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'url', 'amount', 'amount_descriptor', 'deadline',)
        model = Scholarship
