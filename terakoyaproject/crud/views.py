from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Product
from django.urls import reverse_lazy


class TopView(TemplateView):
    template_name = "top.html"

class ProductListView(ListView):
    model = Product
    # ページネーション
    # 1ページに3件表示するように指定
    # ListView のクラス変数
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