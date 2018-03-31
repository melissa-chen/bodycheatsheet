from django.shortcuts import render

def main(request):
    context = {}
    return render(request, 'website/index.html', context)