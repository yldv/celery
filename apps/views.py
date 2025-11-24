from rest_framework import generics, status
from rest_framework.response import Response
from .models import EmailMessage
from .serializer import EmailMessageSerializer

class EmailMessageView(generics.CreateAPIView):
    queryset = EmailMessage.objects.all()
    serializer_class = EmailMessageSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({"message": "email kiritildi"}, status=status.HTTP_201_CREATED)