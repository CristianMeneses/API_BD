from rest_framework import serializers
from user.models import user
 
class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ['user_id','username','password', 'profesional_headline', 'create_at', 'updated_at', 'project_id']
