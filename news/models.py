from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.FloatField(default=0.00)


    def update_rating(self):
        total_rating = 0
        for post in Post.objects.filter(author=self):
            total_rating += post.rating * 3
        for comment in Comment.objects.filter(author=self):
            total_rating += comment.rating
        return total_rating
        # for comment in Comment.objects.filter()

        # #суммарный рейтинг каждой статьи автора умножается на 3

        # #суммарный рейтинг всех комментариев автора;

        # #суммарный рейтинг всех комментариев к статьям автора.


    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Category(models.Model):  #статья или новость
    name = models.CharField(max_length=100, unique=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Post(models.Model):
    news = "NE"
    articles = "AR"

    POST_TYPES = [
        (news, 'Новость'),
        (articles, 'Статья')
    ]

    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор')
    post_type = models.CharField(max_length=100, choices=POST_TYPES, default=news, verbose_name='Тип поста')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Описание')
    rating = models.FloatField(default=0.00, verbose_name='Рейтинг')


    def like(self):
        self.rating += 1
        self.save()


    def dislike(self):
        self.rating -= 1
        self.save()


    def preview(self):
        return self.text[:124] + '...'


    def get_absolute_url(self):
        return reverse('news:post_detail', args=[str(self.pk)])



    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='categories')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.category.name


    class Meta:
        verbose_name = 'Категория поста'
        verbose_name_plural = 'Категории постов'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    date_create = models.DateTimeField(auto_now_add=True)
    rating = models.FloatField(default=0.00)


    def like(self):
        self.rating += 1
        self.save()


    def dislike(self):
        self.rating -= 1
        self.save()


    def __str__(self):
        return self.text


    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Subscribers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sub_categories')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, related_name='sub_users')

    def __str__(self):
        return f'{self.user.username}, {self.category}'


    class Meta:
        verbose_name = 'Подписку'
        verbose_name_plural = 'Подписки'


