from django.shortcuts import render
from django.http import HttpResponse
from .models import Collection, Piece
from django.views import generic
from .forms import UserForm
from django.contrib.auth import authenticate, login
from django.views.generic import View


class index(generic.ListView):
    template_name = 'genre/genretemplate.html'

    def get_queryset(self):
        return Collection.objects.all()


class details(generic.DetailView):
    model = Collection
    template_name = 'genre/detailtemplate.html'


"""class UserFormView(View):
    from_class = UserForm
    template_name = 'genre/template.html'


    def get(self, request):
        from=self.from_class(None)
        return render(request, self.template_name,{'form': forms})


    def post(self, request):
        form=self.from_class(request.post)


        if form.is_valid():
             user=form.save()
             username=form.cleaned_data('username')
             password=form.cleaned_data('password')
             user.set_password(password)
             user.save()


             newuser=authenticate(username=username, password=password)

             if newuser is not None:
                 if newuser.is_active:
                     login(request,newuser)
                     return redirect("/index")

        return render(request, self.template_name, {'form': form})"""










