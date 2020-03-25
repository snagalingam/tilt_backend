from django.urls import path

from .views import ScholarshipEditList, ScholarshipEditDetail

urlpatterns = [
    path('<int:pk>/', ScholarshipEditDetail.as_view()),
    path('', ScholarshipEditList.as_view()),
]
