from django.urls import path, include

from .views import *



urlpatterns = [
    path('api/register/', UserListCreateView.as_view(), name='user-list-create'),
    path('token/', ObtainTokenPairWithRoleView.as_view(), name='token_obtain_pair'),
    path('admin-only/', AdminOnlyView.as_view(), name='admin-only'),
    path('staff-only/', StaffOnlyView.as_view(), name='staff-only'),
    path('api/login/', ObtainTokenPairWithRoleView.as_view(), name='token_obtain_pair'),
    path('api/reset-password/', PasswordResetRequestView.as_view(), name='password_reset'),
    path('reset/<uidb64>/<token>/', password_reset_confirm, name='password_reset_confirm'),
    # path('activate/<uidb64>/<token>/', activate, name='activate'),

]
# <html>
# <head>
#     <title>Activate your account</title>
# </head>
# <body>
#     <p>Hi {{ user.username }},</p>
#     <p>Thanks for registering. Please click on the link below to activate your account:</p>
#     <p><a href="http://{{ domain }}{% url 'activate' uidb64=uid token=token %}">Activate Account</a></p>
#     <p>Thank you!</p>
# </body>
# </html>