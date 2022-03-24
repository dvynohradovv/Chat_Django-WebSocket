from django.contrib.auth import login, logout
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import FormView, View, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import LoginForm, ChatRoomForm
from .models import User, Chatroom


def logout_view(request):
    logout(request)
    return redirect(reverse("login"))


class LoginView(View):
    login_text = "Please, LOG IN and input your password"
    signin_text = "Please, SIGN IN and set new password"

    def get(self, request):
        form = LoginForm()
        context = {"form": form}
        username = request.GET.get("username", None)

        if username:
            context.update({"method": "post", "username": username})
            is_user = User.objects.filter(username=username).exists()
            context["submit_text"] = self.login_text if is_user else self.signin_text

        else:
            context["method"] = "get"

        return render(request, 'chat/login.html', context)

    def post(self, request):
        username = request.GET.get("username", None)
        password = request.POST.get("password", None)

        form = LoginForm({"username": username, "password": password})
        context = {"form": form, "method": "post", "username": username}

        if form.is_valid():
            user, created = User.objects.get_or_create(username=username)

            if created:
                user.set_password(password)
                user.save()
                login(request, user)

            elif not user.check_password(password):
                context["submit_text"] = "Wrong password!"
                return render(request, 'chat/login.html', context)

            login(request, user)

            return redirect(reverse("index"))

        context["validation_error"] = form.errors
        return render(request, 'chat/login.html', context)


class IndexView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = request.user
        form = ChatRoomForm()
        context = {
            'username': user.username,
            'form': form
        }
        return render(request, 'chat/index.html', context)

    def post(self, request):
        user = request.user
        form = ChatRoomForm(request.POST)
        if form.is_valid():
            print("valid form")
            chatroom = form.save()
            chatroom.creator = user
            chatroom.save()
            return redirect(reverse("index", args=[chatroom.name]))
        context = {
            'username': user.username,
            'form': form
        }
        print("invalid form")
        return render(request, 'chat/index.html', context)


class ChatRoomView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = request.user
        room_name = kwargs["room_name"]

        has_invite = user.chatroom_invitations.filter(name=room_name).exists()
        is_creator = user.created_chatrooms.filter(name=room_name).exists()
        if not has_invite and not is_creator:
            return HttpResponseBadRequest("You have no access!")

        context = {
            'room_name': room_name,
            'username': user.username,
        }
        return render(request, 'chat/room.html', context)


class ChatRoomCreateView(CreateView):
    model = Chatroom
