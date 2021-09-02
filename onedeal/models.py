from django.db import models
from django.contrib.auth.models import User


class LandingApply(models.Model):
    apply_name = models.CharField(max_length=30, verbose_name="이름")
    apply_phonenum = models.CharField(max_length=30, verbose_name="전화번호")
    apply_email = models.EmailField(max_length=128, verbose_name="이메일 주소")
    apply_birth = models.CharField(max_length=30, verbose_name="생년월일")
    apply_content = models.TextField(verbose_name="상세내용")

    apply_created = models.DateTimeField(verbose_name="생성일자")

    class Meta:
        verbose_name = "주문서 확인"
        verbose_name_plural = "주문서 확인"


class Post(models.Model):
    post_title = models.CharField(max_length=30, verbose_name="제목")
    post_content = models.TextField(verbose_name="내용")

    post_created = models.DateTimeField(verbose_name="생성일자")
    post_author = models.ForeignKey(User, verbose_name="글쓴이", on_delete=models.CASCADE)  # 유저 삭제시 모두 삭제

    class Meta:
        verbose_name = "게시글 확인"
        verbose_name_plural = "게시글 확인"
