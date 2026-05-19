from django.urls import path

from . import views

urlpatterns = [
    path('',views.register,name='register'),
    path('task',views.task,name='task'),
    path('test/',views.test,name='test'),
    path('add/',views.form_task,name='form'),
    path('delete/<int:id>/',views.delete_task,name='delete_task'),
    path('complete/<int:id>/',views.complet_task,name='complete_task'),
    path('uncomplete/<int:id>/', views.uncomplet_task, name='uncomplete_task'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout')

]
