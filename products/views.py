from django.shortcuts import render
from .models import Property
from django.core.paginator import Paginator

# def property_list(request):
#     property_list = Property.objects.filter(is_published=True).order_by('-list_date')
#     paginator = Paginator(property_list, 6) # Show 6 per page
    
#     page_number = request.GET.get('page')
#     properties = paginator.get_page(page_number)
#     return render(request, 'products/list.html', {'properties': properties})


from django.shortcuts import render, get_object_or_404
from .models import Property

def property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)
    return render(request, 'products/detail.html', {'property': property})


def property_list(request):
    queryset = Property.objects.filter(is_published=True).order_by('-list_date')

    # Keyword Filter
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            queryset = queryset.filter(title__icontains=keyword) | queryset.filter(location__icontains=keyword)

    # Category Filter
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            queryset = queryset.filter(category=category)

    # Price Filter
    if 'max_price' in request.GET:
        max_price = request.GET['max_price']
        if max_price:
            queryset = queryset.filter(price__lte=max_price)

    context = {
        'properties': queryset
    }
    return render(request, 'products/list.html', context)