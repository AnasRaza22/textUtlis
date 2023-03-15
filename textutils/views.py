# I have created this file - Anas 
from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse('hello India')
# def adm(request):
#     return HttpResponse("It's for admin")


# def text(request):
#     file = open('text.txt','r') --text func we created for the read and display but it did not work
#     data=file.read()
#     return HttpResponse(data)

# here we will learn about laying pipelines
def index2(request):
    return render(request,'index2.html')

def About(request):
    return render(request,'About.html')

def Contact(request):
    return render(request,'Contact.html')

def analyze(request):
    # print(request.GET.get('text','default')) #and we can put it in a variable
    # here we will get the text
    djtext = request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcap=request.POST.get('fullcap','off')               #if we gave post method in 
    newlineremover=request.POST.get('newlineremover','off') #form/action we have to give 
    spaceremover=request.POST.get('spaceremover','off')     #all request 'post' otherwise
    charcount=request.POST.get('charcount','off')           #it will give us else msg(lastbaala)

    if removepunc=='on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
                
        params={"purpose":"Removing punctuations","analyzed_text":analyzed}
        # return render(request,'analyze2.html',params)
        djtext=analyzed
    
    if fullcap=='on':
        analyzed=''
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={"purpose":"making all upper case",'analyzed_text':analyzed}
        # return render(request,'analyze2.html',params)
        djtext=analyzed
    
    if newlineremover=='on':
        analyzed=''
        for char in djtext:     #we have to given both method to replace new line
            if char!='\n'and char!='\r':  #bcoz when we execute the new line both are in our text
                analyzed=analyzed+char    
        params={'purpose':"here you will not see any new line","analyzed_text":analyzed}
        # return render(request,"analyze2.html",params)
        djtext=analyzed
    
    if spaceremover=='on':
        analyzed=''
        for index,char in enumerate(djtext):
            if not(djtext[index]==' ' and djtext[index+1]==' '):
                analyzed=analyzed+char
        params={"purpose":'removing space',"analyzed_text":analyzed}
        # return render(request,'analyze2.html',params)
        djtext=analyzed
    
    if charcount=='on':
        count=0
        while len(djtext)>count:
            count+=1

        params={"purpose":"Count the characters","analyzed_text":count}
        # return render(request,'analyze2.html',params)
    if(charcount!='on' and spaceremover!='on' and newlineremover!='on' and fullcap!='on' and removepunc!='on'):
        return HttpResponse("Here is something Error")
    return render(request,'analyze2.html',params)   
    


# def charcount(request):
#     return HttpResponse("charcount<br><a href='http://127.0.0.1:8000/'>hOmE</a>")