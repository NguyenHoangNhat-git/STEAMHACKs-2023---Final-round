from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from django.views import View

from HeartHeal.models.user import User
from HeartHeal.models.post import Post, Comment, Like, Category

import datetime
import os

class Forum(View):
    def get(self, request, category=None):
        if ('user' not in request.session):
            return redirect('login')

        current_user = User.get_user_by_id(request.session['user'])
        all_posts = Post.get_all_posts().order_by('-timestamp')
        all_categories = Category.objects.all()

        if category:
            if category == 'popular_today':
                all_posts = all_posts.filter(timestamp__date=datetime.date.today())
                all_posts = sorted(all_posts, key=lambda x: x.get_like_num(), reverse=True)
            elif category == 'my_post':
                all_posts = all_posts.filter(user=current_user)
            else:
                all_posts = all_posts.filter(categories__name__contains=category)

        
        data = {
            'current_user' : current_user,
            'posts': all_posts,
            'categories' : all_categories
        }
        return render(request, 'forum.html', data)
    
    def post(self, request):
        current_user = User.get_user_by_id(request.session['user'])
        if 'post_id' in request.POST:
            current_post = Post.objects.get(id=request.POST['post_id'])
            if 'comment' in request.POST:
                new_comment = Comment(post=current_post, user=current_user, content=request.POST['comment'])
                new_comment.save()
                return redirect('forum')
            elif 'like' in request.POST:
                new_like = Like(post=current_post, user=current_user)
                new_like.save()
                return redirect('forum')
            elif 'un_like' in request.POST:
                current_like = Like.objects.filter(post=current_post, user=current_user)
                current_like.delete()
                return redirect('forum')
        elif 'title' and 'content' in request.POST:
            category = Category.objects.filter(name=request.POST['category'])[0]
            if 'upload-file' in request.FILES:
                print('got the image')
                uploaded_image = request.FILES['upload-file']
                file_path = os.path.join(settings.MEDIA_ROOT, uploaded_image.name)
                file_name = default_storage.save(file_path, ContentFile(uploaded_image.read()))
                new_post = Post(title=request.POST['title'], content=request.POST['title'], user=current_user, image=file_name, categories=category)
            else:
                print('didnt got the image')
                new_post = Post(title=request.POST['title'], content=request.POST['content'], user=current_user, categories=category)
            new_post.save()
            return redirect('forum')

