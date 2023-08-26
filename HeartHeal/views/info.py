from django.shortcuts import render, redirect

from HeartHeal.models.news import News, News_Category, News_Comments

def hotlines(request):
    return render(request, 'hotlines.html')

def how_it_works(request):
    return render(request, 'how_it_works.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def news(request):
    categories = News_Category.objects.all()
    posts = News.objects.all()

    data = {
        'categories' : categories,
        'posts' : posts
    }
    return render(request, 'news.html', data)

def detail(request, post_id):
    news = News.objects.get(id=post_id)
    # if request.method == 'POST':
    #     name = request.POST['name']
    #     email = request.POST['email']
    #     comment = request.POST['message']
    #     News_Comments.objects.create(
    #         news=news,
    #         name=name,
    #         email=email,
    #         comment=comment,
    #     )

    category = News_Category.objects.get(id=news.category.id)
    related_news = News.objects.filter(category=category).exclude(id=news.id)[0:8]
    # related = related_news.all()
    # comments = News_Comments.objects.filter(news=news, status=True).order_by('-id')
    return render(request, 'Detail.html', {
        'detail': news,
        'related_news': related_news,
        # 'comments': comments,
    })