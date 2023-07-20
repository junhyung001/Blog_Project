from django.shortcuts import get_object_or_404, render

# Create your views here.
def Board(request):
    return render(
        request,
        'Notice_Board/board.html',
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

