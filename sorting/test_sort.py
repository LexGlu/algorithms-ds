import random
import copy
from . import bubble_sort, insertion_sort, selection_sort, shaker_sort, reverse_bubble_sort, merge_sort
import pytest


class TestSort:
    @pytest.fixture(scope='function', params=[bubble_sort, insertion_sort, selection_sort, shaker_sort,
                                              reverse_bubble_sort, merge_sort])
    def sort_func(self, request):
        return request.param

    @pytest.fixture(scope='function')
    def lst(self):
        return [random.randint(0, 100) for _ in range(10)]

    def test_sort(self, sort_func, lst: list):
        lst_copy = copy.deepcopy(lst)
        result = sort_func(lst)
        if result:
            assert result == sorted(lst_copy)
        else:
            assert lst == sorted(lst_copy)
        