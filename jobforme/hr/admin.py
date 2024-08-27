from django.contrib import admin
from hr import models
# Register your models here.

@admin.register(models.Hr)
class HrAdmin(admin.ModelAdmin):
    list_display=('id','user')
    
@admin.register(models.JobPost)
class JobPostAdmin(admin.ModelAdmin):
    list_display=('id','user','titile','address','companyName','salaryLow','salaryHigh','lastDateApply','applyCount')



@admin.register(models.CandidateApplication)
class CandidateApplicationAdmin(admin.ModelAdmin):
    list_display=('id','user','job')
    


@admin.register(models.selectCandidateJob)
class selectCandidateJobAdmin(admin.ModelAdmin):
    list_display=('id','job','candidate')