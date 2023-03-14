# I'm creating this file because of I want to create a 5 Urls website
# and It will be called Personal Navigator

from django.http import HttpResponse

def web(request):
    return HttpResponse("""<h1> here we will see five Websites<h2>
    <a href="https://www.codewithharry.com/videos/python-django-tutorials-hindi-6/">
    This is Code with Harry Channel</a><br>
    <p>here is another channel that we visit</p><a href="https://search.yahoo.com/search?fr=mcafee&type=E211US885G0&p=facebook">facebook</a><br>
    <a href="https://www.webmicrosystems.com/">this is Danish bhai's website</a><br>
    <a href="https://www.shaadi.com/join-now/misspelt-shadi?ptnr=nbsribrncrexsha0062&msclkid=6999ca29630c1744f705ae2fbaaac5f0">Shaadi karo</a><br>
    <a href="https://stores.lenskart.com/">Chashma lgao</a>""")
    
