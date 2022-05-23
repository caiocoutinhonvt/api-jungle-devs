from rest_framework import serializers
from jungledevs import models
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = '__all__'


class ArticlesSerializer(serializers.ModelSerializer):                             #Articles 
    author = AuthorSerializer(many=False, read_only=True)
    author_id = serializers.UUIDField(write_only=True)

    class Meta:
        model = models.Articles
        fields = ["id", "author_id", "author", "category",
                  "title", "summary", "firstParagraph", "body"]


class NotAuthenticatedArticlesSerializer(serializers.ModelSerializer):                    #Anonymous User Articles
    author = AuthorSerializer(many=False, read_only=True)
    author_id = serializers.UUIDField(write_only=True)

    class Meta:
        model = models.Articles
        fields = ["id", "author_id", "author", "category",
                  "title", "summary", "firstParagraph"]


class RegisterSerializer(serializers.ModelSerializer):                                #Register User
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2',
                  'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
