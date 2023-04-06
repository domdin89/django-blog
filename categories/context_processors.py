from .models import Category

def get_categories(request):
    return {'category': Category.objects.all().order_by('?')}