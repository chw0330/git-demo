from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["author", "title", "content"]
        labels = {
            "author": "昵称",
            "title": "标题",
            "content": "内容",
        }
        widgets = {
            "author": forms.TextInput(
                attrs={"placeholder": "你的昵称", "autocomplete": "name"}
            ),
            "title": forms.TextInput(attrs={"placeholder": "一句话标题"}),
            "content": forms.Textarea(
                attrs={"placeholder": "写点想分享的内容", "rows": 6}
            ),
        }
