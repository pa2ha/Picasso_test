from rest_framework import serializers

from .models import File


class FileSerializer(serializers.ModelSerializer):
    uploaded_at = serializers.DateTimeField(format='%Y-%m-%d %I:%M:%S',
                                            read_only=True)

    class Meta:
        model = File
        fields = ['id', 'file', 'uploaded_at', 'processed']
        read_only_fields = ['uploaded_at', 'processed', 'id']
