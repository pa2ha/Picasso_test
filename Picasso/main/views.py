import os

from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

from .models import File
from .serializers import FileSerializer
from .tasks import process_file


class UploadFileViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    def create(self, request, *args, **kwargs):
        file = request.data.get('file')
        if file is None:
            return Response({"message": "Файл не найден в запросе"},
                            status=status.HTTP_400_BAD_REQUEST)

        # Проверяем расширение файла
        file_name, file_extension = os.path.splitext(file.name)
        allowed_extensions = ['.jpg', '.png', '.txt', '.pdf']
        if file_extension.lower() not in allowed_extensions:
            return Response({"message": "Неподдерживаемый формат"
                             " файла(jpg, png, txt, pdf)"},
                            status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            file_obj = serializer.save()
            process_file.delay(file_obj.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"message": "Ожидается формат {'file': ваш_файл}",
                        "errors": serializer.errors},
                        status=status.HTTP_400_BAD_REQUEST)


class ListFilesViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
