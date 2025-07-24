from django.contrib import admin
from django.urls import path, include
from participants.views import sign_in, sign_out, sign_up, admin_Dashboard, activate_user, assign_Role,create_participant, create_category,delete_user, category_list,create_group,group_list, delete_group
from event.views import createEvent,viewEvents
from core.views import noPermission
urlpatterns = [
    path('no-permission/',noPermission,name='noPermission'),
    path('sign-up/',sign_up,name='sign_up'),
    path('sign-in/',sign_in,name='sign_in'),
    path('sign-out/',sign_out,name='sign_out'),
    path('activate/<int:user_id>/<str:token>/',activate_user),
    path('admin/dashboard',admin_Dashboard,name='admin_Dashboard'),
    path('admin/create-group/',create_group,name='create_group'),
    path('admin/delete-group/<int:group_id>/', delete_group, name='delete_group'),
    path('admin/delete-user/<int:user_id>/', delete_user, name='delete_user'),
    path('admin/group-list/',group_list,name='group_list'),
    path('admin/create-category/',create_category,name='create_category'),
    path('admin/create-events/',createEvent,name='create_events'),
    path('admin/view-events/',viewEvents,name='view_events'),
    path('admin/create-participant/',create_participant,name='create_participant'),
    path('admin/category-list/',category_list,name='category_list'),
    path('admin/<int:user_id>/assign-role/',assign_Role,name='assign_Role'),
    path('activate/<int:user_id>/<str:token>/',activate_user),
]
