from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.get(user=user)
            return Response({
                "user": UserSerializer(user).data,
                "token": token.key
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)

            return Response({
                "user": UserSerializer(user).data,
                "token": token.key
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(APIView):

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

# follow user
class FollowerUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request,user_id):
        user_follow = get_object_or_404(User,id=user_id)
        
        if user_follow == request.user:
           return Response(
            {'factor':'you cannot follow yourself'},
            status = status.HTTP_404_BAD_REQUEST
        )
        request.user.following.add(user_follow)
        return Response(
            {'factor':f'you can follow {user_follow.username}'},
            status = status.HTTP_200_OK
        )
# unfollow user
class UnfollowUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self,request,user_id):
        user_unfollow = get_object_or_404(User,id=user_id)
        
        if user_unfollow == request.user:
           return Response(
            {'factor':f'you have unfollow {user_unfollow.username}'},
            status = status.HTTP_200_OK
        )