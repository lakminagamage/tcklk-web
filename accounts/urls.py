from .views import loginView,signupView,profileView,update_profileView,change_passwordView,adminpanelActions
from django.urls import path
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/' , auth_views.LoginView.as_view(template_name='users/login.html'), name='loginUrl'),
    path('logout/' , auth_views.LogoutView.as_view(template_name='users/logout.html') , name='logoutUrl'),
    path('password-reset/' , auth_views.PasswordResetView.as_view(template_name='users/reset.html') , name='password_reset'),
    path('password-reset/done/' , auth_views.PasswordResetDoneView.as_view(template_name='users/reset-success.html') , name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/' , auth_views.PasswordResetConfirmView.as_view(template_name='users/password-reset-confirm.html') , name='password_reset_confirm'),
    path('password-reset-complete/' , auth_views.PasswordResetCompleteView.as_view(template_name='users/password-reset-complete.html') , name='password_reset_complete'),
    path('signup/' ,signupView , name='signupUrl'),
    path('myaccount/', profileView , name='myaccountUrl' ),
    path('updateProfile/', update_profileView, name='updateprofileUrl'),
    path('changeCreds/', change_passwordView, name='changepassUrl' ),
    path('adminconsole/', adminpanelActions, name='adminpanelactionsUrl')



]