from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def login_view(request):
    error = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            error = 'ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง'
    return render(request, 'myapp/login.html', {'error': error})

def register(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if not username or not password1 or not password2:
            error = "กรุณากรอกข้อมูลให้ครบ"
        elif password1 != password2:
            error = "รหัสผ่านไม่ตรงกัน"
        elif User.objects.filter(username=username).exists():
            error = "ชื่อผู้ใช้นี้ถูกใช้แล้ว"
        else:
            User.objects.create_user(username=username, password=password1)
            messages.success(request, "สมัครสมาชิกสำเร็จ! กรุณาเข้าสู่ระบบ")
            return redirect('login')
    return render(request, 'register.html', {'error': error})

# บังคับล็อกอินก่อนเข้าหน้าเหล่านี้
@login_required(login_url='login')
def home(request):
    return render(request, 'myapp/home.html')

def menu(request):
    return render(request, 'myapp/menu.html')

from django.conf import settings

def delivery(request):
    return render(request, 'myapp/delivery.html', {
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY
    })

def trackorder(request):
    return render(request, 'myapp/trackorder.html')

@login_required
def order_status(request):
    customer_name = request.user.get_full_name() or request.user.username

    order_items = [
        {
            'name': 'มาการองรสสตรอว์เบอร์รี่',
            'quantity': 2,
            'price': 60,
            'image_url': 'https://i.imgur.com/1.png',
        },
        {
            'name': 'ชาเขียวมัทฉะเย็น',
            'quantity': 1,
            'price': 55,
            'image_url': 'https://i.imgur.com/2.png',
        },
        {
            'name': 'พุดดิ้งชานมไข่มุก',
            'quantity': 1,
            'price': 45,
            'image_url': 'https://i.imgur.com/3.png',
        },
    ]

    total_price = sum(item['quantity'] * item['price'] for item in order_items)

    return render(request, 'myapp/order_status.html', {
        'customer_name': customer_name,
        'order_items': order_items,
        'total_price': total_price,
    })
