from django.shortcuts import render
from blog.models import Category, Banner, Article, Tag, Link
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
# 首页
def index(request):
    allcategory = Category.objects.all()  # 通过Category表查出所有分类
    banner = Banner.objects.filter(is_active=True)[0:4] #banner图
    tui = Article.objects.filter(tui__id = 1)[:3]   #推荐
    article = Article.objects.order_by('-id')[:10]  #查询文章
    hot = Article.objects.all().order_by('views')[:10]  # 通过浏览数进行排序
    remen = Article.objects.filter(tui__id=2)[:6]   #热门推荐
    tags = Tag.objects.all()    #标签
    links = Link.objects.all()

    # 把查询出来的分类封装到上下文里
    context = {
        'allcategory': allcategory,
        'banner':banner,
        'tui': tui,
        'allarticle':article,
        'hots':hot,
        'remens':remen,
        'tags':tags,
        'links':links,
    }
    return render(request, 'index.html', context)  # 把上下文传到index.html页面

# 列表页
def list(request, lid):
    list = Article.objects.filter(category_id = lid)
    cname = Article.objects.get(id = lid)
    remen = Article.objects.filter(tui__id = 2)[:6]
    all_category = Category.objects.all()
    tags = Tag.objects.all()
    # 分页
    page = request.GET.get('page')
    pagintor = Paginator(list, 5)
    try:
        list = pagintor.page(page)
    except PageNotAnInteger:
        list = pagintor.page(1)
    except EmptyPage:
        list = pagintor.page(pagintor.num_pages)

    return render(request, 'list.html', locals())

# 内容页
def show(request, sid):
    show = Article.objects.get(id=sid)  # 查询指定ID的文章
    allcategory = Category.objects.all()  # 导航上的分类
    tags = Tag.objects.all()  # 右侧所有标签
    remen = Article.objects.filter(tui__id=2)[:6]  # 右侧热门推荐
    hot = Article.objects.all().order_by('?')[:10]  # 内容下面的您可能感兴趣的文章，随机推荐
    previous_blog = Article.objects.filter(create_time__gt=show.create_time, category=show.category.id).first()
    netx_blog = Article.objects.filter(create_time__lt=show.create_time, category=show.category.id).last()
    show.views = show.views + 1
    show.save()
    return render(request, 'show.html', locals())

# 标签
def tag(request, tag):
    list = Article.objects.filter(tags__name=tag)  # 通过文章标签进行查询文章
    remen = Article.objects.filter(tui__id=2)[:6]
    allcategory = Category.objects.all()
    tname = Tag.objects.get(name=tag)  # 获取当前搜索的标签名
    page = request.GET.get('page')
    tags = Tag.objects.all()
    paginator = Paginator(list, 5)
    try:
        list = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        list = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        list = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return render(request, 'tags.html', locals())

# 搜索
def search(request):
    ss = request.GET.get('search')  # 获取搜索的关键词
    list = Article.objects.filter(title__icontains=ss)  # 获取到搜索关键词通过标题进行匹配
    remen = Article.objects.filter(tui__id=2)[:6]
    allcategory = Category.objects.all()
    page = request.GET.get('page')
    tags = Tag.objects.all()
    paginator = Paginator(list, 10)
    try:
        list = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        list = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        list = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return render(request, 'search.html', locals())

# 关于我们
def about(request):
    allcategory = Category.objects.all()
    return render(request, 'page.html', locals())
