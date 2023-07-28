from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MessageSerializer

class SendMessageView(APIView):
    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(sender=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class InboxView(APIView):
    def get(self, request):
        messages = Message.objects.filter(recipient=request.user)
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

class MessageDetailView(APIView):
    def get(self, request, message_id):
        message = Message.objects.get(id=message_id, recipient=request.user)
        serializer = MessageSerializer(message)
        return Response(serializer.data)

    def put(self, request, message_id):
        message = Message.objects.get(id=message_id, recipient=request.user)
        serializer = MessageSerializer(message, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
