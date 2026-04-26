from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.contrib import messages
from .models import Message
from .forms import MessageForm


class InboxView(LoginRequiredMixin, ListView):
    template_name = 'messaging/inbox.html'
    context_object_name = 'messages_list'

    def get_queryset(self):
        return Message.objects.filter(receiver=self.request.user).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['unread_count'] = Message.objects.filter(
            receiver=self.request.user, read=False
        ).count()
        return context


class SentView(LoginRequiredMixin, ListView):
    template_name = 'messaging/sent.html'
    context_object_name = 'messages_list'

    def get_queryset(self):
        return Message.objects.filter(sender=self.request.user).order_by('-created_at')


@login_required
def message_detail_view(request, pk):
    message = get_object_or_404(Message, pk=pk)
    if message.receiver != request.user and message.sender != request.user:
        messages.error(request, 'No tenés permiso para ver este mensaje.')
        return redirect('messaging:inbox')
    if message.receiver == request.user and not message.read:
        message.read = True
        message.save()
    return render(request, 'messaging/detail.html', {'message': message})


@login_required
def compose_view(request, receiver_id=None):
    initial = {}
    if receiver_id:
        from django.contrib.auth.models import User
        receiver = get_object_or_404(User, pk=receiver_id)
        initial['receiver'] = receiver

    if request.method == 'POST':
        form = MessageForm(request.POST, current_user=request.user)
        if form.is_valid():
            msg = form.save(commit=False)
            msg.sender = request.user
            msg.save()
            messages.success(request, f'Mensaje enviado a {msg.receiver.username}.')
            return redirect('messaging:sent')
    else:
        form = MessageForm(current_user=request.user, initial=initial)

    return render(request, 'messaging/compose.html', {'form': form})
