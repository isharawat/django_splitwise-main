from django.urls import path
from django.contrib import admin
from . import views

from django.conf import settings 
from django.conf.urls.static import static
from django.views.generic.base import TemplateView # new


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('groups/', views.groups, name='groups'),
    path('', TemplateView.as_view(template_name='registration/login.html'), name='home'), 
    path('success/', views.success, name = 'success'),
    path('transaction/',views.transaction,name='transaction'),
    path('transaction/forms/',views.transaction_form_multiple,name='transaction_form_multiple'),
    path('transaction/form/<str:f>/',views.transaction_form, name='transaction_form'),
    path('transaction/form/',views.transaction_form_multiple, name='transaction_form_multiple'),
    path('groups/transaction/',views.group_transaction, name='group_transaction'),
    
    path('friend/<str:f>/', views.friend, name='friend'),
    path('group/<str:g>/', views.group, name='group'),
    path('activity_tab/', views.activity_tab, name='activity_tab'),
    path('detailed_activity/<str:i>/',views.detailed_activity1, name='detailed_activity'),
    path('detailed_activity/<str:i>/<str:j>/',views.detailed_activity2, name='detailed_activity'),
]

if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT)

