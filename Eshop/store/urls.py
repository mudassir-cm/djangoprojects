from django.urls import path
from store import views
from store.views import Login, Index, Cart, CheckOut, OrderView

urlpatterns = [
   # path('', views.index, name='index'),
    path('', Index.as_view(), name='index'),
    path('signup/', views.signup, name='signup'),
   # path('user_login/', views.user_login, name='user_login'),
    path('user_login/', Login.as_view(), name='user_login'),
    path('logout/', views.logout, name='logout'),
    path('cart/', Cart.as_view(), name='cart'),
    path('checkout', CheckOut.as_view(), name='checkout'),
    path('order/', OrderView.as_view(), name='order'),
]