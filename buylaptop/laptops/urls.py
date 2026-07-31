from django.urls import path
from . import views

urlpatterns = [
    # 🏠 Home
    path('', views.home, name='home'),

    # 💻 All laptops (search + category filter inside)
    path('all-laptops/', views.all_laptops_view, name='all_laptops'),

    # 🏷️ Brand
    path('brand/<int:id>/', views.brand_view, name='brand'),

    # 📂 Category
    path('category/<int:id>/', views.category_laptops, name='category_laptops'),

    # 🔍 Search (optional but useful)
    path('search/', views.search_laptops, name='search'),

    # 📊 Compare
    path('compare/', views.compare_page, name='compare'),

    # 💳 EMI
    path('emi/', views.emi_calculator, name='emi'),

    # 📩 About
    path('about/', views.about, name='about'),

    # ⭐ Review
    path('submit-review/', views.submit_review, name='submit_review'),

    # 🛠️ Accessories
    path('accessories/', views.accessories_view, name='accessories'),
]