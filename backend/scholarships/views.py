from rest_framework import generics, permissions

from .models import Scholarship
from .permissions import IsAdminOrReadOnly
from .serializers import ScholarshipSerializer


class ScholarshipEditList(generics.ListCreateAPIView):
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Scholarship.objects.all()
    serializer_class = ScholarshipSerializer

class ScholarshipEditDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminOrReadOnly,)
    queryset = Scholarship.objects.all()
    serializer_class = ScholarshipSerializer
