from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item

def home_page(request):
  if request.method == 'POST':
    Item.objects.create(text=request.POST['item_text'])
    return redirect('/lists/the-only-list-in-the-world/')
  # items = Item.objects.all()
  return render(request, 'lists/home.html')
  # if request.method == 'POST':
  #   new_item_text = request.POST['item_text']
  #   Item.objects.create(text=new_item_text)
  # else:
  #   new_item_text = ''
  # return render(request, 'lists/home.html',
  #   {
  #     'new_item_text': new_item_text,
  #   })
  
def view_list(request):
  items = Item.objects.all()
  return render(request, 'lists/list.html', {'items': items})