# from django.shortcuts import render
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from api.jsonrender import UserRenderer
from api.serializers import UserRegisterSerializer,UserLoginSerializer,UserProfileSerializer
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from django.contrib.auth import authenticate,login,logout
from rest_framework.permissions import IsAuthenticated
# from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import OutstandingToken,BlacklistedToken
from rest_framework_simplejwt.utils import aware_utcnow
from api.models import Profile


# Create your views here.


# Generate JWT tokens manually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    refresh['username'] = user.username

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class UserRegisterView(APIView):
    renderer_classes = [UserRenderer]
    
    def post(self, request, format=None):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response({'token':token, 'msg':'Registration Successful'}, status=status.HTTP_201_CREATED)
        return Response({'error':'User not registered'}, status=status.HTTP_401_UNAUTHORIZED)

    

class UserLoginView(APIView):
    renderer_classes = [UserRenderer]

    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.data.get('username')
        password = serializer.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            old_tokens = OutstandingToken.objects.filter(user_id=user.id)
            for old_token in old_tokens:
                t, _ = BlacklistedToken.objects.get_or_create(token=old_token)
            token = get_tokens_for_user(user)
            return Response({'token':token, 'msg':'Login Success'}, status=status.HTTP_200_OK)
        else:
            return Response({'error':{'non_field_error':['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)


class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        try:
            print(request.data)
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'msg':'Logged Out Successfully'}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({'msg':'Logout Failed'},status=status.HTTP_400_BAD_REQUEST)
        

class UserProfileView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def put(self, request, format=None):
        try:
            old_profile = Profile.objects.get(user=request.user)
            serializer = UserProfileSerializer(old_profile, data = request.data,
                                                context = {'request': request})
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'profile':serializer.data, 'msg':'Profile Updated'}, status=status.HTTP_202_ACCEPTED)
            return Response({'error':'Some error occured'}, status=status.HTTP_304_NOT_MODIFIED)
        except Profile.DoesNotExist:
            serializer = UserProfileSerializer(data = request.data, context = {'request': request})
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'profile':serializer.data, 'msg':'Profile Updated'}, status=status.HTTP_201_CREATED)
            return Response({'error':'Some error occured'}, status=status.HTTP_403_FORBIDDEN)
        
    def get(self, request, format=None):
        try:
            profile = Profile.objects.get(user=request.user)
            serializer = UserProfileSerializer(profile)
            return Response({'profile':serializer.data, 'msg':'Profile Fetched'}, status=status.HTTP_202_ACCEPTED)
        except Profile.DoesNotExist:
            return Response({'error':'Profile does not exist'},status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request, format=None):
        serializer = UserProfileSerializer(data = request.data, context = {'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'profile':serializer.data, 'msg':'Profile Created'}, status=status.HTTP_201_CREATED)
        return Response({'error':'Some error occured'}, status=status.HTTP_403_FORBIDDEN)




def flushexpired(request):
    OutstandingToken.objects.filter(expires_at__lte=aware_utcnow()).delete()
    blacklisted = BlacklistedToken.objects.all()
    for token in blacklisted:
        OutstandingToken.objects.filter(id=token.token_id).delete()
        BlacklistedToken.objects.filter(token_id=token.token_id).delete()
    return JsonResponse({'msg':'Expired & Blacklisted Tokens have been Flushed'}, status=status.HTTP_205_RESET_CONTENT)