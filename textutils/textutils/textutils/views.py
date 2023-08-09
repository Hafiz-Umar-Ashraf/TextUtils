from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def analyze(request):
        global params
        text_param = request.POST.get('text', 'default')
        remove_punc = request.POST.get('remove_punc', 'off')
        upper_case = request.POST.get('upper_case', 'off')
        newline = request.POST.get('newline', 'off')
        extra_space_remover = request.POST.get('extra_space_remover', 'off')
        char_count = request.POST.get('char_count', 'off')

        if remove_punc == 'on':
            punctuations = '''. , ? ! ; : ' \" () [] {} - — – ... / \\ & * $ % # @'''
            analyzed = ""
            for char in text_param:
                if char not in punctuations:
                    analyzed = analyzed + char
            params = {'purpose': ' Removed Punctuations', 'analyzed_text': analyzed}
            text_param = analyzed

        if upper_case == 'on':
            analyzed = ""
            for char in text_param:
                analyzed = analyzed + char.upper()
            params = {'purpose': ' Upper Case', 'analyzed_text': analyzed}
            text_param = analyzed

        if newline == 'on':
            analyzed = ""
            for char in text_param:
                if char != "\n":
                    analyzed = analyzed + char
            text_param = analyzed
            params = {'purpose': ' Removed New Line ', 'analyzed_text_line_remove': analyzed}



        if extra_space_remover == 'on':
            analyzed = ""
            for index, char in enumerate(text_param):
                if not (text_param [index] == " " and text_param [index+1] == " "):
                    analyzed = analyzed + char
            params = {'purpose': ' Extra Space Remover ', 'analyzed_text': analyzed}
            text_param = analyzed
            # return render(request, 'analyze.html', params)

        if char_count == 'on':
            analyzed = len(text_param)
            text_param = analyzed
            params = {'purpose': ' Character Count ', 'analyzed_text': analyzed}

        if (remove_punc != "on" and newline != "on" and extra_space_remover != "on" and upper_case != "on" and char_count != "on"):
            return HttpResponse("please select any operation and try again")
        return render(request, 'analyze.html', params)


