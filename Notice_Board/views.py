from django.shortcuts import get_object_or_404, render
from Notice_Board.models import Board_list

# Create your views here.
def Board(request):
    return render(
        request,
        'Notice_Board/board.html',
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






def DeleteTodo(request, pk):
    delete_todo = get_object_or_404(Board, pk=pk)
    delete_todo.delete()
    return redirect('/todo/')

def CompletedTodo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.complete = True
    todo.save()
    return redirect('/todo/')

