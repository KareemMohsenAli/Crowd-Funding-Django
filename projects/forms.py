
from django import forms
from projects.models import Comment, Project,ReportComment


class ProjectModelForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

# ========================(start comment form)=========================================

class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        # fields = '__all__'
        # fields = ['text',]
        fields = ('comment_body',)


class ReportCommentModelForm(forms.ModelForm):
    class Meta:
        model = ReportComment
        # fields = '__all__'
        # fields = ['text',]
        fields = ('boolean_field',)
