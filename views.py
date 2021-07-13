from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect

from django.views.generic import ListView,CreateView, UpdateView, DeleteView
import pickle
import json
from .models import student
# from .forms import *
from django.contrib.auth.decorators import login_required
# from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_exempt
# from .models import PicPost

# Create your views here.


def home(request):
	st=student.objects.all()
	# return HttpResponse(st)
	return render(request=request, template_name="index.html", context={"st":st})

class DataCreateView(CreateView):
	model = student
	fields = ['enrl_no','first_name','last_name','age','batch','course','address']
	template_name="data_insert.html"

	def form_valid(self, form):
		return super().form_valid(form)

class DataUpdateView(UpdateView):
	model = student
	fields = ['enrl_no','first_name','last_name','age','batch','course','address']
	template_name="data_update.html"
	def form_valid(self, form):
		return super().form_valid(form)


class DataDeleteView(DeleteView):
	model=student
	success_url="/"
	template_name = "student_confirm_delete.html"


def about(request):
	return render(request=request,template_name="about.html", context={})

