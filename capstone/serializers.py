from itertools import product
from rest_framework import serializers
from .models import Kscholar,Interscholar,Berta,Favorscholar

class ScholarSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Kscholar
        fields = ('id','number','date','title','content','department',)

class InterestSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Interscholar
        fields = ('user','product_option')



class BertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Berta
        fields = '__all__'

class BertSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Berta
        fields = '__all__'

class FavorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorscholar
        fields = '__all__'