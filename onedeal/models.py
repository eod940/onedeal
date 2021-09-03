from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import User


class LandingApply(models.Model):
    apply_name = models.CharField(max_length=30, verbose_name="이름")
    apply_phonenum = models.CharField(max_length=30, verbose_name="전화번호")
    apply_email = models.EmailField(max_length=128, verbose_name="이메일 주소")
    apply_birth = models.CharField(max_length=30, verbose_name="생년월일")
    apply_content = models.TextField(verbose_name="상세내용")

    apply_created = models.DateTimeField(auto_now_add=True, verbose_name="생성일자")

    CHOICES = {
        ('진행중', '진행중'),
        ('완료', '완료'),
    }
    apply_check = models.CharField(max_length=20 , choices=CHOICES, default='진행중', null=True, verbose_name="상담여부")

    def __str__(self):
        return "[{}] - {}::{}".format(self.apply_check, self.apply_name, self.apply_birth)

    def get_absolute_url(self):
        return '/onedeal/'

    class Meta:
        verbose_name = "주문서 확인"
        verbose_name_plural = "주문서 확인"


class Post(models.Model):
    post_title = models.CharField(max_length=30, verbose_name="제목")
    post_content = models.TextField(verbose_name="내용")

    post_created = models.DateTimeField(auto_now_add=True, verbose_name="생성일자")
    post_author = models.ForeignKey(User, verbose_name="글쓴이", on_delete=models.CASCADE)  # 유저 삭제시 모두 삭제

    def __str__(self):
        return "{}::{}".format(self.post_title, self.post_author)

    class Meta:
        verbose_name = "게시글 확인"
        verbose_name_plural = "게시글 확인"


class Item(models.Model):
    item_title = models.CharField(max_length=30, verbose_name="기기고유번호")
    item_name = models.CharField(max_length=30, verbose_name="기기명")
    item_quantity = models.IntegerField(verbose_name="수량", validators=[MinValueValidator(1)])
    item_price = models.IntegerField(verbose_name="가격", validators=[MinValueValidator(1)])
    item_content = models.TextField(verbose_name="세부설명")

    item_img = models.ImageField(upload_to='onedeal/%Y/%m/%d', blank=True, verbose_name="기기 이미지")
    item_content_img = models.ImageField(upload_to='onedeal/contentImg/%Y/%m/%d', blank=True, verbose_name="상세페이지")

    item_created = models.DateTimeField(auto_now_add=True, verbose_name="생성일자")

    def __str__(self):
        return "{}::{}".format(self.item_title, self.item_name)

    class Meta:
        verbose_name = "모바일기기 "
        verbose_name_plural = "기기확인"


# class MainAdvertisement(models.Model):
#     adm_img = models.ImageField(upload_to='onedeal/%Y/%m/%d', blank=True, verbose_name="제목")
#     adm_content = models.TextField(verbose_name="식별용 내용")
#
#     adm_created = models.DateTimeField(verbose_name="생성일자")
#
#     def __str__(self):
#         return "{}::{}".format(self.ad_content, self.ad_created)
#
#     class Meta:
#         verbose_name = "메인광고 이미지"
#         verbose_name_plural = "메인광고 이미지"


# class SubAdvertisement(models.Model):
#     ads_img = models.ImageField(upload_to='onedeal/%Y/%m/%d', blank=True, verbose_name="제목")
#     ads_title = CharField(max_length=30, verbose_name="제목")
#     ads_content = models.TextField(verbose_name="내용")
#
#     ads_created = models.DateTimeField(verbose_name="생성일자")
#
#     def __str__(self):
#         return "{}::{}".format(self.ad_content, self.ad_created)
#
#     class Meta:
#         verbose_name = "메인광고 이미지"
#         verbose_name_plural = "메인광고 이미지"
