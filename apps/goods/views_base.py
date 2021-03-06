from django.http import JsonResponse
from django.views.generic.base import View
from goods.models import Goods
import json
from django.core import serializers


class GoodsListView(View):
    def get(self):
        """
        通过django的view实现商品列表页
        :param request:
        :return:
        """
        goods = Goods.objects.all()[:10]
        json_data = serializers.serialize('json', goods)  # 获取到字符串
        json_dict = json.loads(json_data)  # 字符串转字典
        return JsonResponse(json_dict, safe=False)
