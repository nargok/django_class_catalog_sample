from django.views.generic import ListView, DetailView

from .models import Broadcast, Teacher

class BroadcastListView(ListView):
  model = Broadcast
  context_object_name = 'broadcasts'

class BroadcastDetailView(DetailView):
  model = Broadcast
  context_object_name = 'broadcast'

class TeacherDetailView(DetailView):
  model = Teacher
  context_object_name = 'teacher'