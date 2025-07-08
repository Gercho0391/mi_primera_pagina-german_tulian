from django.shortcuts import render

def portada_con_template(request):
    return render(request, 'mi_primer_app/portada.html') 
