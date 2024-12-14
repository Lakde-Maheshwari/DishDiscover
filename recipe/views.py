from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .forms import RecipeForm,CommentForm
from .models import Recipes,Comments

@login_required
def createpost(request):
    form = None
    if request.method == 'POST':
        form = RecipeForm(request.POST,request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('postsuccess') 
        else:
            print(form.errors) 
    else:
        form = RecipeForm()
    return render(request, 'createpost.html', {'form': form})

def postsuccess(request):
    return render(request,'postsuccess.html')

def recipe_list(request):
    recipe_list = Recipes.objects.all().order_by('-date_posted')
    return render(request, 'home.html', {'recipe_list': recipe_list})

def recipe_detail(request,id):
    recipe = Recipes.objects.get(id=id)
    comments = Comments.objects.filter(recipe_id=id).order_by('-date_posted')
    ingredients_list = recipe.Ingredients.split(',')
    instructions_list = recipe.instructions.split(',')

    context = {
        'recipe': recipe,
        'ingredients_list': ingredients_list,
        'instructions_list': instructions_list,
        'comments' :comments,
    }
    return render(request, 'detail.html', context)

@login_required
def recipe_edit(request,id):
    recipe = get_object_or_404(Recipes, id=id, author=request.user)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('home')
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'edit_recipes.html', {'form': form})

@login_required
def recipe_delete(request,id):
    recipe = get_object_or_404(Recipes,id = id,author = request.user)
    if request.method == 'POST':
        recipe.delete()
        return redirect('home')
    return render(request, 'recipe_confirm_delete.html', {'recipe': recipe})


def comment(request, recipe_id):
    recipe = get_object_or_404(Recipes, id=recipe_id)

    if request.method == 'POST':
        cform = CommentForm(request.POST)
        if not request.user.is_authenticated:
            return render(request, 'not_logged_in.html')

        if cform.is_valid():
            comment = cform.save(commit=False)
            comment.user = request.user
            comment.recipe = recipe
            comment.save()
            return redirect('recipe_detail', id=recipe.id) 
        else:
            print(cform.errors)
    else:
        cform = CommentForm()

    comments = Comments.objects.filter(recipe=recipe)  
    return render(request, 'detail.html', {'cform': cform, 'recipe': recipe, 'comments': comments})