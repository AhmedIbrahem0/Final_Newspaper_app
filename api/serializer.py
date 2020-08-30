from rest_framework import serializers
from users.models import CustomUser 
from articles.models import Article
#? User Serializer
class UserSerizlezier(serializers.ModelSerializer):
    class Meta:
        model =CustomUser
        fields =('username' ,'email' ,'age' ,'is_staff')

#? Articel Serializer
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields=("title","body","date")