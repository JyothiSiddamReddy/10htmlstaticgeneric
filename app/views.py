from django.shortcuts import render

# Create your views here.
def forms(request):
    return render(request,'inlineforms.html')


def table(request):
    return render(request,'table.html')

def cssforms(request):
    return render(request,'cssforms.html')

def csslandingfile(request):
    return render(request,'csslandingfile.html')

def registerform(request):
    return render(request,'registerform.html')

def animation(request):
    return render(request,'animation.html')

def boxmodel(request):
    return render(request,'boxmodel.html')

def transforms(request):
    return render(request,'transforms.html')

def combinators(request):
    return render(request,'csscombinators.html')

def selectors(request):
    return render(request,'selectors.html')


