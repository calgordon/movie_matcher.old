from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, UserSerializerWithToken


@api_view(['GET'])
def current_user(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


class UserList(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['POST'])
# def send_friend_request(request):
#     from_user = request.user
#     to_user = Profile.objects.get(id=user_id)
#     friend_request, created = FriendRequest.objects.get_or_create(from_user=from_user, to_user=to_user)
#     if created:
#         return Response('Friend request sent!')
#     else:
#         return Response('You already sent a request!')
#
#
# @api_view
# def accept_friend_request(request, request_id):
#     friend_request = FriendRequest.objects.get(id=request_id)
#     if friend_request.to.user == request.user:
#         friend_request.to.user.friends.add(friend_request.from_user)
#         friend_request.from_user.friends.add(friend_request.to_user)
#         friend_request.delete()
#         return HttpResponse(friend_request.to_user.username + " has accepted your friend request!")
#     else:
#         return
