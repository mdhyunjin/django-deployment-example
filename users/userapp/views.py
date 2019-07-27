from django.shortcuts import render
from userapp.forms import NewUserForm

# Create your views here.
def index(request):
    return render(request,'userapp/index.html')

def new_user_form(request):
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Error Form Invalid!")

    return render(request, 'userapp/user.html', {'form':form})
