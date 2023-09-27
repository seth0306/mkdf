from django.db import models


# TODO 会社データ作成
class Company(models.Model):
    """_summary_
    会社データ
    Args:
        models (_type_): _description_
    """

    name = models.CharField(max_length=200)  # 会社名
    address = models.CharField(max_length=200)  # 住所

    created_at = models.DateTimeField(auto_now_add=True)  # 作成日時
    updated_at = models.DateTimeField(auto_now=True)  # 更新日時


# TODO 要員データ作成
class Person(models.Model):
    """_summary_
    要員データ
    Args:
        models (_type_): _description_
    """

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


# TODO 受注データ作成
class R_Order(models.Model):
    """_summary_
    受注データ
    Args:
        models (_type_): _description_
    """

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


# TODO 発注データ作成
class Order(models.Model):
    """_summary_
    発注データ
    Args:
        models (_type_): _description_
    """

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


# TODO 売上データ作成
class Sales(models.Model):
    """_summary_
    売上データ
    Args:
        models (_type_): _description_
    """

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


# TODO 請求データ作成
class Invoice(models.Model):
    """_summary_
    売上データ
    Args:
        models (_type_): _description_
    """

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


# TODO 外注データ作成
class OSCost(models.Model):
    """_summary_
    外注データ
    Args:
        models (_type_): _description_
    """

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


# TODO 支払データ作成
class Payment(models.Model):
    """_summary_
    支払データ
    Args:
        models (_type_): _description_
    """

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
