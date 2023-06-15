from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from projects.forms import ProjectModelForm ,CommentModelForm,ReportCommentModelForm
from projects.models import Comment, Donation, Project,ReportComment
# from django.contrib.auth.decorators import login_required


# Create your views here.
# ============================(start projects)===================
class AllProjects(ListView):
    model = Project
    template_name = 'project_list.html'

class ProjectDetailedView(DetailView):
    model = Project
    template_name = 'project_detail.html'

class ProjectCreateView(CreateView):
    model = Project
    template_name = 'create_project.html'
    form_class = ProjectModelForm
    success_url = '/projects/'

class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'update_project.html'
    form_class = ProjectModelForm
    success_url = '/projects/'


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'delete_project.html'
    success_url = '/projects/'

# def ProjectDeleteView(request,id):
#     allProducts=Project.objects.get(id=id)
#     # allProducts=get_list_or_404(products,pk=id)
#     if allProducts: 
#         return render(request, 'delete_project.html',context={'list':allProducts})
# ============================(End projects)===================
# ============================(start add comment)==============
# class CommentCreate(CreateView):
#     comment = get_object_or_404(Project, pk=id)
#     model = Comment
#     fields = ['text',]
#     template_name = 'create_project.html'
   
    
#     def get_queryset(self):
#         """ Exclude any unpublished questions. """
#         id = self.get_object().id
#         # put remaining code here


   
# ============================(donate)=================================

def donate(request, id):
    project = get_object_or_404(Project, pk=id)
    if request.method == 'POST':
        amount = request.POST.get('amount')
        donation = Donation(project=project, user=request.user, amount=amount)
        donation.save()
        return redirect('detail', id=project.id)
    return render(request, 'project_detail.html', {'project': project})



def add_comment(request,pk):
    eachproject=Project.objects.get(id=pk)
    form=CommentModelForm(instance=eachproject)
    if request.method == 'POST':
        form = CommentModelForm(request.POST, instance=eachproject)
        if form.is_valid():
            name = request.user.username
            body = form.cleaned_data['comment_body']
            c = Comment(project =eachproject, commenter_name=name, comment_body=body)
            c.save()
            return redirect('allprojects') 
        else:
            print('form is invalid')
    else:
        context={
        'form': form}
    return render(request, 'add-comment.html',context )  


def delete_comment(request,pk):
    # get all comment based on project
    comment =Comment.objects.filter(project=pk).last()
    product_id = comment.project.id
    comment.delete()
    return redirect(reverse('detail', args=[product_id]))




def report_comment(request,pk):
    eachproject=Project.objects.get(id=pk)
    print(eachproject,"kemooooo")
    form=ReportCommentModelForm(instance=eachproject)
    if request.method == 'POST':
        form = ReportCommentModelForm(request.POST, instance=eachproject)
        if form.is_valid():
            name = request.user.username
            # report=request.POST.get('boolean_field')
            # print(report)
            field = form.cleaned_data['boolean_field']
            r = ReportComment(boolean_field=field,user_id=name,project=eachproject)
            r.save()
            return redirect('allprojects') 
        else:
            print('form is invalid')
    else:
        context={
        'form': form,
        'eachproject':eachproject
        }
    return render(request, 'report.html',context )  
