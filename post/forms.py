from django import forms

from post.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['caption', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['caption'].widget.attrs.update({
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Write a caption...'
        })

        self.fields['image'].widget.attrs.update({
            'id': 'id_image'
        })


