"""В этом модуле лежат различные методы по представлению товаров.

Заказов и т.д.

"""
import logging
from timeit import default_timer
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    )

from .models import Product, Order, ProductImage
from django.contrib.auth.models import Group
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, reverse
# from .forms import ProductForms
from .serializers import Productserializer
from drf_spectacular.utils import extend_schema, OpenApiResponse


log = logging.getLogger(__name__)

@extend_schema(description="Product views CRUD")
class ProductViewSet(ModelViewSet):
    """
    Набор представлений для действий над Product.

    Полный CRUD для сущностей товара.
    """
    queryset = Product.objects.all()
    serializer_class = Productserializer
    filter_backends = [
        SearchFilter,
        DjangoFilterBackend,
        OrderingFilter,
    ]
    search_fields = ["name", "discription"]
    filterset_fields = [
        "name",
        "price",
        "discription",
        "discount",
        "archived",
    ]
    ordering_fields = [
        "name",
        "price",
        "discription",
    ]

    @extend_schema(
        summary="Get one product by ID",
        description="Retriever **products**, returns 404 if not found",
        responses={
            200: Productserializer,
            404: OpenApiResponse(description="Empty response, product by id not found"),
        }
    )
    def retrieve(self, *args, **kwargs):
        return super().retrieve(*args, **kwargs)

class ShopIndexView(View):
    """
    метод гет полностью заменит функцию def shop_index
    """

    def get(self, request: HttpRequest) -> HttpResponse:
        products = [
            ('book', 1111),
            ('note', 1211),
            ('paper', 1121),
        ]
        context = {
            "time_running": default_timer(),
            "products": products,
            "items": 5,

        }
        log.debug("Products for shop index: %s", products)
        log.info("Rendering shop index")
        return HttpResponse(render(request, 'old_store/shop_index.html', context=context))


# class GroupListView(View):
#     """
#     этот класс заменяет метод деф groups_list
#     """
#
#     def get(self, request: HttpRequest) -> HttpResponse:
#         context = {
#             "form": GroupForm(),
#             "groups": Group.objects.prefetch_related('permissions').all(),
#             }
#         return render(request, 'old_store/groups-list.html', context=context)
#
#     def post(self, request: HttpRequest):
#         form = GroupForm(request.POST)
#         if form.is_valid():
#             form.save()
#
#         return redirect(request.path)


class ProductDetailsView(DetailView):
    """Класс отображает детали продукта.--
        теперь метод def get мы заменили
        на переменные из класса DetailView

    """
    template_name = "old_store/product_details.html"
    # model = Product
    queryset = Product.objects.prefetch_related("images")
    context_object_name = "product"


class ProductsListView(ListView):
    """
    Этот класс заменяет метод products_list
      теперь чтобы изменить параметры в шаблоне требуется переписать
      их в методе get_context_data
    """
    template_name = "old_store/products-list.html"
    # model = Product
    context_object_name = "products"
    queryset = Product.objects.filter(archived=False)


class ProductCreateView(CreateView):
    # def test_func(self):
    #     # return self.request.user.groups.filter(name="secret-group").exists()
    #     return self.request.user.is_superuser

    model = Product
    fields = "name", "price", "discription", "discount", "preview"
    success_url = reverse_lazy("old_store:product_list")


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("old_store:product_list")

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(success_url)


class ProductUpdateView(UpdateView):
    model = Product
    fields = "name", "price", "discription", "discount", "preview"
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("old_store:products_details")
    # form_class = ProductForms

    def form_valid(self, form):
        response = super().form_valid(form)
        for image in form.files.getlist("images"):
            ProductImage.objects.create(
                product=self.object,
                image=image
            )
        return response

    def get_success_url(self):
        return reverse(
            "old_store:products_details",
            kwargs={"pk": self.object.pk},
        )


class OrderListView(LoginRequiredMixin, ListView):
    queryset = (
        Order.objects
        .select_related("user")
        .prefetch_related("products")
    )


class OrderDetailView(ProductDetailsView, DetailView):
    permission_required = "old_store.view_order",
    queryset = (
        Order.objects
        .select_related("user")
        .prefetch_related("products")
    )


# def create_product(request: HttpRequest) -> HttpResponse:
#     if request.method == "POST":
#         form = ProductForms(request.POST)
#         if form.is_valid():
#             # Product.objects.create(**form.cleaned_data)
#             form.save()
#             url = reverse("products_list")
#             return redirect(url)
#     else:
#         form = ProductForms()
#     context = {
#         "form": form,
#     }
#
#     return render(request, 'old_store/create-product.html', context=context)

class ProductDataExportView(View):
    def get(self, request: HttpRequest) ->JsonResponse:
        products = Product.objects.order_by('pk').all()
        products_data = [
            {
                'pk': product.pk,
                'name': product.name,
                'price': product.price,
                'archived': product.archived,
            }
            for product in products
        ]
        elem = products_data[0]
        name = elem['name']
        print('name', name)
        return JsonResponse({'products':products_data})
