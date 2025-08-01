from django.contrib.auth.views import (LoginView, PasswordChangeView, PasswordChangeDoneView, PasswordResetCompleteView,
                                       PasswordResetDoneView, PasswordResetView, PasswordResetConfirmView)
from django.urls import path

from .views import logout_view, dashboard_view, edit_user, dashboard

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/',  logout_view, name='logout'),
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('profile/', dashboard, name='dashboard'),
    path('dashboard/<str:username>/', dashboard_view , name='dashboard_user'),
    path('profile/edit/', edit_user, name='registration'),
    path('password-change-done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password-reset-done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

