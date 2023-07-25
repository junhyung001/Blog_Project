from Notice_Board.models import Board_list
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


def DeleteBoard(request, pk):
    delete_board = get_object_or_404(Board_list, pk=pk)
    delete_board.delete()
    return redirect('/board/')

def CompletedBoard(request, pk):
    board = get_object_or_404(Board_list, pk=pk)
    board.complete = True
    board.save()
    return redirect('/board/')

class BoardUpdate(UpdateView):
    model = Board_list
    fields = ['board', 'description', 'important']

    template_name = 'Notice_Board/board_update_form.html'
    

class BoardCreate(LoginRequiredMixin, CreateView):
    model = Board_list
    fields = ['board', 'description', 'important']
    login_url = '/Accounts/sigin/'


def index(request):
    board_list = Board_list.objects.all()
    return render(
        request,
        'Notice_Board/index.html',
        {
            'board_list' : board_list,
        },
    )

def Board(request):
    boards = Board_list.objects.all().order_by('pk')
    
    return render(
        request,
        'Notice_Board/board.html',
        {
            'boards': boards
        },
        )