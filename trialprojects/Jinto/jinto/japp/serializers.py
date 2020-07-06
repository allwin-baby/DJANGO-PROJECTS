
from rest_framework import  serializers
from .models import Jinto



class JintoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Jinto
        fields = ['link',]