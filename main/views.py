from django.shortcuts import render
from .models import Book
from django.shortcuts import get_object_or_404, redirect
from order.forms import CustomerForm


def main(request):
    books = Book.objects.all()
    context = {
        "books": books
    }
    return render(request, "main/main_view.html", context)


def book_page(request, idx):
    book = get_object_or_404(Book, pk=idx)
    form = CustomerForm()
    context = {
        "book": book,
        "form": form
    }
    if request.POST:
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save(book=book)
            return redirect("main_page:thanks")
    return render(request, "main/book_page_view.html", context)


def thanks(request):
    return render(request, "main/thanks_view.html")