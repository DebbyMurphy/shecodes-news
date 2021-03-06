from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm
from django.db.models.functions import Trunc
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import CustomUser



class AddStoryView(LoginRequiredMixin, generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.order_by('-pub_date')[:4]
        context['all_stories'] = NewsStory.objects.order_by('-pub_date')[4:]
        return context


class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'


class AuthorsView(generic.ListView):
    template_name = 'news/authors.html'
    model = CustomUser
    context_object_name = "authors"

class AuthorProfileView(generic.DetailView):
    template_name = 'news/authorProfile.html'
    model = CustomUser
    context_object_name = "author"