from django.contrib.auth import login as django_login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .models import SalesPerson, User
from .serializers import RegisterSerializer


def authenticate( username=None, password=None ):
    # Check the username/password and return a User.
    if username != None and password != None:
        # Get the user
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                # logger.info('User is authenticated, logging user in')
                return user
        except User.DoesNotExist:
            pass
    return None

@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'Username already exists'})

        # Create a new user
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return JsonResponse({'success': 'User registered successfully'})

    return JsonResponse({'error': 'Invalid request'})

@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            django_login(request, user)

            # Generate token
            refresh = RefreshToken.for_user(user)

            return JsonResponse({'success': 'User logged in successfully', 'access_token': str(refresh.access_token), 'refresh_token': str(refresh)})
        else:
            return JsonResponse({'error': 'Invalid username or password'})

    return JsonResponse({'error': 'Invalid request'})