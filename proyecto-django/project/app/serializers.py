from rest_framework import serializers
from .models import Persona, Barrio, LocalComida, LocalRepuesto


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'

class BarrioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barrio
        fields = '__all__'

class LocalComidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalComida
        fields = '__all__'

class LocalRepuestoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalRepuesto
        fields = '__all__'
