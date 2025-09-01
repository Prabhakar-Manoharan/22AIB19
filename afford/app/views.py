from django.shortcuts import render, redirect, get_object_or_404
from .models import URLShortener

def shorten_url(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        if url:
            obj = URLShortener.objects.create(original_url=url)
            short_url = request.build_absolute_uri(f'/{obj.short_code}/')
            return render(request, 'shorten_result.html', {'short_url': short_url})
    return render(request, 'shorten_form.html')

def redirect_short_url(request, code):
    obj = get_object_or_404(URLShortener, short_code=code)
    return redirect(obj.original_url)