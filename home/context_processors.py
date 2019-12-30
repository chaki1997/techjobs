
from profile_wizard import models



def bar(request):
    context={}
    if request.user.is_authenticated:
        context['user'] = request.user
        profile_ee = models.EmployeeProfileModel.objects.filter(user=request.user)
        if profile_ee:
            context['profile_ee'] = profile_ee[0].id

        company_obj = models.Company.objects.filter(user=request.user)

        is_company = False

        if company_obj:
            is_company = True
            print(is_company)
            context['is_company'] = is_company
        #print(company)
        if request.user.status == 'Employer':
            company_obj = models.Company.objects.filter(user=request.user)
            if company_obj:
                company_id = company_obj[0].id
                print(company_obj)
                print(company_id)
                context['company_id'] = company_id
    #print(request.user.id)
    return context