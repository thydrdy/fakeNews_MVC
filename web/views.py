from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Users,News,Search
from django.core.files.storage import FileSystemStorage
from datetime import datetime
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect
from urllib.parse import unquote
from PIL.ExifTags import TAGS
import PIL
import os

user=None
# web 

# index
def index(request):
    template = loader.get_template('fake/index.html')
    context={}
    return HttpResponse(template.render(context, request))
# end index

# register
def register(request):
    template = loader.get_template('fake/register.html')
    context={}
    return HttpResponse(template.render(context, request))

@csrf_exempt
def post_register(request):
    first_name=request.POST.get("first_name")
    middle_name=request.POST.get("middle_name")
    last_name=request.POST.get("last_name")
    email=request.POST.get("email")
    pwd1=request.POST.get("pwd1")
    pwd2=request.POST.get("pwd2")
    template = loader.get_template('fake/register.html')
    if(pwd1!=pwd2):return HttpResponse(template.render({'error':'please Enter A valid Password'}, request))

    u= Users()
    u.first_name=first_name
    u.middle_name=middle_name
    u.last_name=last_name
    u.email=email
    u.password=pwd2
    u.save()
    template = loader.get_template('fake/login.html')
    return HttpResponse(template.render({'error':'Registration Complete'}, request))
# end register


# login 
def login(request):
    template = loader.get_template('fake/login.html')
    context={}
    return HttpResponse(template.render(context, request))

@csrf_exempt
def post_login(request):
    email=request.POST.get("email")
    password=request.POST.get("password")
    user_=Users.objects.filter(email=email)
    template = loader.get_template('fake/login.html')
    if(len(user_)==0):
        return HttpResponse(template.render({'error':' No user Register With this name'}, request))
    elif(user_[0].password!=password):
        return HttpResponse(template.render({'error':' Password is not correct'}, request))
    else:
        request.session['id']=user_[0].id
        return redirect('/web/posts')
# end login

# posts
def posts(request):
    template = loader.get_template('fake/posts.html')
    posts=News.objects.all().order_by('-date_created')
    context={'posts':posts}
    user_=user=request.session.get('id', None)
    if(user!=None):context['system_user']=True
    return HttpResponse(template.render(context, request))

def add_post(request):
    user=request.session.get('id', None)
    if(user==None):
        template = loader.get_template('fake/login.html')
        return HttpResponse(template.render({}, request))

    template = loader.get_template('fake/createPost.html')
    context={}
    return HttpResponse(template.render(context, request))

@csrf_exempt
def post_posts(request):
    user=Users.objects.get(id=int(request.session['id']))
    thread_name=request.POST.get("thread_name")
    if(thread_name[0]!='#'):thread_name='#'+thread_name
    head_line=request.POST.get("head_line")
    link=request.POST.get("link")
    news_status=request.POST.get("news_status")
    additional_info=request.POST.get("additional_info")

    if request.method == 'POST' and request.FILES['image']:
        myfile = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

    news=News(news_link=link,thread_name=thread_name,head_line=head_line,by=user.last_name+', '+user.first_name,
    status=news_status,additional_text=additional_info,img_path=uploaded_file_url,date_created=datetime.now())
    news.save()
    template = loader.get_template('fake/createPost.html')
    
    api.publish_changes()
    api.structure_xml()
    return redirect('/web/posts')

def delete_posts(request):
    id=int(request.GET.get("del_id"))
    News.objects.get(id=id).delete()
    return JsonResponse({"id":id})
  
# end posts

# search
@csrf_exempt
def submit(request):
    new_check=request.POST.get('new_check')
    check=Search(thread_link=new_check,news_link='',status=False)
    check.save()
    template = loader.get_template('fake/posts.html')
    posts=News.objects.all().order_by('-date_created')
    return HttpResponse(template.render({'posts':posts}, request))

@csrf_exempt
def search(request):
    new_check=request.POST.get('search')
    if(new_check[0]!='#'):new_check='#'+new_check
    template = loader.get_template('fake/posts.html')
    posts=News.objects.filter(thread_name=new_check).order_by('-date_created')
    return HttpResponse(template.render({'posts':posts}, request))

# end search
# vote
def vote(request):
    pass           
# end vote
def detail(request, entity_id):
    pass
    #template = loader.get_template('pages/chat.html')
    #context = {}
    #return HttpResponse(template.render(context, request))

def upload_image(request):
    pass


#end Web
