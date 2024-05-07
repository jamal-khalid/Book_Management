from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    publication_date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

# class ReadingList(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     name = models.CharField(max_length=255)
#     books = models.ManyToManyField('Book', through='ReadingListEntry')

class ReadingList(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book, through='ReadingListEntry')

    def add_book(self, book, order):
        # Create ReadingListEntry with the provided book and order
        ReadingListEntry.objects.create(reading_list=self, book=book, order=order)


class ReadingListEntry(models.Model):
    reading_list = models.ForeignKey(ReadingList, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    order = models.IntegerField()

    class Meta:
        unique_together = ('reading_list', 'book')  # 
# class ReadingListEntry(models.Model):
#     reading_list = models.ForeignKey(ReadingList, on_delete=models.CASCADE)
#     book = models.ForeignKey('Book', on_delete=models.CASCADE)
#     order = models.PositiveIntegerField()


# class ReadingList(models.Model):
#     user = models.ForeignKey(CustomUser, related_name='reading_lists', on_delete=models.CASCADE)
#     name = models.CharField(max_length=255)
#     books = models.ManyToManyField(Book, related_name='reading_lists', through='ReadingListItem')

#     def __str__(self):
#         return self.name

# class ReadingListItem(models.Model):
#     reading_list = models.ForeignKey(ReadingList, on_delete=models.CASCADE)
#     book = models.ForeignKey(Book, on_delete=models.CASCADE)
#     order = models.PositiveIntegerField()

#     class Meta:
#         unique_together = ('reading_list', 'book')
#         ordering = ['order']

#     def __str__(self):
#         return f'{self.reading_list.name} - {self.book.title}'


