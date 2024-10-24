from django.db import models 
from django.utils.text import slugify
from django.utils.crypto import get_random_string

#회원정보 관련 모델 스키마 정의(스키마: 저장할 데이터의 구조를 강제하는 시스템적인 틀)
#장고에서는 코드개발시 모델을 객체 형식으로 다루게 되므로 SQL을 모르더라도 개발 가능
#하지만 실제적으로 구동시에는 장고가 자체적으로 table형식으로 변환해서 저장(ORM Object Related Mapping)
class Member(models.Model):
  #username이라는 filed에 문자열 30글자까지만 입력받을 수 있는 구조 강제처리
  #max_length로 지정가능한 문자최대길이 255
  username = models.CharField(max_length=30)
  age = models.IntegerField(null=True)
  date = models.DateField(null=True)


def __str__(self):
  return self.username




# 포스트 모델 생성 클래스
class Posts(models.Model):
  # 포스트 카테고리
  CATEGORY = (('BUSINESS', 'Business'), ('PERSONAL','Personal'),('IMPORTANT','Important'))

  # 포스트 모델 스키마 (제목, 본문, 슬러그, 카테고리, 포스트날짜, 수정날짜)
  title= models.CharField(max_length=100)
  body= models.TextField() 
  slug= models.SlugField(unique=True)
  category = models.CharField(max_length=15, choices=CATEGORY, default='PERSONAL')
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  # 포스트 제목 문자열 반환 메서드
  def __str__(self):
    return self.title

  # 슬러그 없을시 고유 슬러그 추가해서 포스트 모델 생성 메서드
  def save(self, *args, ** kwargs):
    if not self.slug:
      
      #추후 게시글 필터링할 때 필요한 기본 슬러그 생성
      slug_base = slugify(self.title)
      slug = slug_base

      #슬러그가 고유값인지 확인후 필요시 슬러그명 수정
      if Posts.objects.filter(slug=slug).exists():
        slug= f'{slug_base} - {get_random_string(5)}'
      self.slug = slug
    super(Posts, self).save(*args, **kwargs)