from django.contrib import admin

# Register your models here.



# Register your models here.




from .models import FreeProfileWizard,\
    EduWizard,\
    EmloymentWizard,\
    PostJob,\
    Company,\
    EmployeeProfileModel

admin.site.register(FreeProfileWizard)

admin.site.register(EduWizard)
admin.site.register(EmloymentWizard)
admin.site.register(PostJob)
admin.site.register(Company)
admin.site.register(EmployeeProfileModel)


