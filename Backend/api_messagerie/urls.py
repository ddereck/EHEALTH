from django.urls import path
from .views import SendMessageView, InboxView, MessageDetailView

urlpatterns = [
    path('send-message/', SendMessageView.as_view(), name='send-message'),
    path('inbox/', InboxView.as_view(), name='inbox'),
    path('message/<int:message_id>/', MessageDetailView.as_view(), name='message-detail'),
]
