from rest_framework_json_api import serializers
from ..models import Case


class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = "__all__"
