from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # Оставляем возможность расширения
    pass

    @property
    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)
