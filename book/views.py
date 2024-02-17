from django.shortcuts import render,redirect
from django.views.generic import View
from book.models import Books
from book.forms import BookForm
from django.contrib.auth.models import User

class BookListView(View):
    def get(self,request,*args,**kwargs):

        qs=Books.objects.all()

        return render(request,"book_list.html",{"data":qs})
    
class BookDetailsView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        qs=Books.objects.get(id=id)
        return render(request,'book_details.html',{'data':qs})

class BookDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        Books.objects.get(id=id).delete()
        return redirect("books-all")
    
class BookCreateView(View):
    def get(self,request,*args,**kwargs):
        form=BookForm()
        return render(request,"book_add.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=BookForm(request.POST,files=request.FILES)

        if form.is_valid():
            form.save()
            return redirect("books-all")
        else:
            return render(request,"book_add.html",{"form":form})
        
class BookUpdateView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Books.objects.get(id=id)
        form=BookForm(instance=obj)
        return render(request,"book_edit.html",{"form":form})
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Books.objects.get(id=id)
        form=BookForm(request.POST,instance=obj,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("books-all")
        else:
            return render(request,"book_edit.html",{"form":form})
 
class SignUpView(View):
    def get(self,request,*args,**kwargs):
        form=BookForm()
        return render(request,"register.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=BookForm(request.POST)
        if form.is_valid():
            # form.save()
            print(form.cleaned_data)
            User.objects.create_user(**form.cleaned_data)
            return render(request,"register.html",{"form":form})
        else:
            return render(request,"register.html",{"form":form})
