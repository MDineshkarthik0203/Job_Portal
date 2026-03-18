from django.contrib import admin
from django.urls import path, include
from accounts.views import register_page, login_page, logout_page
from jobs.views import job_list, recruiter_jobs
from applications.views import apply_job, job_applications
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', job_list),
    path('register/', register_page),
    path('login/', login_page),
    path('logout/', logout_page),
    path('apply/<int:job_id>/', apply_job),

    path('api/', include('accounts.urls')),
    path('api/', include('jobs.urls')),
    path('api/', include('applications.urls')),

    path('my-jobs/', recruiter_jobs),
    path('job-applications/<int:job_id>/', job_applications),
]

# ✅ ALWAYS AT BOTTOM
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)