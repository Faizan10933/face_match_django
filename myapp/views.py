from django.shortcuts import render
from django.http import HttpResponse
from soupsieve import match
from .models import Information
from django.shortcuts import render
# import cv2
# import face_recognition


def index(request):
    information= Information.objects.all()

    context={'information': information}
    return render(request, 'index.html', context)

def check(request):
    if request.method == "POST":
      name = request.POST.get('name')
      age = request.POST.get('age')
      phonenum = request.POST.get('phonenum')
      image1 = request.FILES.get('ima')
      image2 = request.FILES.get('image')

      print("=================")
      print(type(image1))
      print(image2)
      
    #   img = cv2.imread(image1)
    #   rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #   img_encoding = face_recognition.face_encodings(rgb_img)[0]

    #   img2 = cv2.imread(image2)
    #   rgb_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
    #   img_encoding2 = face_recognition.face_encodings(rgb_img2)[0]

    #   result = face_recognition.compare_faces([img_encoding], img_encoding2)

    #   print("Result: ", result)

    #   info =  Information(name=name, age=age, phonenum=phonenum, match=result)
      info =  Information(name=name, age=age, phonenum=phonenum)
      info.save()
    #   messages.success(request, 'Your message has been sent.')
    
    return render(request,'check.html')

# Create your views here.
