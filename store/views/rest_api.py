# views.py
from django.db.models import Count
from django.utils import timezone
from django.http import JsonResponse
from datetime import timedelta
from  store.models.product_count import Product, ProductRetrieval
from rest_framework.views import APIView

class TopProductsAPIView(APIView):
    def get(self, request):
       
        now = timezone.now()

        last_day = now - timedelta(days=1)
        last_week = now - timedelta(weeks=1)

        top_all_time = ProductRetrieval.objects.values('product_id').annotate(
            count=Count('product_id')).order_by('-count')[:5]

        top_last_day = ProductRetrieval.objects.filter(retrieval_time__gte=last_day).values(
            'product_id').annotate(count=Count('product_id')).order_by('-count')[:5]


        top_last_week = ProductRetrieval.objects.filter(retrieval_time__gte=last_week).values(
            'product_id').annotate(count=Count('product_id')).order_by('-count')[:5]

        def convert_to_product_details(queryset):
            return [
                {
                    "product_id": item['product_id'],
                    "name": Product.objects.get(id=item['product_id']).name,
                    "retrieval_count": item['count']
                }
                for item in queryset
            ]

        data = {
            "top_all_time": convert_to_product_details(top_all_time),
            "top_last_day": convert_to_product_details(top_last_day),
            "top_last_week": convert_to_product_details(top_last_week)
        }

        return JsonResponse(data, safe=False)
