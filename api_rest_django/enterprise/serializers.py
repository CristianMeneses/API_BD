from rest_framework import serializers
from enterprise.models import enterprise
 
class enterpriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = enterprise
        fields = ['enterprise_id','name', 'create_at', 'updated_at']
