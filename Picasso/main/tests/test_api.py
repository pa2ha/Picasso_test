from django.test import TestCase
from main.models import File
from rest_framework import status
from rest_framework.test import APIClient


class UploadFileViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_upload_file_success(self):
        file_data = {'file': open('/app/Picasso/main/tests/test_files/testPNG.jpg', 'rb')}
        response = self.client.post('/api/upload/', file_data, format='multipart')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(File.objects.exists())

    def test_upload_file_no_file(self):
        response = self.client.post('/api/upload/')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['message'], 'Файл не найден в запросе')

    def test_upload_file_invalid_extension(self):
        file_data = {'file': open('/app/Picasso/main/tests/test_files/testDOCX.docx', 'rb')}
        response = self.client.post('/api/upload/', file_data, format='multipart')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['message'], 'Неподдерживаемый формат файла(jpg, png, txt, pdf)')


class ListFilesViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_list_files_success(self):
        File.objects.create(file='path/to/file.jpg')
        response = self.client.get('/api/files/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_list_files_empty(self):
        response = self.client.get('/api/files/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)
