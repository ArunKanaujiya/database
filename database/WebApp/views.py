from django.shortcuts import render,redirect
from WebApp.forms import StudForm
# Create your views here.

def home(request):
    form=StudForm(request.POST)
    if form.is_valid():
        form.save()
        print(form)
        return redirect('/')
    context={'form':form}
    return render(request,'myapp/forms.html',context)

