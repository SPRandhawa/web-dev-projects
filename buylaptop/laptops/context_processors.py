from .models import Banner

def global_banner(request):
    return {
        'big_banner': Banner.objects.filter(banner_type='big_banner').first()
    }