from rest_framework import serializers

from uric_api.apps.mtask.models import CmdTemplate, CmdTemplateCategory


class CmdTemplateModelSerialzer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.name", read_only=True)

    class Meta:
        model = CmdTemplate
        fields = ["id", "name", "cmd", "description", "category_name", "category"]


class CmdTemplateCategoryModelSerialzer(serializers.ModelSerializer):
    class Meta:
        model = CmdTemplateCategory
        fields = "__all__"
