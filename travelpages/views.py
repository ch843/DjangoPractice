from django.http import HttpResponse

def indexPageView(request) :
    sOutput = '<html><head><title>My Title</title></head><body><p style="color:red;"><b>one</b></p><p style="color:blue;">two</p><p style="font-size:50px;">three</p><ul><li>A</li><li>B</li><li>C</li></ul></body></html>'
    return HttpResponse(sOutput)   

def aboutPageView(request, trip_name) :
    sOutput = '<html><head><title>My Title</title></head><body><p>Welcome to ' + trip_name + '</p></body></html>'
    return HttpResponse(sOutput) 
  