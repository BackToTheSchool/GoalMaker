from django.urls import path

from GoalMakerWeb import apis
from . import views

app_name = 'GoalMakerWeb'
urlpatterns = [
    # ex: 127.0.0.1/goal_detail/davkim&work%20out/
    # path('goal_detail/<str:user_id>&<str:name>/', views.detail, name='detail'),

    # ex: 127.0.0.1/
    path('', views.main, name='main'),
    path('login/', views.login, name='login'),
    path('login_action/', views.login_action, name='login_action'),
    path('logout/', views.logout, name='logout'),

    # views
    # ex: 127.0.0.1/create_user/
    path('sign_up/', views.create_user, name='create_user'),
    path('detail_user/', views.detail_user, name='detail_user'),
    path('update_user/', views.update_user, name='update_user'),

    path('create_goal/', views.create_goal, name='create_goal'),
    path('detail_goal/', views.detail_goal, name='detail_goal'),
    path('select_goal/', views.select_goal, name='select_goal'),
    path('update_goal/', views.update_goal, name='update_goal'),

    path('create_work/', views.create_work, name='create_work'),
    path('detail_work/', views.detail_work, name='detail_work'),
    path('select_work/', views.select_work, name='select_work'),
    path('update_work/', views.update_work, name='update_work'),

    # apis
    # ex: 127.0.0.1/api/<str:model_name>/<str:method>/    with POST method
    path('api/user/create/', apis.user_create, name='create_user_api'),
    path('api/user/read/', apis.user_read, name='read_user_api'),
    path('api/user/update/', apis.user_update, name='update_user_api'),
    path('api/user/delete/', apis.user_delete, name='delete_user_api'),
    path('api/user/exist/', apis.user_exist, name='exist_user_api'),

    path('api/goal/create/', apis.goal_create, name='create_goal_api'),
    path('api/goal/read/', apis.goal_read, name='read_goal_api'),
    path('api/goal/update/', apis.goal_update, name='update_goal_api'),
    path('api/goal/delete/', apis.goal_delete, name='delete_goal_api'),
    path('api/goal/exist/', apis.goal_exist, name='exist_goal_api'),

    path('api/work/create/', apis.work_create, name='create_work_api'),
    path('api/work/read/', apis.work_read, name='read_work_api'),
    path('api/work/update/', apis.work_update, name='update_work_api'),
    path('api/work/delete/', apis.work_delete, name='delete_work_api'),
    path('api/work/exist/', apis.work_exist, name='exist_work_api'),
]
