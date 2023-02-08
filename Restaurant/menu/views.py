# Create your views here.
from django.contrib import messages
from unicodedata import name
from django.shortcuts import render
from .models import Menu, Meal, MenuSection
from .forms import MealForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# function for rendering the homepage


def home(request):
    return render(request, "home.html")

# function for the validation of a meal form and adding new meals


@staff_member_required(login_url='login')
def addMeal(request):
    form = MealForm()
    if request.method == 'POST':
        form = MealForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/show')
        else:
            messages.info(request, "Invalid data")
    context = {'form': form}
    return render(request, 'index.html', context)

# function for showing menu with sections and meals


def showMenu(request):
    menusection = MenuSection.objects.all
    menu = Menu.objects.all
    return render(request, 'show.html', {'menu': menu, 'menusection': menusection})

# function for editing menu meals via the meal form previously used for adding


@staff_member_required(login_url='login')
def editMeal(request, id):
    meal = Meal.objects.get(id=id)
    form = MealForm(instance=meal)

    if request.method == 'POST':
        form = MealForm(request.POST, request.FILES, instance=meal)
        if form.is_valid():
            form.save()
            return redirect('/show')
    context = {'form': form}
    return render(request, 'index.html', context)

# function for meal deletion using the meal id


@staff_member_required(login_url='login')
def deleteMeal(request, id):
    meal = Meal.objects.get(id=id)
    meal.delete()
    return redirect('/show')

# function for searching the menu meals using the meal name


def searchMenu(request):
    searched_name = request.POST['name']
    menusection = MenuSection.objects.all
    menu = Menu.objects.filter(MealName__icontains=searched_name)
    return render(request, 'show.html', {'menu': menu, 'menusection': menusection})

# function for rendering menu objects to the filter.html page


@login_required(login_url='login')
def filterMenu(request):
    menu = Menu.objects.all
    return render(request, 'filter.html', {'menu': menu})
