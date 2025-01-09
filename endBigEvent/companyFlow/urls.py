from django.urls import path
from companyFlow.views import selectByCompany,testCompanyFlow,selectByTime

urlpatterns = [
    path('s',selectByCompany),
    path('select',testCompanyFlow),
    path('t',selectByTime),
]