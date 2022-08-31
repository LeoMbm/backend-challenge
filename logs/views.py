from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render

from logs.models import Logs


# Create your views here.
@login_required(login_url='/users/login')
def getIpData(request):
    ip_list = Logs.objects.all()
    paginator = Paginator(ip_list, 30)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    return render(request, 'IpResults.html', {'obj': page_obj})