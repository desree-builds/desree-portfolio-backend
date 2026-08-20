from django.urls import path, include
from .views import SkillListView

urlpatterns = [
    path('skills/', SkillListView.as_view(), name='Skill-list'),
]

