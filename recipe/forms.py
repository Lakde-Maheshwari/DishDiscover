from django import forms
from .models import Recipes
from .models import Comments
class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipes
        fields = ['title', 'desc', 'Ingredients', 'instructions', 'recipe_img']

        labels = {
            'title': 'Recipe Title',
            'desc' : 'Describe your recipe',
            'Ingredients': 'Ingredients',
            'instructions': 'Instructions',
        }

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)

        
        self.fields['title'].widget.attrs.update({
            'class': 'border border-gray-300 rounded-lg p-3 w-full focus:outline-none focus:ring-2 focus:ring-green-500','text':'black',
            'placeholder': 'Enter the recipe title',
        })
        
        self.fields['desc'].widget.attrs.update({
            'class': 'border border-gray-300 rounded-lg p-3 w-full focus:outline-none focus:ring-2 focus:ring-green-500',
            'placeholder': 'Enter the recipe description',
        })
        
        self.fields['Ingredients'].widget.attrs.update({
            'class': 'border border-gray-300 rounded-lg p-2 w-full focus:outline-none focus:ring-2 focus:ring-green-500 h-24 resize-none',  # Set height and disable resizing
            'placeholder': 'List the ingredients',
            'rows': 2,  
        })

        
        self.fields['instructions'].widget.attrs.update({
            'class': 'border border-gray-300 rounded-lg p-2 w-full focus:outline-none focus:ring-2 focus:ring-green-500 h-32 resize-none',  # Set height and disable resizing
            'placeholder': 'Enter cooking instructions',
            'rows': 4,  
        })

        
        self.fields['recipe_img'].widget.attrs.update({
            'class': 'border border-gray-300 rounded-lg p-2 w-full focus:outline-none focus:ring-2 focus:ring-green-500',
        })


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['content'] 