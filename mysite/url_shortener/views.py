from django.shortcuts import render, redirect
from django.db.models import Max
from .models import Url



def shorten_url(request):
    if request.method == 'POST':
        long_url = request.POST.get('long_url')

        # check if the long_url existed or not, if True, then return the short_url from DB
        url = Url.objects.filter(long_url=long_url).first()
        if url:
            return render(request, 'shorten.html', {'short_url': url.short_url})

        # if not existed, produce a new one and return it
        short_url = get_short_url()
        url = Url(long_url=long_url, short_url=short_url)
        url.save()
        return render(request, 'shorten.html', {'short_url': short_url})
    return render(request, 'shorten.html')


def get_short_url():
    
    max_id = Url.objects.all().aggregate(max_id=Max("id"))['max_id']
    num = 0 if not max_id else max_id 
    
    alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if num == 0: return '0'
    n = len(alphabet)
    digits = []
    
    while num > 0:
        rem = num % n
        digits.append(alphabet[rem])
        num //= n
        
    return ''.join(reversed(digits))


def redirect_url(request, short_url):
    try:
        url = Url.objects.get(short_url=short_url)
        
    
    except Url.DoesNotExist:
       
        return render(request, 'shorten.html',{'notExist': True}, status=404)
    
    return redirect(url.long_url)

    
