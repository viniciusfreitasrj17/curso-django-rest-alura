import datetime
import os
import random

import django
from faker import Faker
from validate_docbr import CPF

from school.models import Course, Matriculation, Student

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()


def criando_alunos(quantidade_de_pessoas):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(quantidade_de_pessoas):
        cpf = CPF()
        name = fake.name()
        rg = "{}{}{}{}".format(random.randrange(10, 99), random.randrange(
            100, 999), random.randrange(100, 999), random.randrange(0, 9))
        cpf = cpf.generate()
        birth_day = fake.date_between(
            start_date='-18y', end_date='today')
        s = Student(name=name, rg=rg, cpf=cpf, birth_day=birth_day)
        s.save()


def criando_cursos(quantidade_de_cursos):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(quantidade_de_cursos):
        cod = "{}{}-{}".format(random.choice("ABCDEF"),
                               random.randrange(10, 99), random.randrange(1, 9))
        descs = ['Python Fundamentos', 'Python intermediário',
                 'Python Avançado', 'Python para Data Science', 'Python/React']
        description = random.choice(descs)
        descs.remove(description)
        level = random.choice("BIA")
        c = Course(cod=cod, description=description, level=level)
        c.save()


criando_alunos(200)
criando_cursos(5)
