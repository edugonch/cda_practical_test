from django.contrib import admin
from django.urls import path, re_path
from rfp_crud import views

app_name = 'rfp_crud'

urlpatterns = [
    path('', views.index, name='index'),
    path('rfp', views.rfp_list, name='list'),
    path('rfp/pdf_list', views.rfp_list_pdf, name='pdf_list'),
    path('rfp/new', views.rfp_create, name='new'),
    path('rfp/edit/<uuid:id>', views.rfp_update, name='edit'),
    path('rfp/delete/<uuid:id>', views.rfp_delete, name='delete'),
    path('rfp/<uuid:id>', views.rfp_show, name='show')
]
