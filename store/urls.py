from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm,MySetPasswordForm

urlpatterns = [
    path('',views.Home.as_view(),name='home'),

    path('category/',views.category,name='category'),
    path('report/',views.report,name='report'),
    path('search/',views.search,name='search'),

    path('accounts/login/',auth_views.LoginView.as_view(template_name='login1.html',authentication_form=LoginForm),name='login'),

    path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),

    path('registration/',views.CustomerRegistrationView.as_view(),name='customeregistration'),

    path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name='changepsswd.html',form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'),name='passwordchange'),

    path('passwordchangedone/',auth_views.PasswordChangeView.as_view(template_name='passwordchangedone.html'),name='passwordchangedone'), 

    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='password_reset.html',form_class=MyPasswordResetForm),name='password_reset'),

    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html',form_class=MySetPasswordForm),name='password_reset_confirm'),

    path('password-reset-complete',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),


    path('product_details/<int:pk>',views.Product_Details.as_view(),name='product_details'),

    path('add_to_cart/',views.add_to_cart,name='add_to_cart'),

    path('cart/',views.show_cart,name="showcart"),
    path('pluscart/',views.plus_cart),
    path('minuscart/',views.minus_cart),
    path('removecart/',views.remove_cart),
    path('orders/',views.orders,name="orders"),

    path('checkout/',views.checkout,name='checkout'),
    path('paymentdone/',views.paymentdone,name='paymentdone'),

 
    path('interior/',views.Interior,name='interior'),
    path('interior/<slug:data>',views.Interior,name='interiordata'),
    path('exterior/',views.Exterior,name='exterior'),
    path('exterior/<slug:data>',views.Exterior,name='exteriordata'),
    path('accessories/',views.Accessories,name='accessories'),
    path('accessories/<slug:data>',views.Accessories,name='accessoriesdata'),
    path('profile/',views.ProfileView.as_view(),name='profile'),
    path('address/',views.address,name='address')

]