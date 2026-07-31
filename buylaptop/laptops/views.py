from django.shortcuts import render, redirect, get_object_or_404
from .models import Comparison
from django.db.models import Q
from .models import Accessory
from .models import (
    Laptop, Brand, Category,
    Banner, ContactMessage,
    Review, Comparison
)

# =========================================
# 🏠 HOME PAGE
# =========================================
def home(request):
    laptops = Laptop.objects.order_by('-last_updated')[:15]
    comparisons = Comparison.objects.all()   # 🔥 ADD THIS

    featured_laptops = Laptop.objects.filter(is_featured=True).order_by('-last_updated')[:10]
    best_selling = Laptop.objects.filter(is_best_selling=True).order_by('-last_updated')[:5]

    brands = Brand.objects.all()
    categories = Category.objects.all()

    top_sliders = Banner.objects.filter(banner_type='top_slider')
    big_banner = Banner.objects.filter(banner_type='big_banner').first()
    carousel_banners = Banner.objects.filter(banner_type='carousel')

    reviews = Review.objects.all().order_by('-created_at')

    # ✅ ADD THIS BLOCK (MOST IMPORTANT)
    comparison_data = {}

    for laptop in laptops:
        comp = Comparison.objects.filter(laptop=laptop).first()

    comparison_data[laptop.id] = {
        "ram": comp.ram if comp else "N/A",
        "ssd": comp.ssd if comp else "N/A",
        "processor": comp.processor if comp else "N/A",
        "display": comp.display if comp else "N/A",
        "battery": comp.battery if comp else "N/A",
        "gpu": comp.gpu if comp else "N/A",
    }

    return render(request, 'home.html', {
        'laptops': laptops,
        'comparisons': comparisons,
        'featured_laptops': featured_laptops,
        'best_selling': best_selling,
        'brands': brands,
        'categories': categories,
        'top_sliders': top_sliders,
        'big_banner': big_banner,
        'carousel_banners': carousel_banners,
        'reviews': reviews,
        'comparison_data': comparison_data   # ✅ VERY IMPORTANT
    })


# =========================================
# 💻 ALL LAPTOPS (SEARCH + CATEGORY FILTER)
# =========================================
def all_laptops_view(request):
    laptops = Laptop.objects.all().order_by('-last_updated')

    query = request.GET.get('q')
    category_id = request.GET.get('category')

    comparisons = Comparison.objects.all()

    # 🔍 SEARCH
    if query:
        laptops = laptops.filter(
            Q(name__icontains=query) |
            Q(brand__name__icontains=query)
        )

    # 📂 CATEGORY FILTER
    category_name = None
    if category_id:
        category = get_object_or_404(Category, id=category_id)
        laptops = laptops.filter(category=category)
        category_name = category.name

    return render(request, 'all_laptops.html', {
        'laptops': laptops,
        'query': query,
        'category_name': category_name,
        'comparisons': comparisons
    })


# =========================================
# 📂 CATEGORY PAGE (USED BY HOME PAGE)
# =========================================
def category_laptops(request, id):
    category = get_object_or_404(Category, id=id)
    laptops = Laptop.objects.filter(category=category)

    return render(request, 'all_laptops.html', {
        'laptops': laptops,
        'category_name': category.name
    })


# =========================================
# 🏷️ BRAND PAGE
# =========================================
def brand_view(request, id):
    brand = get_object_or_404(Brand, id=id)
    laptops = Laptop.objects.filter(brand=brand)

    return render(request, 'brand.html', {
        'laptops': laptops,
        'brand': brand
    })


# =========================================
# 🔍 SEARCH PAGE (OPTIONAL)
# =========================================
def search_laptops(request):
    query = request.GET.get('q')

    laptops = Laptop.objects.all()

    if query:
        laptops = laptops.filter(
            Q(name__icontains=query) |
            Q(brand__name__icontains=query)
        )

    return render(request, 'all_laptops.html', {
        'laptops': laptops,
        'query': query
    })


# =========================================
# 📊 COMPARE PAGE
# =========================================
def compare_page(request):

    laptops = Comparison.objects.all()   # dropdown list

    l1 = None
    l2 = None

    if request.method == "POST":
        id1 = request.POST.get('laptop1')
        id2 = request.POST.get('laptop2')

        if id1 and id2:
            l1 = get_object_or_404(Comparison, id=id1)
            l2 = get_object_or_404(Comparison, id=id2)

    return render(request, 'compare.html', {
        'laptops': laptops,
        'l1': l1,
        'l2': l2
    })

# =========================================
# 📩 ABOUT / CONTACT
# =========================================
def about(request):
    if request.method == "POST":
        ContactMessage.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            message=request.POST.get('message')
        )

    return render(request, 'about.html')


# =========================================
# ⭐ SUBMIT REVIEW
# =========================================
def submit_review(request):
    if request.method == "POST":
        Review.objects.create(
            name=request.POST.get('name'),
            rating=request.POST.get('rating'),
            comment=request.POST.get('comment')
        )

    return redirect('home')


# =========================================
# 💳 EMI PAGE
# =========================================
def emi_calculator(request):
    return render(request, 'emi.html')


# =========================================
# 🛍️ ACCESSORIES PAGE
# =========================================


def accessories_view(request):
    accessories = Accessory.objects.all()

    selected_type = request.GET.get('type')

    if selected_type:
        accessories = accessories.filter(type=selected_type)

    return render(request, 'accessories.html', {
        'accessories': accessories,
        'selected_type': selected_type
    })