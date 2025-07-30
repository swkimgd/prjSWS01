from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'

class MemberListView(TemplateView):
    template_name = 'members.html'
    