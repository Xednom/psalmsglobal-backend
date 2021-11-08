import factory
from django.contrib.auth import get_user_model


User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = factory.Faker("first_name")
    username = factory.Sequence(lambda n: f"user{n}")
    email = factory.Sequence(lambda n: f"user{n}@example.com")