from django.shortcuts import render

# Create your views here.
def Board(request):
    return render(
        request,
        'Notice_Board/board.html',
        )