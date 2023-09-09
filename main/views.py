from django.shortcuts import render

def show_main(request):
    context={
        'name_app' : 'inventory',
        'name' : 'Edbert',
        'class' : 'PBP D'
    }
    return render(request,"main.html",context)