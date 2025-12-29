from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def test_notification(request):
    # Stubbed response — later integrate Celery + Redis
    return Response({"message": "Notification sent (stub)"})
