from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from api.models import Profile
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


# Custom Token Claim for adding username to JWT

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username
        return token
    


# Register New User Serializer 

class UserRegisterSerializer(serializers.ModelSerializer):
    # Unique User Validation
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    cf_password = serializers.CharField(style={'input_type':'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username','email','password','cf_password']
        extra_kwargs = {'password':{'write_only':True}}
    
    def validate(self, attrs):
        password = attrs.get('password')
        cfpassword = attrs.get('cf_password')

        # Password & confirm password matching
        if password != cfpassword:
            raise serializers.ValidationError("Password and Confirm Password doesn't match")
        
        # Validate Email
        try:
            validate_email(attrs.get('email'))
        except ValidationError as err:
            raise serializers.ValidationError({'error':err.messages})
        return attrs


    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )

        # Validate Password
        try:
            password = validated_data['password']
            validate_password(password=password,user=user)
        except ValidationError as err:
            user.delete()
            raise serializers.ValidationError({'error':err.messages})

        # Register the user if everything is done correct
        user.set_password(validated_data['password'])
        user.save()
        return user
    


# Login User Serialization

class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100)
    class Meta:
        model = User
        fields = ['username','password']



# Serialization For User Profile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['first_name','last_name','about','phone','country']
        read_only_fields = ['user']

    def create(self, validated_data):
        user = self.context['request'].user
        return Profile.objects.create(user=user, **validated_data)