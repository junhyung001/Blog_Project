from Notice_Board.models import Board_list
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


def DeleteBoard(request, pk):
    delete_todo = get_object_or_404(Board_list, pk=pk)
    delete_todo.delete()
    return redirect('/board/')

def CompletedBoard(request, pk):
    todo = get_object_or_404(Board_list, pk=pk)
    todo.complete = True
    todo.save()
    return redirect('/board/')

class BoardUpdate(UpdateView):
    model = Board_list
    fields = ['todo', 'description', 'important']

    template_name = 'Notice_Board/board_update_form.html'


class BoardCreate(LoginRequiredMixin, CreateView):
    model = Board_list
    fields = ['todo', 'description', 'important']
    login_url = '/accounts/sigin/'

def Todos(request):
    boards = Board.objects.all().order_by('pk')

# Create your views here.
def Board(request):
    boards = Board_list.objects.all().order_by('pk')
    return render(
        request,
        'Notice_Board/board.html',
        {'board':boards},
        )

def index(request):
    board_list = Board_list.objects.all()
    return render(
        request,
        'Notice_Board/index.html',
        {
            'board_list' : board_list,
        }
    )