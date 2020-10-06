from django.urls import path

from .views import index, other_page, BBLoginView, BBLogoutView, profile, ChangeUserInfoView

app_name = 'main'

urlpatterns = [
    path('accounts/login', BBLoginView.as_view(), name='login'),
    path('accounts/logout', BBLogoutView.as_view(), name='logout'),
    path('accounts/profile/change/', ChangeUserInfoView.as_view(), name='profile_change'),
    path('accounts/profile/', profile, name='profile'),
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index'),
]
