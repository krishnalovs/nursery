# urls.py

from django.urls import path
from .views import *
from django.conf import settings    
from django.conf.urls.static import static

urlpatterns = [
    path('', navbar_view, name='navbar'),

    path('Nursery/', category_lists, name='category_lists'),

    path('Nursery/<slug:nav_slug>', nav_lists, name='nav_lists'),

    path('Nursery/<slug:nav_slug>/', category_list, name='category_list'),

    path('Nursery/<slug:nav_slug>/<slug:item_slug>', subcategory_list, name='subcategory_list'),
    
    path("search",search_view, name="search_view"),

    path("cart", add_to_cart, name="add_to_cart"),

    path('Refundpolicy',Refundpolicy, name='Refundpolicy'),

    path('Terms-of-service',Termsofservice, name='Termsofservice'),

    path('shippingpolicy',shippingpolicy, name='shippingpolicy'),

    path('privacypolicy',privacypolicy, name='privacypolicy'),

    path('jobs/',jobs, name='jobs'),

    path('contact/',contact, name='contact'),

    path('blogs/',blogs, name='blogs'),

    path('fruits/',fruits, name='fruits'),

    path('incredible/',incredible, name='incredible'),

    path('have',have, name='have'),

    path('white/',white, name='white'),

    path('vegetables/',vegetables, name='vegetables'),

    path('ever/',ever, name='ever'),

    path('indoor/',indoor, name='indoor'),

    path('butterfly/',butterfly, name='butterfly'),

    path('absorb/',absorb, name='absorb'),

    path('magical/',magical, name='magical'),

    path('rise/',rise, name='rise'),

    path('why/',why, name='why'),

    path('login/', login_page, name='login_page'), # Login page

	path('register/', register_page, name='register'), # Registration page

    path('Review',Review, name='Review'),

    path('product/<int:id>',product, name='product'),
    path('product_list/',product_list,name='product_list'),

    path('profile/',my_profile_view,name="profile"),

    # Add other paths as needed
    path('cart/', view_cart, name='view_cart'),

    path('add/<int:item_id>/', add_to_cart, name='add_to_cart'),

    path('remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),

    path('add/address',add_address,name='add_address'),

    path('edit/address/<int:id>', edit_address, name='edit_address'), 

    path('address/', address_list, name='address_list'),

    path('delete/<int:id>/', delete_address, name='delete_address'),

    path('select_address/<int:id>/', select_address, name='select_address'),

    path('edit_profile/', edit_profile_view, name='edit_profile'), 

      path('add_profile/', add_profile, name='add_profile'), 


    path('customer-address', customer_address_view,name='customer-address'),

    # path('payment-success', payment_success_view,name='payment-success'),

    # path('my-order', my_order_view,name='my-order'),
    path('contact/', contact,name='contact'),
    

    path('logout',logout_view,name ="logout"),

       path('orders',orders,name ="orders"),
    
    path('orders/status',order_status,name ="order_status"),

    path('rewards',reward,name ="rewards"),

    path('offers',offers,name ="offers"),
    
    path('subscribe/',subscribe,name="subscribe")
    
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

