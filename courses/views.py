from django.views.generic import TemplateView,ListView,DetailView,View
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

from .models import Course, Branch_of_study
from memberships.models import StudentMembership


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        category = Branch_of_study.objects.all()
        context['category'] = category
        return context


class AboutView(TemplateView):
    template_name = 'about.html'


class ContactView(TemplateView):
    template_name = 'contact.html'


class CourseListView(ListView):
    context_object_name = 'courses'
    template_name = 'courses/course_list.html'
    model = Course


class CourseDetailView(DetailView):
    context_object_name = 'course'
    template_name = 'courses/course_detail.html'
    queryset = Course.objects.all()
    #model = Course


    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context['student_membership'] = StudentMembership.objects.all()
        context['courses'] = Course.objects.all()
        context['branches'] = Branch_of_study.objects.all()

        return context