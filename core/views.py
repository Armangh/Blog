from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import generic
from django.urls import reverse_lazy

from . import models
from .forms import PostForm


# create post: /post/create/ name: create_post
class CreatePost(LoginRequiredMixin, generic.CreateView):
    model = models.Post
    template_name = "post/create.html"
    form_class = PostForm
    success_url = reverse_lazy('main_page')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# detail post: /post/1/ name: detail_post
class DetailPost(DetailView):
    model = models.Post
    template_name = "post/detail.html"


# delete post: /post/delete/1/ name:delete_post
class DeletePost(LoginRequiredMixin, generic.DeleteView):
    model = models.Post
    template_name = "post/delete.html"
    success_url = reverse_lazy('main_page')


# create comment: /post/1/comment/ name: create_comment
class CreateComment(generic.View):
    def post(self, request, *args, **kwargs):
        post = get_object_or_404(models.Post, pk=kwargs['pk'])
        models.Comment.objects.create(
            body=request.POST['body'],
            post=post)
        return redirect(
            reverse_lazy('detail_post', kwargs={'pk': kwargs['pk']}))


# create tag
class CreateTag(LoginRequiredMixin, generic.CreateView):
    model = models.Tag
    fields = ['title']
    template_name = "tag/create.html"
    success_url = reverse_lazy('main_page')


class DeleteTag(LoginRequiredMixin, generic.DeleteView):
    model = models.Tag
    template_name = "tag/delete.html"
    success_url = reverse_lazy('main_page')

class DetailTag(DetailView):
    model = models.Tag
    template_name = "tag/detail.html"


class MainPage(ListView):
    template_name = "index.html"
    model = models.Post

    def get_context_data(self, *args, **kwargs):
        context = super(MainPage, self).get_context_data(*args, **kwargs)
        context.update({
            'tags': models.Tag.objects.all(),
        })
        return context

    def get_queryset(self):
        return self.model.objects.order_by('-create_date')
