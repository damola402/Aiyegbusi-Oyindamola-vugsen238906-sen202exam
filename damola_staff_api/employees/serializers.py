from rest_framework import serializers
from .models import Manager, Intern

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'
        extra_kwargs = {'has_company_card': {'read_only': True}}

class InternSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intern
        fields = '__all__'