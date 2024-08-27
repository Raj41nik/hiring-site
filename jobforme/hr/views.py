from django.shortcuts import render,redirect
from hr.models import JobPost,CandidateApplication,selectCandidateJob,Hr
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def hrHome(request):
    if Hr.objects.filter(user=request.user).exists():
        jobpost=JobPost.objects.filter(user=request.user)
        # print(jobpost)
        return render(request,'hr/hrDashBoard.html',{'jobpost':jobpost})
    return redirect('candidate_dashboard')

@login_required
def post_job(request):
    msg = None
    if request.method =="POST":
        job_title=request.POST.get('job-title')
        address=request.POST.get('address')
        company_name=request.POST.get('company-name')
        salary_low=request.POST.get('salary-low')
        salary_high=request.POST.get('salary-high')
        last_date=request.POST.get('last-date')
        msg='Job added successfully'
        
        job_post= JobPost(user=request.user,titile=job_title,address=address,companyName=company_name,salaryLow=salary_low,salaryHigh=salary_high,lastDateApply=last_date)
        job_post.save()
          
    return render(request,'hr/postjob.html',{'msg':msg})
@login_required
def candidate_view(request,pk):
    if JobPost.objects.filter(id=pk).exists():
        job =JobPost.objects.get(id=pk)
        applications=CandidateApplication.objects.filter(job=job)
        selectedApplication=selectCandidateJob.objects.filter(job=job)
        return render(request,'hr/candidate.html',{'applications':applications,'selectedApplication':selectedApplication,'jobpost':job})
    
    return redirect('hrdash')

@login_required
def selectCandidate(request):
    if request.method =='POST':
        candidateID=request.POST.get('candidateid')
        jobID=request.POST.get('jobpostid')
        job=JobPost.objects.get(id=jobID)
        candidate=CandidateApplication.objects.get(id=candidateID)
        selectCandidateJob(job=job,candidate=candidate)
    return redirect('hrdash')

@login_required
def deleteCandidate(request):
    if request.method =='POST':
        candidateID=request.POST.get('candidateid')
        jobID=request.POST.get('jobpostid')
        job=JobPost.objects.get(id=jobID)
        candidate=CandidateApplication.objects.get(id=candidateID).delete()
        job.applyCount =job.applyCount-1
    return redirect('hrdash')