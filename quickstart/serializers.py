from django.contrib.auth.models import User, Group
from rest_framework import serializers

# class안에 Meta라는 이름의 class를 선언하는 문법(django만의 약속)
# python의 metaclass 문법과는 관련이 없음
# django에서 model 클래스 혹은 ModelForm 클래스에 대한 메타정보(설정, 즉 참조할 model, field 등)를 설정하는 일종의 선언
# class Meta는 클래스지만 인스턴스를 만드는 목적으로 사용되지않으며, 클래스 변수로서만 사용됨
# 따라서 아래와 같이 접근이 가능함 ex) PostForm.Meta

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
