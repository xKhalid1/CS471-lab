from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Book, Student, Departement, Card, Address, Course, Student9
from django.db.models import Q
from django.db.models import Count, Min, Max, Sum, Avg
from .forms import BookForm
from django import forms


def index(request):
    return render(request, "bookmodule/index.html")

def list_books(request): 
    return render(request, 'bookmodule/list_books.html')


def viewbook(request, bookId): 
    return render(request, 'bookmodule/one_book.html')

def aboutus(request): 
    return render(request, 'bookmodule/aboutus.html')

def html5(request):
    return render(request, 'bookmodule/html5.html')

def tables(request):
    return render(request, 'bookmodule/tables.html')

def formatting(request):
    return render(request, 'bookmodule/formatting.html')


def listing(request):
    return render(request, 'bookmodule/listing.html')


def links(request):
    return render(request, 'bookmodule/links.html')

def search(request):
    if request.method == "POST":
        string = request.POST.get('keyword', '').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        books = __getBooksList()
        newBooks = []

        for item in books:
            contained = False
            if isTitle and string in item['title'].lower():
                contained = True
            if not contained and isAuthor and string in item['author'].lower():
                contained = True
            
            if contained:
                newBooks.append(item)
        return render(request, 'bookmodule/booklist.html', {'books': newBooks})
    
    return render(request, 'bookmodule/search.html')

def __getBooksList():
    mybook = Book(title = 'CS471', author = 'Khalid Alomar', edition = 1)
    mybook.save()
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'} 
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'} 
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]

def simple_query(request):
    mybooks=Book.objects.filter(title__icontains='471') # <- multiple objects
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})

def complex_query(request):
    mybooks=books=Book.objects.filter(author__isnull = False).filter(title__icontains='and').filter(edition__gte = 2).exclude(price__lte = 100)[:10]
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')
    

def task1(request):
    mybooks=Book.objects.filter(price__lte='80').order_by('-price')
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})


def task2(request):
    mybooks=Book.objects.filter(edition__gt='3').filter(Q(title__icontains='co') | Q(author__icontains='co'))
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})



def task3(request):
    mybooks=Book.objects.filter(edition__lte='3').exclude(Q(title__icontains='co') | Q(author__icontains='co'))
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})


def task4(request):
    mybooks=Book.objects.order_by('title')
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})


def task5(request):
    mybooks = Book.objects.aggregate(booknum_count=Count('id'), total_price=Sum('price'), average_price=Avg('price'), max_price=Max('price'), min_price=Min('price'))
#    mybooks=Book.objects.aggregate(booknum_count=Count('id')),Sum('price'), Avg('price'), Max('price'), Min('price')
    return render(request, 'bookmodule/bookList5.html', {'books':mybooks})



def task7(request):
    mybooks = Student.objects.values('address__city').annotate(student_count=Count('id')).order_by('student_count')
    return render(request, 'bookmodule/studentlist.html', {'books': mybooks})



#lab 9
def lab9task1(request):
    mybook = Student9.objects.values('departement__name').annotate(student9_count=Count('id')).order_by('-student9_count')

    return render(request, 'bookmodule/lab9task1.html', {'books': mybook})


def lab9task2(request):
    mybook = Student9.objects.values('Courses__title').annotate(student9_count=Count('id')).order_by('-student9_count')
    
    return render(request, 'bookmodule/lab9task2.html', {'book': mybook})


def lab9task3(request):
    mybook = Student9.objects.values('departement__name').annotate(student_id=Min('id'))

    for item in mybook:
        student = Student9.objects.get(id=item['student_id'])
        item['student_name'] = student.name

    return render(request, 'bookmodule/lab9task3.html', {'books': mybook})

def lab9task4(request):

    mybook = Departement.objects.annotate(student_count=Count('student9')).filter(student_count__gt=2).order_by('-student_count')
    return render(request, 'bookmodule/lab9task4.html', {'books': mybook})



#lab 10
def listbooks(request):
    mybooks = Book.objects.order_by('id')
    return render(request, 'bookmodule/listbooks.html', {'books': mybooks})



def addbook(request):
    if request.method == "POST":
        title = request.POST['title']
        author = request.POST['author']
        price = request.POST['price']
        edition = request.POST['edition']
        Book.objects.create(title = title, author = author, price = price, edition = edition)
        return redirect('books.listbooks')
    return render(request, 'bookmodule/addbook.html')


def editbook(request, id):
    mybook = get_object_or_404(Book, id=id)
    if request.method == "POST":
        mybook.title = request.POST['title']
        mybook.author = request.POST['author']
        mybook.price = request.POST['price']
        mybook.edition = request.POST['edition']
        mybook.save()
        return redirect('books.listbooks')
    return render(request, 'bookmodule/editbook.html', {'books': mybook})

def deletebook(request, id):
    mybook = get_object_or_404(Book, id=id)
    mybook.delete()
    return redirect('books.listbooks')


#lab 10_2

def listbooks2(request):
    mybooks = Book.objects.order_by('id')
    return render(request, 'bookmodule/listbooks2.html', {'books': mybooks})

def addbook2(request): 
    if request.method=='POST':
        form = BookForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('books.listbooks2')
    else: form = BookForm() 
    return render(request, "bookmodule/addbook2.html", {'form':form})

def editbook2(request,id): 
    obj = Book.objects.get(id = id) 
    if request.method=='POST':
        form = BookForm(request.POST, instance=obj)
        if form.is_valid(): 
            form.save() 
            return redirect('books.listbooks2')
    else: form = BookForm(instance=obj) 
    return render(request, "bookmodule/editbook2.html",{'form':form})

def deletebook2(request,id):
    obj = Book.objects.get(id = id) 
    if request.method=='POST': 
        obj.delete() 
        return redirect('books.listbooks2')
    return render(request, "bookmodule/deletebook2.html", {'obj':obj})