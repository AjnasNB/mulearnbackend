from django.urls import path
from . import profile_view

urlpatterns = [
    # path('add', portal_views.AddPortal.as_view()),
    path('user-log/', profile_view.UserLogAPI.as_view()),
    path('edit-user-profile/', profile_view.EditUserDetailsAPI.as_view()),
]