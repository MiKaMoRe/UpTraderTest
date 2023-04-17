from django.shortcuts import render
from django.views.generic import View
# from menu.models import Menu


class MenuView(View):
    def get(self, request, path=''):
        ctx = {'active_path': path}
        return render(request, 'menu/index.html', ctx)
