from django.http import HttpResponse


def index(request):
    html= """<b>My personal Site</b> <br/>
          <i>author: Albert Ribes</i><br/>
	  <hr>
          <a href="/polls/">Polls</a> <br/>
          <a href="/blog/">Blog</a> <br/>
          <a href="/admin/">Admin</a> <br/>
	  <a href="/contact/">Contact</a>"""
    return HttpResponse(html)
