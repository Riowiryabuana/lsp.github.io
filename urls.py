from django.contrib import admin
from django.urls import path
from laundry_app import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.manajemen_kasir, name='manajemen_kasir'), 
    path('update-status/<str:tipe>/<int:id>/', views.update_status, name='update_status'),
]