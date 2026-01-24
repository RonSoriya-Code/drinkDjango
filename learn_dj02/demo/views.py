from django.shortcuts import render

# Create your views here.

def subjectStudy(request):
    context = {
        "subjectTitle": "Python-Django Development",
        "subjectCredit": "3",
        "subectPrice": "3.12"
    }

    return render(request, 'subject.html', context)