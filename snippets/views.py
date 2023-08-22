from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Snippet
from .serializers import SnippetSerializer

# csrf_exempt
# api를 만들경우 csrf 보안이 필요하지않으므로, csrf를 꺼주는 전처리기
