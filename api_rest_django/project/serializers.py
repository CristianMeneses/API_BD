from rest_framework import serializers
from project.models import project
 
class projectSerializer(serializers.ModelSerializer):
    class Meta:
        model = project
        fields = ['project_id','description','name', 'start_date','end_dat', 'create_at', 'updated_at', 'project_id']
