from django.shortcuts import render
from django.views import generic

class BaseView(generic.TemplateView):
    template_name = "base.html"

class IndexView(generic.TemplateView):
    template_name = "index.html"

class HomeView(generic.TemplateView):
    template_name = "home-page.html"

class ServicesView(generic.TemplateView):
    template_name = "services.html"

class AboutusView(generic.TemplateView):
    template_name = "about-us.html"

class AboutmeView(generic.TemplateView):
    template_name = "about-me.html"

class ContactsView(generic.TemplateView):
    template_name = "contacts.html"

class HmView(generic.TemplateView):
    template_name = "hm.html"

class GurafuView(generic.TemplateView):
    template_name = "gurafu.html"

# test
class MonthDashboard(generic.TemplateView):
    """月間支出ダッシュボード"""
    template_name = 'hm.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # これから表示する年月
        year = int(self.kwargs.get('year'))
        month = int(self.kwargs.get('month'))
        context['year_month'] = f'{year}年{month}月'

        # 前月と次月をコンテキストに入れて渡す
        if month == 1:
            prev_year = year - 1
            prev_month = 12
        else:
            prev_year = year
            prev_month = month - 1

        if month == 12:
            next_year = year + 1
            next_month = 1
        else:
            next_year = year
            next_month = month + 1
        context['prev_year'] = prev_year
        context['prev_month'] = prev_month
        context['next_year'] = next_year
        context['next_month'] = next_month

        return context
# Create your views here.
