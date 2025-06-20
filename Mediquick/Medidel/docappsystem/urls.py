"""
URL configuration for docappsystem project.

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views,adminviews,docviews,userviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE, name='base'),
    path('login', views.LOGIN, name='login'),
    path('login/', views.LOGIN, name='login'),
    path('doctor/login/', views.DOCTOR_LOGIN, name='doctor_login'),
    path('patient/login/', views.PATIENT_LOGIN, name='patient_login'),
    
    path('doLogin', views.doLogin, name='doLogin'),
    path('doLogout', views.doLogout, name='logout'),

    # This is admin panel
    path('Admin/AdminHome', adminviews.ADMINHOME, name='admin_home'),
    path('Admin/Specialization', adminviews.SPECIALIZATION, name='add_specilizations'),
    path('Admin/ManageSpecialization', adminviews.MANAGESPECIALIZATION, name='manage_specilizations'),
    path('Admin/DeleteSpecialization/<str:id>', adminviews.DELETE_SPECIALIZATION, name='delete_specilizations'),
    path('UpdateSpecialization/<str:id>', adminviews.UPDATE_SPECIALIZATION, name='update_specilizations'),
    path('UPDATE_Specialization_DETAILS', adminviews.UPDATE_SPECIALIZATION_DETAILS, name='update_specilizations_details'),
    path('Admin/DoctorList', adminviews.DoctorList, name='viewdoctorlist'),
    path('Admin/ViewDoctorDetails/<str:id>', adminviews.ViewDoctorDetails, name='viewdoctordetails'),
    path('Admin/ViewDoctorAppointmentList/<str:id>', adminviews.ViewDoctorAppointmentList, name='viewdoctorappointmentlist'),
    path('Admin/ViewPatientDetails/<str:id>', adminviews.ViewPatientDetails, name='viewpatientdetails'),
    path('SearchDoctor', adminviews.Search_Doctor, name='search_doctor'),

    path('DoctorBetweenDateReport', adminviews.Doctor_Between_Date_Report, name='doctor_between_date_report'),

    #Website Page
     path('Website/update', adminviews.WEBSITE_UPDATE, name='website_update'),
     path('UPDATE_WEBSITE_DETAILS', adminviews.UPDATE_WEBSITE_DETAILS, name='update_website_details'),

    # This is Doctor Panel
    path('docsignup/', docviews.DOCSIGNUP, name='docsignup'),
    path('Doctor/DocHome', docviews.DOCTORHOME, name='doctor_home'),
    path('Doctor/ViewAppointment', docviews.View_Appointment, name='view_appointment'),
    path('DoctorPatientAppointmentDetails/<str:id>', docviews.Patient_Appointment_Details, name='patientappointmentdetails'),
    path('AppointmentDetailsRemark/Update', docviews.Patient_Appointment_Details_Remark, name='patient_appointment_details_remark'),
     path('DoctorPatientApprovedAppointment', docviews.Patient_Approved_Appointment, name='patientapprovedappointment'),
     path('DoctorPatientCancelledAppointment', docviews.Patient_Cancelled_Appointment, name='patientcancelledappointment'),
     path('DoctorPatientNewAppointment', docviews.Patient_New_Appointment, name='patientnewappointment'),
     path('DoctorPatientListApprovedAppointment', docviews.Patient_List_Approved_Appointment, name='patientlistappointment'),
     path('DoctorAppointmentList/<str:id>', docviews.DoctorAppointmentList, name='doctorappointmentlist'),
     path('PatientAppointmentPrescription', docviews.Patient_Appointment_Prescription, name='patientappointmentprescription'),
      path('PatientAppointmentCompleted', docviews.Patient_Appointment_Completed, name='patientappointmentcompleted'),
      path('SearchAppointment', docviews.Search_Appointments, name='search_appointment'),
      path('BetweenDateReport', docviews.Between_Date_Report, name='between_date_report'),

    #This is User Panel
    path('userbase/', userviews.USERBASE, name='userbase'),
    path('', userviews.Index, name='index'),
    
    path('privacy-policy/', userviews.privacy_policy, name='privacy_policy'),
    path('terms-and-conditions/', userviews.terms_and_conditions, name='terms_conditions'),
    
    path('userappointment/', userviews.create_appointment, name='appointment'),
    path('User_SearchAppointment', userviews.User_Search_Appointments, name='user_search_appointment'),
    path('ViewAppointmentDetails/<str:id>/', userviews.View_Appointment_Details, name='viewappointmentdetails'),
    
    # Patient URLs
    path('patient/signup/', userviews.patient_signup, name='patient_signup'),
    path('patient/dashboard/', userviews.patient_dashboard, name='patient_dashboard'),
    path('patient/profile/', userviews.patient_profile, name='patient_profile'),
    path('patient/appointment/cancel/<int:appointment_id>/', userviews.cancel_appointment, name='cancel_appointment'),
 
    
    



    #profile path
    path('Profile', views.PROFILE, name='profile'),
    path('Profile/update', views.PROFILE_UPDATE, name='profile_update'),
    path('Password', views.CHANGE_PASSWORD, name='change_password'),

    # Password Reset URLs
    path('password-reset/', 
         auth_views.PasswordResetView.as_view(
             template_name='password_reset.html',
             email_template_name='password_reset_email.html',
             subject_template_name='password_reset_subject.txt'
         ),
         name='password_reset'),
    path('password-reset/done/', 
         auth_views.PasswordResetDoneView.as_view(
             template_name='password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='password_reset_complete.html'
         ),
         name='password_reset_complete'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
