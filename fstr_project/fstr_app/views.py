from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Pass
from .serializers import PassSerializer
from .database import DatabaseManager

class SubmitDataView(APIView):
    def post(self, request):
        db_manager = DatabaseManager()
        try:
            serializer = PassSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            pass_instance = db_manager.create_pass(serializer.validated_data)
            return Response({'status': 200, 'message': 'Отправлено успешно', 'id': pass_instance.id})
        except Exception as e:
            return Response({'status': 500, 'message': str(e)})
