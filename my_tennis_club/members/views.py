from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.shortcuts import render
from .models import Member

def testing(request):
    try:
        mymembers = Member.objects.all()
        return render(request, 'members/members_list.html', {'mymembers': mymembers})
    except Exception as e:
        return HttpResponse(f"An error occurred: {str(e)}", status=500)