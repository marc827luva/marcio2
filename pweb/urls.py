from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('', views.index,name='index'),
    path('sobre', views.sobre,name='sobre'),
    path('contato', views.contato,name='contato'),
    path('ajudar', views.ajudar,name='ajudar'),

    path('exibiritem/<int:id>', views.exibiritem,name='exibiritem'),
    
    path('perfil/<str:usuario>/',views.perfil,name='perfil'),
    path('agendamento/<int:id>',views.agendamento,name='dia'),

    path('dados/',views.dados,name='dados'),
    path('form/',views.form,name='form'),

]