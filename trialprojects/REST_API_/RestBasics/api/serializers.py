from rest_framework import  serializers
from .models import Article

""" class ArticleSerializers(serializers.Serializer):
    # specify fields copy from models
    title =   serializers.CharField(max_length=100)
    author= serializers.CharField(max_length=100)
    email =  serializers.CharField(max_length=100)
    date=  serializers.DateTimeField() # removed one argument

    def create(self,validated_data):
        return Article.objects.create(validated_data)

    def update(self,instance,validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.email = validated_data.get('email', instance.email)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance """                      #WE ARE REPEATING A LOT OF INFOMATION
# DJANGO PROVIDE AN EASY WAY

class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id','author','title','email',]
