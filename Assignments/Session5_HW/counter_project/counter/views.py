from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'counter/index.html')

def result(request):
    text = request.POST['text']
    total_len = len(text)
    total_len_no_blank = len(text.replace(' ',''))
    word_len = len(text.split(' '))
    context = {'text':text, 'total_len' : total_len, 'total_len_no_blank':total_len_no_blank, 'word_len' : word_len}
    return render(request, 'counter/result.html', context)