from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # log the user in (optional, not implemented here)
            return redirect('articles:list')  # Replace with your redirect target
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})
