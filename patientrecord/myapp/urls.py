from django.urls import path
from myapp import views

urlpatterns = [
  path('dashboard/', views.dashboard, name='dashboard'),
  path('usersignup/', views.usersignup, name='usersignup'),
  path('userlogin/', views.userlogin, name='userlogin'),
  path('userlogout/', views.userlogout, name='userlogout'),
  path('addpatient/', views.addpatient, name='addpatient'),
  path('updatepatient/<int:id>/', views.updatepatient, name='updatepatient'),
  path('deletepatient/<int:id>/', views.deletepatient, name='deletepatient'),
  path('patienthistory/<int:id>/', views.patienthistory, name='patienthistory'),
  path('addpatienthistory/<int:id>/', views.addpatienthistory, name='addpatienthistory'),
  path('deletepatienthistory/<int:id>/', views.deletepatienthistory, name='deletepatienthistory'),
  path('updatepatienthistory/<int:id>', views.updatepatienthistory, name='updatepatienthistory'),
]