# views.py
from django.shortcuts import render, redirect,get_object_or_404
from .forms import *
from .models import *
from django.db.models import Q
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import json
from django.contrib.auth import logout

categories = Navbar.objects.all()

def navbar_view(request):
    navbars = Navbar.objects.all()
    return render(request, 'Home.html', {'categories': navbars})


def nav_lists(request,nav_slug):
    categories = Navbar.objects.all()
    selected_items = Items.objects.filter(navbar__slug=nav_slug)
    context = {'categories': categories,'selected_items': selected_items}
    return render(request, 'product.html', context)


def category_lists(request):
    categories = Navbar.objects.all()
    product = Items.objects.all()
    return render(request, 'product.html', {'categories': categories, 'selected_items': product})


def category_list(request, nav_slug):
    categories = Navbar.objects.all()
    selected_items = Items.objects.filter(category__slug=nav_slug)
    context = {'categories': categories,'selected_items': selected_items}
    return render(request, 'product.html', context)
    # category = get_object_or_404(Navbar, nav_slug=nav_slug)
    # subcategories = Dropdown.objects.filter(category=category)
    # return render(request, 'navbar.html', {'category': category, 'subcategories': subcategories})


def subcategory_list(request, nav_slug, item_slug):
    categories = Navbar.objects.all()
    selected_items = Items.objects.filter(category__slug=nav_slug,subcategory__slug=item_slug)
    context = {'categories': categories,'selected_items': selected_items}
    return render(request, 'product.html', context)

def search_view(request):
    categories = Navbar.objects.all()
    query = request.GET['search']
    items= Items.objects.all().filter(slug__icontains=query)
    if 'items__ids' in request.COOKIES:
        items_ids = request.COOKIES['item__ids']
        counter=items_ids.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=0
      
    word="Searched Result :"

    if request.user.is_authenticated:
        return render(request,'product.html',{'categories': categories,'selected_items':items,'word':word,'product_count_in_cart':product_count_in_cart})
    return render(request,'product.html',{'categories': categories,'selected_items':items,'word':word,'product_count_in_cart':product_count_in_cart})

def add_to_cart(request):
    return render(request,'add_to_cart.html')


def product(req,id):
    categories = Navbar.objects.all()
    product =Items.objects.get(id=id)
    return render(req,'Description.html',{'categories': categories, 'i':product})

def Refundpolicy(req):
    return render(req,'Refundpolicy.html',{'categories': categories})

def Termsofservice(req):
    return render(req,'Termsofservice.html',{'categories': categories})

def shippingpolicy(req):
    return render(req,'shippingpolicy.html',{'categories': categories})


def privacypolicy(req):
    categories = Navbar.objects.all()
    return render(req,'privacypolicy.html',{'categories': categories})

def blogs(req):
    categories = Navbar.objects.all()
    return render(req,'Blogs.html',{'categories': categories})

def absorb(req):
    return render(req,'Absorb.html',{'categories': categories})

def butterfly(req):
    return render(req,'Butterfly.html',{'categories': categories})

def indoor(req):
    return render(req,'indoorplant.html',{'categories': categories})

def magical(req):
    return render(req,'Magical Ashwagandha.html',{'categories': categories})

def rise(req):
    return render(req,'The Rise of Shilajit.html',{'categories': categories})

def why(req):
     return render(req,'Why Ayurveda is the Real Deal.html',{'categories': categories})

def have(req):
    return render(req,'Have.html',{'categories': categories})

def incredible(req):
    return render(req,'8Incredible.html',{'categories': categories})

def white(req):
    return render(req,'whiterosemean.html',{'categories': categories})  

def vegetables(req):
    return render(req,'8Vegetables.html',{'categories': categories})

def fruits(req):
    return render(req,'10Fruits.html',{'categories': categories})

def ever(req):
    return render(req,'Everwondered.html',{'categories': categories})

def jobs(req):
    return render(req,'jobs.html',{'categories': categories})



def contact(req):
    return render(req,'contact.html',{'categories': categories})

def Review(req):
    categories = Navbar.objects.all()
    return render(req,'Review.html')

def login_page(request):
	# Check if the HTTP request method is POST (form submission)
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		# Check if a user with the provided username exists
		if not User.objects.filter(username=username).exists():
			# Display an error message if the username does not exist
			messages.error(request, 'Invalid Username')
			return redirect('/login/')
		
		# Authenticate the user with the provided username and password
		user = authenticate(username=username, password=password)
		
		if user is None:
			# Display an error message if authentication fails (invalid password)
			messages.error(request, "Invalid Password")
			return redirect('/login/')
		else:
			# Log in the user and redirect to the home page upon successful login
			login(request, user)
			return redirect('navbar')
	
	# Render the login page template (GET request)
	return render(request, 'login.html')

# Define a view function for the registration page


def product_list(request):
    products = Items.objects.all()

    # Filter by category
    category = request.GET.get('category')
    if category:
        products = Items.filter(category=category)

    # Filter by price range
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price and max_price:
        products = Items.objects.filter(dis_price__range=(min_price, max_price))

    return render(request, 'product.html', {'selected_items': products,'categories':categories})

def register_page(request):
	# Check if the HTTP request method is POST (form submission)
	if request.method == 'POST':
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		# Check if a user with the provided username already exists
		user = User.objects.filter(username=username)
		
		if user.exists():
			# Display an information message if the username is taken
			messages.info(request, "Username already taken!")
			return redirect('/register/')
		
		# Create a new User object with the provided information
		user = User.objects.create_user(
			first_name=first_name,
			last_name=last_name,
			username=username
		)
		
		# Set the user's password and save the user object
		user.set_password(password)
		user.save()
		
		# Display an information message indicating successful account creation
		messages.info(request, "Account created Successfully!")
		return redirect('/login/')
     
    

	
	# Render the registration page template (GET request)
	return render(request, 'register.html')

@login_required
def view_cart(request):
	cart_items = Cart.objects.filter(user=request.user)
	total_price = sum(item.product.dis_price * item.quantity for item in cart_items)
	return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price,'categories':categories})
@login_required
def add_to_cart(request, item_id):
	product = Items.objects.get(id=item_id)
	cart_item, created = Cart.objects.get_or_create(product=product, user=request.user)
	cart_item.quantity += 1
	cart_item.save()
	return redirect('view_cart')

@login_required
def remove_from_cart(request, item_id):
	cart_item = Cart.objects.get(id=item_id)
	cart_item.delete()
	return redirect('view_cart')

@login_required
def order_tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        try:
            order=Order.objects.filter(pk=orderId)

            if len(order)>0:
                update = Order.objects.filter(pk=orderId)
                updates = []
                for order in update:
                    # change order status to scheduled
                    if order.status == 'processing':
                        order.status = 'scheduled'
                        order.save()
                    updates.append({'status' : order.status})
                    response = json.dumps(updates)
                    return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            # add some logging here
            return HttpResponse('{}')
    return render(request,"tracker.html",{'categories': categories})

@login_required
def add_profile(request):
     if request.method == 'POST':
         form = UserProfileForm(request.POST)
         if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
             # you might associate this address with a specific user or order
            return redirect('/profile/')
     else:
         form = UserProfileForm()
     return render(request, 'add_profile.html', {'form': form,'categories': categories})

@login_required
def add_address(request):
     if request.method == 'POST':
         form = AddressForm(request.POST)
         if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
             # you might associate this address with a specific user or order
            return redirect('/address/')
     else:
         form = AddressForm()
     return render(request, 'edit_address.html', {'form': form,'categories': categories})


@login_required
def edit_address(request,id):
    address = get_object_or_404(Address, pk=id, user=request.user)
    if request.method == 'POST':
        form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            return redirect('address_list')
    else:
        form = AddressForm(instance=address)
    return render(request, 'edit_address.html', {'form': form})

@login_required
def delete_address(request,id):
	address = Address.objects.get(id=id)
	address.delete()
	return redirect('address_list')

@login_required
def address_list(request):
    addresses = Address.objects.filter(user=request.user)
    return render(request, 'address_list.html', {'addresses': addresses,'categories': categories})

@login_required
def select_address(request,id):
    # Perform actions based on selected address
    return redirect('navbar')

def logout_view(request):
    logout(request)
    # Redirect to a specific URL after logout
    return redirect('navbar') 

# @login_required
# def edit_profile(request):
#     profile = request.user
#     if request.method == 'POST':
#         form = UserProfileForm(request.POST, instance=profile)
#         if form.is_valid():
#             form.save()
#             return redirect('navbar')
#     else:
#         form = UserProfileForm(instance=profile)
#     return render(request, 'edit_profile.html', {'form': form,'categories': categories})


def my_profile_view(request):
    customer=User.objects.get(id=request.user.id)
    address = Address.objects.filter(user=request.user)
    return render(request,'my_profile.html',{'customer':customer,'categories': categories,'address':address})

def cart(request):
    if request.user.is_authenticated:
        cart_count = Cart.objects.filter(user=request.user).count()
    else:
        cart_count = 0

    context = {
        'cart_count': cart_count
    }
    return redirect('add_to_cart')


# def update_quantity(request, product_id):
#     product = get_object_or_404(Items, pk=product_id)
    
#     if request.method == 'POST':
#         form = UpdateQuantityForm(request.POST)
#         if form.is_valid():
#             new_quantity = form.cleaned_data['quantity']
#             product.quantity = new_quantity
#             product.save()
#             return redirect('view_cart', product_id=product.id)
#     else:
#         form = UpdateQuantityForm()

#     return render(request, 'cart.html', {'form': form, 'product': product})

@login_required
def edit_profile_view(request):
    user=User.objects.get(id=request.user.id)
    userForm = CustomerUserForm(instance=user)
    mydict={'userForm':userForm,'categories': categories}
    if request.method=='POST':
        userForm=CustomerUserForm(instance=user)
        if userForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/profile')
    return render(request,'edit_profile.html',context=mydict)

@login_required(login_url='login')
def incredecre(request, id):
    cart = Cart.objects.get(user=request.user)
    if request.GET.get('action') == "incre":
        myli = json.loads((str(cart.product)).replace("'", '"'))
        myli['objects'][0][str(id)] = myli['objects'][0].get(str(id), 0) + 1
    if request.GET.get('action') == "decre":
        myli = json.loads((str(cart.product)).replace("'", '"'))
        if myli['objects'][0][str(id)] == 1:
            del myli['objects'][0][str(id)]
        else:
            myli['objects'][0][str(id)] = myli['objects'][0].get(str(id), 0) - 1
    cart.product = myli
    cart.save()
    return redirect('view_cart')

@login_required(login_url='login')
def customer_address_view(request):
    # this is for checking whether product is present in cart or not
    # if there is no product in cart we will not show address form
    product_in_cart=False
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        if product_ids != "":
            product_in_cart=True
    #for counter in cart
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=0

    addressForm = AddressForm()
    if request.method == 'POST':
        addressForm = AddressForm(request.POST)
        if addressForm.is_valid():
            # here we are taking address, email, mobile at time of order placement
            # we are not taking it from customer account table because
            # these thing can be changes
            email = addressForm.cleaned_data['Email']
            mobile=addressForm.cleaned_data['Mobile']
            address = addressForm.cleaned_data['Address']
            #for showing total price on payment page.....accessing id from cookies then fetching  price of product from db
            total=0
            if 'product_ids' in request.COOKIES:
                product_ids = request.COOKIES['product_ids']
                if product_ids != "":
                    product_id_in_cart=product_ids.split('|')
                    products=models.Product.objects.all().filter(id__in = product_id_in_cart)
                    for p in products:
                        total=total+p.price

            response = render(request, 'payment.html',{'total':total})
            response.set_cookie('email',email)
            response.set_cookie('mobile',mobile)
            response.set_cookie('address',address)
            return response
    return render(request,'user_address.html',{'addressForm':addressForm,'product_in_cart':product_in_cart,'product_count_in_cart':product_count_in_cart})

# @login_required(login_url='customerlogin')
# def payment_success_view(request):
#     # Here we will place order | after successful payment
#     # we will fetch customer  mobile, address, Email
#     # we will fetch product id from cookies then respective details from db
#     # then we will create order objects and store in db
#     # after that we will delete cookies because after order placed...cart should be empty
#     # customer=UserProfile.objects.get(user_id=request.user.id)
#     products=None
#     email=None
#     mobile=None
#     address=None
#     if 'product_ids' in request.COOKIES:
#         product_ids = request.COOKIES['product_ids']
#         if product_ids != "":
#             product_id_in_cart=product_ids.split('|')
#             products=models.Product.objects.all().filter(id__in = product_id_in_cart)
#             # Here we get products list that will be ordered by one customer at a time

#     # these things can be change so accessing at the time of order...
#     if 'email' in request.COOKIES:
#         email=request.COOKIES['email']
#     if 'mobile' in request.COOKIES:
#         mobile=request.COOKIES['mobile']
#     if 'address' in request.COOKIES:
#         address=request.COOKIES['address']

#     # here we are placing number of orders as much there is a products
#     # suppose if we have 5 items in cart and we place order....so 5 rows will be created in orders table
#     # there will be lot of redundant data in orders table...but its become more complicated if we normalize it
#     for product in products:
#         Order.objects.get_or_create(customer=customer,product=product,status='Pending',email=email,mobile=mobile,address=address)

#     # after order placed cookies should be deleted
#     response = render(request,'payment_success.html')
#     response.delete_cookie('product_ids')
#     response.delete_cookie('email')
#     response.delete_cookie('mobile')
#     response.delete_cookie('address')
#     return response




# @login_required(login_url='customerlogin')
# def my_order_view(request):
#     # customer=UserProfile.objects.get(user_id=request.user.id)
#     # orders=Order.objects.all().filter(customer_id = customer)
#     ordered_products=[]
#     for order in orders:
#         ordered_product=Items.objects.all().filter(id=order.items.id)
#         ordered_products.append(ordered_product)

#     return render(request,'my_order.html',{'data':zip(ordered_products,orders)})
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('phone_number')
        company_name = request.POST.get('company_name')
        message = request.POST.get('message')
        Contact.objects.create(name=name,email=email,number=number,company_name=company_name,message=message)
        return redirect('navbar')
    return render(request,'contact.html')


def orders(req):
     return render(req,'orders.html',{'categories': categories})

def order_status(req):
     return render(req,'order_status.html',{'categories': categories})

def reward(req):
     return render(req,"under_Maintaince.html",{'categories': categories})

def offers(req):
     return render(req,"under_Maintaince.html",{'categories': categories})

def subscribe(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        Subscribe.objects.create(name=name,email=email)
        messages.info(request, "Thanks for subscribing")
        return redirect('navbar')
    return render(request,'Home.html')