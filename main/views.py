from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, FormView, CreateView
from django.views.generic.detail import SingleObjectMixin
from main import models,forms
from django.contrib.auth.mixins import PermissionRequiredMixin
# Create your views here.
class Index(ListView):
    template_name = 'main/index.html'
    model = models.Question
class Question(PermissionRequiredMixin,SingleObjectMixin,FormView):
    model=models.Question
    template_name = 'main/question.html'
    form_class =forms.AnswerForm
    permission_required = ['add_answer']
    def form_valid(self, form):
        obj=form.save(commit=False)
        obj.question=self.get_object()
        obj.user=self.request.user
        obj.save()
        return HttpResponseRedirect('/')
    def get_context_data(self, **kwargs):
        data=super().get_context_data(**kwargs)
        data['answer']=models.Answer.objects.filter(
            question=self.get_object(),
            user=self.request.user
        )
        return data

    def get(self,request,*args,**kwargs):
        self.object=self.get_object()
        context=self.get_context_data(object=self.object)
        return self.render_to_response(context)
    def post(self, request, *args, **kwargs):
        self.object=self.get_object()
        return super().post(request,*args,**kwargs)

class CreateQuestion(CreateView, PermissionRequiredMixin):
    permission_required = ['add_question']
    model= models.Question
    template_name = 'main/question_create.html'
    fields = '__all__'
    success_url ='/'
