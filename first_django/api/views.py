from rest_framework import viewsets, permissions
from .serializers import QuestionSerializer, ChoiceSerializer
from my_polls.models import Question, Choice

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by("-pub_date")
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    permission_classes = [permissions.AllowAny]


