from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.db.models import Q
from .models import Page
from .forms import PageForm


class AuthorOrAdminMixin(LoginRequiredMixin):
    """Permite acceso solo al autor del objeto o a staff/superusuarios."""

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        obj = self.get_object()
        if obj.author != request.user and not request.user.is_staff:
            raise PermissionDenied
        return response


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_pages'] = Page.objects.order_by('-created_at')[:3]
        return context


class AboutView(TemplateView):
    template_name = 'about.html'


class PageListView(ListView):
    model = Page
    template_name = 'pages/list.html'
    context_object_name = 'pages'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q', '').strip()
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(subtitle__icontains=query) | Q(content__icontains=query)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context


class PageDetailView(DetailView):
    model = Page
    template_name = 'pages/detail.html'
    context_object_name = 'page'


class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    form_class = PageForm
    template_name = 'pages/form.html'
    success_url = reverse_lazy('pages:list')
    extra_context = {'action': 'Crear', 'title': 'Nueva Página'}

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Página creada exitosamente.')
        return super().form_valid(form)


class PageUpdateView(AuthorOrAdminMixin, UpdateView):
    model = Page
    form_class = PageForm
    template_name = 'pages/form.html'
    extra_context = {'action': 'Guardar cambios', 'title': 'Editar Página'}

    def get_success_url(self):
        return reverse_lazy('pages:detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        messages.success(self.request, 'Página actualizada exitosamente.')
        return super().form_valid(form)


@login_required
def page_delete(request, pk):
    page = get_object_or_404(Page, pk=pk)
    if page.author != request.user and not request.user.is_staff:
        raise PermissionDenied
    if request.method == 'POST':
        page.delete()
        messages.success(request, 'Página eliminada exitosamente.')
        return redirect('pages:list')
    return render(request, 'pages/confirm_delete.html', {'page': page})
