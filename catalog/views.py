from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.views import View

from .models import Broadcast, Teacher
from .view_models import BroadcastViewModel

class BroadcastListView(ListView):
  model = Broadcast
  context_object_name = 'broadcasts'

class BroadcastDetailView(View):
  def get(self, request, *args, **kwargs):
    length = 1000
    broadcast = Broadcast.objects.get(id=self.kwargs['pk'])
    broadcast = BroadcastViewModel(broadcast, length=length)
    context = {
      'broadcast': broadcast
    }
    return render(request, 'catalog/broadcast_detail.html', context)

class TeacherDetailView(DetailView):
  model = Teacher
  context_object_name = 'teacher'