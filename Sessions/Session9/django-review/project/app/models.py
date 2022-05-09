from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    n_hit = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.title)

    def update_counter(self):
        self.n_hit = self.n_hit + 1
        self.save()
    # """
    # Post 모델에는 제목과 내용 필드가 필요합니다.
    # *이때 제목은 50글자를 초과하여 작성할 수 없도록 합니다.
    # """
    # pass
