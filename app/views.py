from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse


class TopPageView(View):
    def get(self, request):
        return HttpResponse("<h1>こんにちは</h1>")


class MyPageView(LoginRequiredMixin, View):
    def get(self, request):
        return HttpResponse(f"<h1>{request.user.username}さん こんにちは</h1>")
