from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# ==============================(category)=============================================

class Category(models.Model):
    cat_title = models.CharField(max_length=255)
    cat_description = models.CharField(max_length=255)
    def __str__(self):
                return self.cat_title  
    # ==============================(project)=============================================

class Project(models.Model):
    title = models.CharField(max_length=255)
    details = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True,
                                 related_name='category_Project')
    images = models.ImageField(upload_to='projects/images')
    total_target = models.IntegerField()
    tags = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    
    def __str__(self):
            return self.title  
      
    def get_image_url(self):
        return f"/media/{self.images}"
    
# =======================(donation)==========================================

class Donation(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='donations')
    user = models.ForeignKey(User,null=True,on_delete=models.CASCADE,
                                 related_name='user')
    amount = models.IntegerField()
    
# ================================(comments)=================================================
class Comment(models.Model):
    text = models.TextField()
    ###############using on_delete beacuse when project is deleted also all comment that realted to it will also deleted
    project = models.ForeignKey(Project,related_name="comments", on_delete=models.CASCADE)
    commenter_name =models.CharField(max_length=200,null=True)
    # commenter_name=models.ForeignKey(User ,on_delete=models.CASCADE, null=True,related_name='cuser')
    comment_body = models.TextField(null=True)
    # created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.project.title,self.commenter_name)
    

class ReportComment(models.Model):
    project = models.ForeignKey(Project,related_name="commentrr", on_delete=models.CASCADE,null=True)
    user_id = models.TextField(null=True)
    boolean_field = models.BooleanField(default=True)

    



#  user_id = models.ForeignKey(User, on_delete=models.CASCADE)