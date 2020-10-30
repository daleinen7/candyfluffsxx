from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from .models import Product
# from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm

# Create your views here.
def home(request):
    context = {'title': 'Candy Fluffs!', 'products': Product.objects.all()}
    return render(request, 'home.html', context)

def necahual(request):
    value = 'Necahual'
    product_list = Product.objects.filter(fandom='N')
    context = {
        'title': 'Candy Fluffs!', 
        'products':product_list
    }
    print(context)
    return render(request, 'necahual.html', context)

class ProductsList(ListView):
    model = Product
    template = 'product_list.html'

class ProductDetail(DetailView):
    model = Product
    template = 'product_detail.html'

def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = SignUpForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            user.refresh_from_db()
            user.profile.billing_address = form.cleaned_data.get('billing_address')
            user.profile.default_shipping_address = form.cleaned_data.get('default_shipping_address')
            user.profile.country = form.cleaned_data.get('country')
            user.profile.phone = form.cleaned_data.get('phone')
            user.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = SignUpForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)