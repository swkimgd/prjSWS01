from django.db import models
from datetime import date

# Create your models here.

# M_POSITION 테이블에 해당: 직책 마스터 데이터
class Position(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='役職名')

    def __str__(self):
        return self.name

# M_GROUP 테이블에 해당: 팀명 마스터 데이터
class Group(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='チーム名')

    def __str__(self):
        return self.name
    
# T_MEMBER 테이블에 해당: 회원 정보
class Member(models.Model):
    email = models.EmailField(unique=True, verbose_name='メールアドレス')
    first_name = models.CharField(max_length=50, verbose_name='名')
    last_name = models.CharField(max_length=50, verbose_name='性')
    birthday = models.DateField(verbose_name='生年月日', null=True, blank=True) # null, blank 허용
    employ_date = models.DateField(verbose_name='入社日')
    position = models.ForeignKey(Position, on_delete=models.PROTECT, verbose_name='役職')
    group = models.ForeignKey(Group, on_delete=models.PROTECT, verbose_name='チーム')

    def __str__(self):
        # 관리자 페이지 등에서 객체를 표시할 때 사용할 이름
        return f'{self.last_name} {self.first_name}'

    @property
    def age(self):
        """생년월일을 기반으로 만 나이를 계산합니다."""
        if not self.birthday:
            return None
        today = date.today()
        return today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))

    @property
    def experience_years(self):
        """입사일을 기반으로 만 근무 년차를 계산합니다."""
        today = date.today()
        return today.year - self.employ_date.year - ((today.month, today.day) < (self.employ_date.month, self.employ_date.day))