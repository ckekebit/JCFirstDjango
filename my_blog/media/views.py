from django.shortcuts import render
from media.models import Media
import os

# Create your views here.

def media_home(request):
    media_list = Media.objects.all()
    return render(request, 'mediahome.html', {'media_list' : media_list}, {'request' : request})

def upload_file(request):
    if request.method == "POST":
        myFile =request.FILES.get("myfile", None)
        if not myFile:
            return render(request,'home.html')
	filePath = os.path.join("/Users/longjing/Django/my_blog/static/",myFile.name)
        destination = open(filePath, 'wb+')
        for chunk in myFile.chunks():
            destination.write(chunk)
        destination.close()
        Media.objects.create(mediaName=myFile.name, mediaPath=filePath).save
        return render(request,'home.html')
