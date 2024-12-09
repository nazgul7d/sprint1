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
    
    def get(self, request, id=None, email=None):
        if id:
            pass_instance = get_object_or_404(Pass, pk=id)
            serializer = PassSerializer(pass_instance)
            return Response(serializer.data)
        elif email:
            passes = Pass.objects.filter(user__email=email)
            serializer = PassSerializer(passes, many=True)
            return Response(serializer.data)
        else:
            return Response({'error': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        pass_instance = get_object_or_404(Pass, pk=id)
        serializer = PassSerializer(data=request.data, instance=pass_instance, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'state': 1, 'message': 'Запись успешно обновлена'})
        return Response({'state': 0, 'message': serializer.errors})
