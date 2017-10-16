from django import forms
from django.forms import ModelForm, TextInput
from .models import Post, Comment, Tag

class PostForm(forms.ModelForm):
    #print("> INFO, forms.py: Class definition")
    tags=""
    post_tags=""
    tag_selector=forms.CharField(initial=tags)

    def __init__(self, *args, **kwargs):
        #print("> INFO, forms.py: def __init__")
        super(PostForm, self).__init__(*args, **kwargs)
        #instance = super(PostForm, self).save(commit=commit)
        post_instance=self.instance
        global post_tags
        global tags
        post_tags=post_instance.tags.all()
        for tag in post_tags:
            tag=tag.name
            self.tags=self.tags + ", " + tag
        tags=self.tags[2:]
        print("> INFO, forms.py, inside __init__: " + tags)
        kwargs.update(initial={
            # 'field': 'value'
            'tag_selector': tags
        })
        super(PostForm, self).__init__(*args, **kwargs)

    class Meta:
        #print("> INFO, forms.py: class Meta")
        model = Post
        fields = ('title', 'text', 'tag_selector',)#'tags',)

        #widgets = {
            #'tags': TextInput,
        #}
    def clean_tag_selector(self):
         data = self.cleaned_data['tag_selector']
         # Check that data are corrects ie the string is correctly formatted
         # If not raise validation error
         tags = data.split(",")
         #Check that all tags are fruit or raise a validation error
         return tags

    def save(self, commit=True):
        instance = super(PostForm, self).save(commit=commit)
        #Borrem els Tags del Post
        instance.tags.clear()
        # Compare the list of tags fruit_tags with self.instance.fruit.all()
        # Take the right actions
        tags = self.cleaned_data.get('tag_selector', None)
        #tags = tags.split(",")
        for tag_el in tags:
            if not Tag.objects.filter(name=tag_el).exists():
                tag = Tag.objects.create(name=tag_el)
                instance.tags.add(tag)
            else:
                tag = Tag.objects.get(name=tag_el)
                instance.tags.add(tag)
        instance.save()
        return instance

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
