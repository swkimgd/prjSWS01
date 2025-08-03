from django.views.generic import TemplateView, ListView
from .models import Member

class IndexView(TemplateView):
    template_name = 'index.html'

class MemberListView(ListView):
    template_name = 'members.html'
    model = Member
    context_object_name = 'member_list'
