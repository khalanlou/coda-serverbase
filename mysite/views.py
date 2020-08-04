from django.shortcuts import render
from django.views.generic import TemplateView
from .models import main ,adminProfile
from .forms import emailservice



class contact_us(TemplateView):
    from .forms import centure_form
    mains=[]
    main_query = main.objects.all()
    for c in main_query:
        mains.append({
            'logo':c.logo.url ,
            'field1':c.field1 ,
            'field2':c.field2 ,
            'field3':c.field3 ,
            'field4':c.field4 ,
        })
    users = []
    user_query = adminProfile.objects.all()
    for a in user_query:
        users.append({
        'name':a.user.first_name+' '+a.user.last_name ,
        'img':a.avatar.url ,
        'description':a.description , 
        'theory':a.theory ,
        })
    centure_form = centure_form()
    form = emailservice()
    def get(self, request, **kwargs):
        context ={
            'users':self.users ,
            'main':self.mains[0] ,
            'centure':self.centure_form ,
            'form':self.form ,
        }
        return render(request,"contact.htm", context)
    def post(self, request, **kwargs):
        centure_filled_form = centure_form(request.POST)
        filled_form = emailservice(request.POST)
        if filled_form.is_valid():
            filled_form.save()
        if centure_filled_form.is_valid():
            centure_filled_form.save()
        context ={
            'users':self.users ,
            'main':self.mains[0] ,
            'form': self.form ,
            'centure_form':self.centure_form ,
        }
        return render(request,"index.htm", context)
class index(TemplateView):
    mains = []
    users = []
    user_query = adminProfile.objects.all()
    main_query = main.objects.all()
    for c in main_query:
        mains.append({
            'logo':c.logo.url ,
            'field1':c.field1 ,
            'field2':c.field2 ,
            'field3':c.field3 ,
            'field4':c.field4 ,
        })
    for a in user_query:
        users.append({
        'name':a.user.first_name+' '+a.user.last_name ,
        'img':a.avatar.url ,
        'description':a.description , 
        'theory':a.theory ,
        'github':a.social_media.github ,
        'linkedin':a.social_media.linkedin ,
        'twitter':a.social_media.twitter ,
        'telegram':a.social_media.telegram ,
        'bale':a.social_media.bale ,
        'instagram':a.social_media.instagram ,
        })  
    def get(self, request, **kwargs):
        form = emailservice()
        context ={
            'users':self.users ,
            # 'posts':self.posts ,
            'main':self.mains[0] ,
            'form': form ,
        }
        return render(request,"index.htm", context)

    def post(self, request, **kwargs):
        form = emailservice()
        filled_form = emailservice(request.POST)
        if filled_form.is_valid():
            filled_form.save()
        else:
            form = emailservice()
        form = emailservice()
        context ={
            'users':self.users ,
            # 'posts':self.posts ,
            'main':self.mains[0] ,
            'form': form
        }
        return render(request,"index.htm", context)

class costs(TemplateView):
    mains = []
    main_query = main.objects.all()
    for c in main_query:
        mains.append({
            'logo':c.logo.url ,
            'field1':c.field1 ,
            'field2':c.field2 ,
            'field3':c.field3 ,
            'field4':c.field4 ,
        })
    def get(self, request, **kwargs):
        form = emailservice()
        context = {
            'main':self.mains[0] ,
            'form': form ,
        }        
        return render(request , 'costs.htm' , context)
    def post(self, request, **kwargs):
        form = emailservice()
        filled_form = emailservice(request.POST)
        if filled_form.is_valid():
            filled_form.save()
        else:
            form = emailservice()
        form = emailservice()
        context ={
            'main':self.mains[0] ,
            'form': form
        }
        return render(request,"index.htm", context)
class portfolio(TemplateView):
    def get(self, request, **kwargs):
        # mains = []
        # main_query = main.objects.all()
        # for c in main_query:
        #    mains.append({
        #        'logo':c.logo ,
        #        'field1':c.field1 ,
        #        'field2':c.field2 ,
        #        'field3':c.field3 ,
        #        'field4':c.field4 ,
        #    })
        context ={
        #    'main':self.mains[0] ,
        }
        return render(request,"portfolio.htm", context)

class blog(TemplateView):
    from django.db.models import Q
    from .models import Article
    #for searching in blog
    mains = []
    posts = []
    results =[]
    post_query = Article.objects.all()
    main_query = main.objects.all()
    for c in main_query:
        mains.append({
            'logo':c.logo.url ,
            'field1':c.field1 ,
            'field2':c.field2 ,
            'field3':c.field3 ,
            'field4':c.field4 ,
        })
    for b in post_query:
        posts.append({
        'author':b.author ,
        'cover':b.cover.url ,
        'content':b.content[:256]+"..." , #just shows the 256 character 
        'category':b.category,
        'title':b.title ,
        })
    def get(self, request, **kwargs):
        results =[]
        query = request.GET.get('q')
        form = emailservice()
        #you say that you working on a global result
        if query:
            self.results = []
            queryset = self.Q(title__icontains=query) | self.Q(content__contains=query)
            #include searched data in title or content
            result_query = self.Article.objects.filter(queryset).distinct()
            #distinct remove duplicate search results
            for result in result_query:
                self.results.append({
                    'author'   :result.author  ,
                    'cover'    :result.cover.url , 
                    'content'  :result.content ,
                    'category' :result.category ,
                    'title'    :result.title ,
                })
        else:
            self.results = []
        form = emailservice()
        context = {
            'main':self.mains[0] ,
            'form': form ,
            'posts' :self.posts ,
            'results' :self.results ,
            'query':query,
        }
        return render(request,"blog.htm", context)
    def post(self, request, **kwargs):
        form = emailservice()
        filled_form = emailservice(request.POST)
        if filled_form.is_valid():
            filled_form.save()
        else:
            form = emailservice()
        form = emailservice()
        context ={
            'main':self.mains[0] ,
            'form': form ,
            'posts' :self.posts ,
        }
        return render(request,"blog.htm", context)
