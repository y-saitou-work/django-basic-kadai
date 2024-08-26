from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Product
from django.urls import reverse_lazy
 
# Create your views here.
class ProductListView(ListView):
    model = Product
    paginate_by = 3


class ProductCreateView(CreateView):
    model = Product
    fields = '__all__' # 新規作成時にユーザーが入力するフィールドを指定する

class ProductUpdateView(UpdateView):
    model = Product
    fields = '__all__'  # 新規作成時にユーザーが入力するフィールドを指定する
    template_name_suffix = '_update_form'  # 編集用のTemplateファイル名を指定。この場合はproduct_update_form.htmlとなる

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('list')  # 削除成功後に遷移するURL


class ProductDetailView(DetailView):
    model = Product
    template_name_suffix =  '_detail'