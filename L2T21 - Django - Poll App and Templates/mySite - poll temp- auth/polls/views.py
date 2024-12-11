
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login
from django import forms
from .models import Poll, Choice

# Create a registration form for new users
class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match!")

# Registration view
def register(request):
    """Handle user registration."""
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])  # Set the hashed password
            user.save()
            messages.success(request, 'Registration successful. You can now log in.')
            auth_login(request, user)  # Automatically log in the user after registration
            return redirect('polls:index')  # Redirect to polls index page
    else:
        form = UserRegistrationForm()
    return render(request, 'polls/register.html', {'form': form})

# Login view
def login_view(request):
    """Handle user login."""
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)  # Authenticate user
            if user is not None:
                auth_login(request, user)  # Log in the user
                messages.success(request, 'Login successful.')
                return redirect('polls:index')  # Redirect to polls index page
    else:
        form = AuthenticationForm()
    return render(request, 'polls/login.html', {'form': form})

# Index view to display all polls
def index(request):
    """Display all polls."""
    polls = Poll.objects.all()  # Fetch all polls from the database
    return render(request, 'polls/index.html', {'polls': polls})

# Detail view for a specific poll
def detail(request, poll_id):
    """Display details of a specific poll and its choices."""
    poll = get_object_or_404(Poll, pk=poll_id)  # Get poll or 404 if not found
    return render(request, 'polls/detail.html', {'poll': poll})

# Vote view to handle voting logic
@login_required
def vote(request, poll_id):
    """Handle the voting process for a specific poll."""
    poll = get_object_or_404(Poll, pk=poll_id)  # Get poll or 404 if not found

    if request.method == 'POST':
        selected_choice = request.POST.get('choice')  # Get selected choice from POST data
        choice = get_object_or_404(Choice, pk=selected_choice)  # Get choice or 404 if not found
        choice.votes += 1  # Increment the vote count
        choice.save()  # Save the updated choice
        messages.success(request, 'Your vote has been recorded!')  # Success message
        return redirect('polls:results', poll_id=poll.id)  # Redirect to results page

    return render(request, 'polls/vote.html', {'poll': poll})

# Results view to display voting results for a specific poll
def results(request, poll_id):
    """Display results of a specific poll."""
    poll = get_object_or_404(Poll, pk=poll_id)  # Get poll or 404 if not found
    return render(request, 'polls/results.html', {'poll': poll})
