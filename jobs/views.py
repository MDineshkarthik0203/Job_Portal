from django.shortcuts import render
from .models import Job
from rest_framework import viewsets
from .serializers import JobSerializer
from rest_framework.permissions import IsAuthenticated
from applications.models import Application

# Create your views here.
def job_list(request):
    jobs = Job.objects.all()

    applied_jobs = []

    if request.user.is_authenticated:
        applied_jobs = Application.objects.filter(user=request.user).values_list('job_id', flat=True)

    return render(request, 'job_list.html', {
        'jobs': jobs,
        'applied_jobs': applied_jobs
    })


class JobViewSet(viewsets.ModelViewSet):
    queryset=Job.objects.all()
    serializer_class=JobSerializer
    permission_classes=[IsAuthenticated]