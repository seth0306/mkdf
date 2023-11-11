from django.db import models


# 住所データ
class Address(models.Model):
    """_summary_
    住所データ
    Args:
        models (_type_): _description_
    """

    # 郵便番号
    zip = models.CharField(max_length=7)
    # 都道府県
    pref = models.CharField(max_length=10)
    # 市区郡町村
    city = models.CharField(max_length=50)
    # 住所１
    address1 = models.CharField(max_length=100)
    # 住所２
    address2 = models.CharField(max_length=100, blank=True, null=False, default="")
    # 作成日時
    created_at = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)
    # 更新日時
    updated_at = models.DateTimeField(verbose_name="更新日時", auto_now=True)

    def __str__(self):
        return self.zip + " " + self.pref + self.city + self.address1 + self.address2


# 会社データ
class Company(models.Model):
    """_summary_
    会社データ
    Args:
        models (_type_): _description_
    """

    # 会社名
    name = models.CharField(max_length=200)
    # 住所
    address = models.ForeignKey(
        Address,
        on_delete=models.CASCADE,
        verbose_name="住所",
    )
    # 適格請求者番号
    claimant_number = models.CharField(max_length=14, blank=True, null=True)
    # 作成日時
    created_at = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)
    # 更新日時
    updated_at = models.DateTimeField(verbose_name="更新日時", auto_now=True)

    def __str__(self):
        return self.name


# プロジェクトデータ
class Project(models.Model):
    """_summary_
    プロジェクトデータ
    Args:
        models (_type_): _description_
    """

    # 対象会社
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    # プロジェクト名称
    name = models.CharField(verbose_name="プロジェクト名称", max_length=200)
    # 開始年月
    start_date = models.DateField(verbose_name="開始日")
    # 終了年月
    end_date = models.DateField(verbose_name="終了日")
    # 版数　修正するごとに１増加
    version = models.IntegerField(verbose_name="版数", default=0)
    # 作成日時
    created_at = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)
    # 更新日時
    updated_at = models.DateTimeField(verbose_name="更新日時", auto_now=True)

    def __str__(self):
        return self.company.name + " " + self.name


# 要員データ
class Person(models.Model):
    """_summary_
    要員データ
    Args:
        models (_type_): _description_
    """

    # 姓
    last_name = models.CharField(max_length=200)
    # 名
    first_name = models.CharField(max_length=200)
    # 姓　カナ
    kana_last_name = models.CharField(max_length=200)
    # 名　カナ
    kana_first_name = models.CharField(max_length=200)
    # 所属会社
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    # メールアドレス
    email = models.EmailField(max_length=200)
    # 連絡先電話番号
    phone = models.CharField(max_length=200)
    # 作成日時
    created_at = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)
    # 更新日時
    updated_at = models.DateTimeField(verbose_name="更新日時", auto_now=True)

    def __str__(self):
        return self.last_name + " " + self.first_name


# プロジェクト要員データ
class ProjectPerson(models.Model):
    """_summary_
    要員データ
    Args:
        models (_type_): _description_
    """

    # プロジェクト
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    # 要員
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    # 作成日時
    created_at = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)
    # 更新日時
    updated_at = models.DateTimeField(verbose_name="更新日時", auto_now=True)

    def __str__(self):
        return self.last_name + " " + self.first_name


# プロジェクト工数データ
class ProjectEffort(models.Model):
    """_summary_
    作業量を管理するテーブル。人月にて入力
    Args:
        models (_type_): _description_
    """

    # 対象プロジェクト
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    # 対象年月　月を操作する場合は1日を設定
    target_month = models.DateField(verbose_name="対象年月")
    # 計画工数（人月）　最大9999.9
    budget＿effort = models.DecimalField(
        verbose_name="計画工数", max_digits=5, decimal_places=1
    )
    # 実績工数人月（人月）　最大9999.9
    actual_effort = models.DecimalField(
        verbose_name="実績工数", max_digits=5, decimal_places=1
    )
    # 版数　修正するごとに１増加
    version = models.IntegerField(verbose_name="版数", default=0)
    # 作成日時
    created_at = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)
    # 更新日時
    updated_at = models.DateTimeField(verbose_name="更新日時", auto_now=True)


# 原価データ
class Cost(models.Model):
    """_summary_
    原価データ
    Args:
        models (_type_): _description_
    """

    # 対象要員
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    # 対象年月
    target_month = models.DateField(verbose_name="対象年月")
    # 原価
    cost_price = models.IntegerField(verbose_name="原価")
    # 版数　修正するごとに１増加
    version = models.IntegerField(verbose_name="版数", default=0)
    # 作成日時
    created_at = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)
    # 更新日時
    updated_at = models.DateTimeField(verbose_name="更新日時", auto_now=True)


# 単価データ作成
class Price(models.Model):
    """_summary_
    単価データ
    Args:
        models (_type_): _description_
    """

    # 単価名称
    name = models.CharField(verbose_name="単価名称", max_length=200)
    # 月額単価
    base_price = models.IntegerField(verbose_name="月額単価")
    # 超過単価
    deduct_price = models.IntegerField(verbose_name="超過単価")
    # 控除単価
    excess_price = models.IntegerField(verbose_name="控除単価")
    # 基準労働時間
    base_work_hour = models.DecimalField(
        verbose_name="基準労働時間", max_digits=5, decimal_places=2
    )
    # 上限時間
    max_work_hour = models.DecimalField(
        verbose_name="上限時間", max_digits=5, decimal_places=2
    )
    # 下限時間
    min_work_hour = models.DecimalField(
        verbose_name="下限時間", max_digits=5, decimal_places=2
    )

    # 作成日時
    created_at = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)
    # 更新日時
    updated_at = models.DateTimeField(verbose_name="更新日時", auto_now=True)


# 月別作業期間データ作成
class Span(models.Model):
    """_summary_
    月別作業期間データ
    Args:
        models (_type_): _description_
    """

    # 月別作業期間名称
    name = models.CharField(verbose_name="単価名称", max_length=200)
    # 作業開始日
    start_date = models.DateField(verbose_name="作業開始日")
    # 作業終了日
    end_date = models.DateField(verbose_name="作業終了日")

    # 作成日時
    created_at = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)
    # 更新日時
    updated_at = models.DateTimeField(verbose_name="更新日時", auto_now=True)


# 受注データ
class R_Order(models.Model):
    """_summary_
    受注データ
    Args:
        models (_type_): _description_
    """

    # 受注元会社
    client = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        verbose_name="受注元",
    )
    # 受注元注文番号
    client_order_no = models.CharField(verbose_name="注文番号", max_length=200)
    # 受注元業務名称
    business_desc = models.CharField(verbose_name="業務名称", max_length=200)
    # 要員名
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        verbose_name="要員",
    )
    # 作業期間
    span = models.ForeignKey(
        Span,
        on_delete=models.CASCADE,
        verbose_name="作業期間",
    )
    # 単価
    price = models.ForeignKey(
        Price,
        on_delete=models.CASCADE,
        verbose_name="単価",
    )
    # 締日
    due_date = models.DateField(verbose_name="締日")
    # 支払予定日
    payment_date = models.DateField(verbose_name="支払予定日")
    # 備考
    note = models.CharField(verbose_name="備考", max_length=200)
    # ステータス
    status = models.IntegerField(verbose_name="ステータス")
    # 作成日時
    created_at = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)
    # 更新日時
    updated_at = models.DateTimeField(verbose_name="更新日時", auto_now=True)


# 発注データ作成
class Order(models.Model):
    """_summary_
    発注データ
    Args:
        models (_type_): _description_
    """

    # 発注先会社
    associated_order = models.ForeignKey(
        R_Order,
        on_delete=models.CASCADE,
        verbose_name="受注データ",
    )
    # 発注先会社
    supplier = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        verbose_name="発注先",
    )
    # 注文番号
    client_order_no = models.CharField(verbose_name="注文番号", max_length=200)
    # 業務名称
    business_desc = models.CharField(verbose_name="業務名称", max_length=200)
    # 要員名
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        verbose_name="要員",
    )
    # 作業期間
    span = models.ForeignKey(
        Span,
        on_delete=models.CASCADE,
        verbose_name="作業期間",
    )
    # 単価
    price = models.ForeignKey(
        Price,
        on_delete=models.CASCADE,
        verbose_name="単価",
    )
    # 締日
    due_date = models.DateField(verbose_name="締日")
    # 支払予定日
    payment_date = models.DateField(verbose_name="支払予定日")
    # 備考
    note = models.CharField(verbose_name="備考", max_length=200)
    # ステータス
    status = models.IntegerField(verbose_name="ステータス")
    # 作成日時
    created_at = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)
    # 更新日時
    updated_at = models.DateTimeField(verbose_name="更新日時", auto_now=True)


# 労働時間データ作成
class Worktime(models.Model):
    """_summary_
    労働時間データ
    Args:
        models (_type_): _description_
    """

    # 要員名
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        verbose_name="要員",
    )
    # 作業期間
    span = models.ForeignKey(
        Span,
        on_delete=models.CASCADE,
        verbose_name="作業期間",
    )
    # 作業時間
    work_hour = models.DecimalField(verbose_name="作業時間", max_digits=5, decimal_places=2)

    # 作成日時
    created_at = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)
    # 更新日時
    updated_at = models.DateTimeField(verbose_name="更新日時", auto_now=True)


# 売上データ作成
class Sales(models.Model):
    """_summary_
    売上データ
    Args:
        models (_type_): _description_
    """

    # 受注
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        verbose_name="受注",
    )
    # 作業時間
    worktime = models.ForeignKey(
        Worktime,
        on_delete=models.CASCADE,
        verbose_name="作業時間",
    )

    # 作成日時
    created_at = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)
    # 更新日時
    updated_at = models.DateTimeField(verbose_name="更新日時", auto_now=True)


# TODO 請求データ作成
class Invoice(models.Model):
    """_summary_
    請求データ
    Args:
        models (_type_): _description_
    """

    # 作成日時
    created_at = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)
    # 更新日時
    updated_at = models.DateTimeField(verbose_name="更新日時", auto_now=True)


# TODO 外注データ作成
class OSCost(models.Model):
    """_summary_
    外注データ
    Args:
        models (_type_): _description_
    """

    # 作成日時
    created_at = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)
    # 更新日時
    updated_at = models.DateTimeField(verbose_name="更新日時", auto_now=True)


# TODO 支払データ作成
class Payment(models.Model):
    """_summary_
    支払データ
    Args:
        models (_type_): _description_
    """

    # 作成日時
    created_at = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)
    # 更新日時
    updated_at = models.DateTimeField(verbose_name="更新日時", auto_now=True)
