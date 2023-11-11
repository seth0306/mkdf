from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(Address)  # Addressモデルを登録
admin.site.register(Company)
admin.site.register(Project)  # プロジェクトデータ
admin.site.register(Effort)  # 工数データ
admin.site.register(Person)  # 要員データ
admin.site.register(Cost)  # 原価データ
admin.site.register(Price)  # 単価データ作成
admin.site.register(Span)  # 月別作業期間データ作成
admin.site.register(R_Order)  # 受注データ
admin.site.register(Order)  # 発注データ作成
admin.site.register(Worktime)  # 労働時間データ作成
admin.site.register(Sales)  # 売上データ作成
admin.site.register(Invoice)  # TODO 請求データ作成
admin.site.register(OSCost)  # TODO 外注データ作成ß
admin.site.register(Payment)  # TODO 支払データ作成
