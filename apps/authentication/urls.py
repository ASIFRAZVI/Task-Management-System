from rest_framework.urls import path
from .views import UserRegisteration, UserLoginView,UserLogoutView,VerifyUser, resend_otp
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # register user
    path("signup/", UserRegisteration.as_view(), name="register_user"),
    # login user
    path("signin/", UserLoginView.as_view(), name="login_user"),
    # logout user
    path("signout/", UserLogoutView.as_view(), name="logout_user"),
    # verify user
    path("verify/", VerifyUser.as_view(), name="ativate_account"),
    # resend otp
    path("resend-otp/", resend_otp, name="resend_otp"),
    # # simple jwt urls
    # path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
