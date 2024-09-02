from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from .forms import AddPostForm
from .models import Crypto, Network
from .utils import FormMixin


class CryptoHome(ListView):
    """
    Displays a list of published cryptocurrencies.

    This view retrieves all cryptocurrencies from the database that are marked as
    published and displays them with pagination.
    """

    template_name = 'crypto/index.html'
    context_object_name = 'posts'
    extra_context = {'title': 'Main page', 'network_selected': 0}
    paginate_by = 5

    def get_queryset(self):
        # Get access to all published cryptocurrencies using the greedy data download
        return Crypto.published.all().prefetch_related('networks')


class CryptoNetwork(ListView):
    """
    Displays a paginated list of published cryptocurrencies filtered by the selected network.

    This view retrieves all published cryptocurrencies from the database, filtered by the
    network specified via the `slug` parameter in the URL.
    """

    template_name = 'crypto/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        # Add the page title in the form of the selected network, and also transmit the selected network
        context = super().get_context_data(**kwargs)
        networks = Network.objects.get(slug=self.kwargs['net_slug'])
        context['title'], context['network_selected'] = f'Network: {networks}', networks.pk
        return context

    def get_queryset(self):
        # Get access to all published cryptocurrencies using network field filtering and greedy data download
        return Crypto.published.filter(networks__slug=self.kwargs['net_slug']).prefetch_related('networks')


class ShowPost(DetailView):
    """
    Displays the published cryptocurrency.

    This view extracts the cryptocurrency from the database by the slug field, which is marked as
    published, and displays it.
    """

    model = Crypto
    template_name = 'crypto/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        # Add the title of the page in the form of the selected cryptocurrency
        context = super().get_context_data(**kwargs)
        context['title'] = context['post'].title
        return context

    def get_object(self, queryset=None):
        # Get access to the published cryptocurrency or get a 404 error
        return get_object_or_404(Crypto.published, slug=self.kwargs[self.slug_url_kwarg])


class AddPage(FormMixin, LoginRequiredMixin, CreateView):
    """
    Creates a new cryptocurrency.

    This view allows authorized users to add a new cryptocurrency to the database.
    Access is restricted to logged-in users.

    Permissions:
        - Access is restricted to authenticated users only.

    Notes:
        - The form's title will be converted to lowercase by FormMixin.
    """

    form_class = AddPostForm
    template_name = 'crypto/addpage.html'
    success_url = reverse_lazy('home')
    extra_context = {'title': 'Add the post'}


class UpdatePage(FormMixin, LoginRequiredMixin, UpdateView):
    """
    Updates the cryptocurrency.

    This view allows authorized users to update the cryptocurrency to the database.
    Access is restricted to logged-in users.

    Permissions:
        - Access is restricted to authenticated users only.

    Notes:
        - The form's title will be converted to lowercase by FormMixin.
    """

    model = Crypto
    fields = ['title', 'content', 'is_published']
    template_name = 'crypto/editpage.html'
    success_url = reverse_lazy('home')
    extra_context = {'title': 'Editing the post'}


class DeletePage(LoginRequiredMixin, DeleteView):
    """
    Deletes the cryptocurrency.

    This view allows authorized users to delete cryptocurrency from the database.
    Access is restricted to registered users.

    Permissions:
        - Access is restricted only to authenticated users.
    """

    model = Crypto
    success_url = reverse_lazy('home')
    template_name = 'crypto/deletepage.html'
    extra_context = {'title': 'Deleting the post'}


class AboutPage(TemplateView):
    """
    Displays information about the site.
    """

    template_name = 'crypto/about.html'
    extra_context = {'title': 'About the site'}


class ContactPage(TemplateView):
    """
    Displays the contacts of the website developer.
    """

    template_name = 'crypto/contact.html'
    extra_context = {'title': 'Contact'}


class SearchPost(DetailView):
    """
    Searches the cryptocurrency.

    This view extracts the cryptocurrency from the database by the title field, which is marked as
    published, and displays it.
    """

    model = Crypto
    template_name = 'crypto/post.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        # The form's title will be converted to lowercase and get access to the published cryptocurrency
        # or get a 404 error message
        title = self.request.GET['search'].lower()
        return get_object_or_404(Crypto.published, title=title)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
