"""
URL configuration for credit_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from credit.views import *

urlpatterns = [
    path('', Home.as_view()),
    path('admin/', admin.site.urls),
    path('fill-data/', FillDataView.as_view()),
    path('register/', RegisterView.as_view(), name='register'),
    path('check-eligibility/', CheckEligibilityView.as_view()),
    path('create-loan/', CreateLoanView.as_view(), name='create-loan'),
    path('view-loan/<int:loan_id>/', ViewLoanView.as_view(), name='view-loan'),
    path('view-loans/<int:customer_id>', ViewLoansView.as_view(), name='view-loans')
]
