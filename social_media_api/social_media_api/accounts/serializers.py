from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    class Meta:
        model = User
        fields = ['id','username','email','password','bio','profile_pic']
        
    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data.get['email'],
            password = validated_data.get['password'],
            bio = validated_data.get['bio'])
        
        Token.objects.create(user = user)
        return user
    
    
class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only = True)
    
    def validate(self, data):
        user = authenticate(
            username = data['username'],
            password = data['password']
        )
        if not user:
            raise serializers.ValidationError('Eneter the correct details')
        data['user'] = user
        return user
    
class UserSerializer(serializers.ModelSerializer):
    followers_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id','username','email','password','bio','profile_picture','followers_count','following_count']
        
        def get_followers_count(self,obj):
            return obj.followers_count()
        
        def get_following_count(self,obj):
            return obj.following_count()