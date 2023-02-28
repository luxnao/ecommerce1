from django.urls import path
from .import views
urlpatterns=[
    path('',views.apiOverview,name='home'),
    path('create/',views.add_items,name='add_items'),
    path('all/', views.view_items, name='view_items'),
    path('update/<int:pk>', views.update_items, name='update_items'),

]
