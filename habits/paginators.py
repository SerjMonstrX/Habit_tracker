from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size = 10  # Количество элементов на странице
    page_size_query_param = 'page_size'  # Параметр запроса для указания размера страницы
    max_page_size = 100  # Максимальное количество элементов на странице
