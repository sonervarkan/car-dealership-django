from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from car_dealership_app.models import Car, Image
from django.http import JsonResponse

def index(request):
    
    cars=Car.objects.all()

    items=[]  

    for car in cars:
        images = Image.objects.filter(car=car)
        items.append({
            'car': car,
            'images': images
        })
    
    brands = Car.objects.values_list('brand', flat=True).distinct()

    return render(request, 'index.html', {'items': items, 'brands': brands})

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request, '/registraion/register.html', {'error': 'Bu kullanıcı adı zaten mevcut!'})

        User.objects.create_user(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            is_active=True,
            is_staff=False,
            is_superuser=False
        )
        return redirect('login')

    return render(request, 'registration/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            return render(request, 'registration/login.html', {'error': 'Kullanıcı adı veya şifre hatalı!'})

    return render(request, 'registration/login.html')


def logout(request):
    auth_logout(request)
    return redirect('index')

def add_car(request):
    
    if not request.user.is_authenticated:
        return redirect('login') 

    if request.method == "POST":
       
        brand = request.POST.get("brand")
        model = request.POST.get("model")
        gear_type = request.POST.get("gear_type")
        fuel_type = request.POST.get("fuel_type")
        year = request.POST.get("year")
        color = request.POST.get("color")
        price = request.POST.get("price")
        car_image_file = request.FILES.get("car_image")
        
        
        new_car = Car(
                brand=brand, 
                model=model, 
                gear_type=gear_type, 
                fuel_type=fuel_type, 
                year=year, 
                color=color, 
                price=price,
                user=request.user
            )
        new_car.save()
        
        if car_image_file:
                Image.objects.create(
                    car=new_car,          
                    img_url=car_image_file    
                )

        return redirect('index') 
    
    else:
        return render(request, 'add-car.html')

def get_models_by_brand(request):
    brand=request.GET.get('brand')
    models = list(Car.objects.filter(brand=brand).values_list('model', flat=True).distinct())
    return JsonResponse(models, safe=False)
    
def get_gear_type_by_model_brand(request):
    model=request.GET.get('model')
    brand=request.GET.get('brand')
    gear_types=list(Car.objects.filter(brand=brand, model=model).values_list('gear_type', flat=True).distinct())
    return JsonResponse(gear_types, safe=False)

def get_fuel_type_by_brand_model_gear_type(request):
    gear_type=request.GET.get("gear_type")
    brand=request.GET.get("brand")
    model=request.GET.get("model")
    fuel_types=list(Car.objects.filter(brand=brand, model=model, gear_type=gear_type).values_list("fuel_type", flat=True).distinct())
    return JsonResponse(fuel_types, safe=False)

def get_filter_results(request):
    brand = request.GET.get("brand")
    model = request.GET.get("model")
    gear_type = request.GET.get("gear_type")
    fuel_type = request.GET.get("fuel_type")
    year = request.GET.get("year")

    cars = Car.objects.filter(
        brand=brand,
        model=model,
        gear_type=gear_type,
        fuel_type=fuel_type,
        year=year
    )

    filter_cars = []
    for car in cars:
        images = Image.objects.filter(car=car)
        filter_cars.append({
            'car': car,
            'images': images 
        })

    return render(request, 'filter-results.html', {'filter_cars': filter_cars})
