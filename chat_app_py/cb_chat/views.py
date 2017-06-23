from django.contrib.auth.models import User
from cb_chat.models import Message
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    else:
        form = UserCreationForm()
    return render(request, 'registration/registration_form.html', {'form': form})


@login_required(login_url="/accounts/login/")
def root(request):
    return redirect("home")


@login_required(login_url="/accounts/login/")
def home(request, frnd_id=None):
    offset = 0
    me = request.user
    chat_rooms = list(User.objects.all())
    chat_rooms.remove(me)
    context = {}
    context['chat_rooms'] = chat_rooms
    if frnd_id:
        messages = Message.objects.filter(Q(reciever=me, sender=frnd_id) | Q(sender=me, reciever=frnd_id))
        context["messages"] = messages
        context["frnd_id"] = frnd_id
    return render(request, "pk_chat/chat_window.html", context)


@csrf_exempt
def send(request):
    p = request.POST
    user = User.objects.get(id=p['room'])
    Message.objects.create(message=p['text'], sender=request.user, reciever=user)
    return HttpResponse("")