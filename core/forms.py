from django import forms

from .models import Post, Tag


class PostForm(forms.ModelForm):
    tags = forms.CharField(max_length=255)

    class Meta:
        model = Post
        fields = ['title', 'body']

    def cleaned_tags(self):
        data = list()
        tags = self.cleaned_data['tags']
        for tag in tags.split():
            tag_title = Tag.objects.get_or_create(
                title=tag
            )
            data.append(tag_title)

        return data

    def save(self, commit=True):
        post = super().save(commit=True)
        for title in self.cleaned_data['tags'].split():
            tag, created = Tag.objects.get_or_create(
                title=title
            )
            post.tags.add(tag)
        return super().save(commit=True)


