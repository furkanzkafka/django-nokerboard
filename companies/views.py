from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Company

def index(request):
    companies = Company.objects.order_by('-list_date').filter(is_listed=True)

    paginator = Paginator(companies, 3)
    page = request.GET.get('page')
    paged_companies = paginator.get_page(page)

    context = {
        'companies': companies
    }
    return render(request, 'companies/companies.html',context)

def company(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    context = {
        'company': company
    }
    return render(request, 'companies/company.html',context)

def search(request):
    return render(request, 'companies/search.html')