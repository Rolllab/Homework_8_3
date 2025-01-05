import pytest
from discipline import DisciplineTeacher

# def foo():
#     name = ['John', 'Jessica', 'Boris', 'James']
#     lastname = ['Deere', 'Parker', 'Swanson', 'Cooper']
#     education = ["Bachelor's Degree", "Bachelor's Degree", "Bachelor's Degree", "Bachelor's Degree"]
#     experience = [15, 7, 9, 3]
#     discipline = ['mathmatics', 'chemistry', 'computer since', 'dancing']
#     job_title = ['teacher', 'teacher', 'teacher', 'teacher']
#     for item in range(len(name)):
#         yield dict(
#             name=name[item],
#             lastname=lastname[item],
#             education=education[item],
#             experience=experience[item],
#             discipline=discipline[item],
#             job_title=job_title[item]
#         )


# @pytest.fixture
# def data():
#     return DisciplineTeacher(**next(foo()))

@pytest.fixture
def data():
    name = ['John', 'Jessica', 'Boris', 'James']
    lastname = ['Deere', 'Parker', 'Swanson', 'Cooper']
    education = ["Bachelor's Degree", "Bachelor's Degree", "Bachelor's Degree", "Bachelor's Degree"]
    experience = [15, 7, 9, 3]
    discipline = ['mathmatics', 'chemistry', 'computer science', 'dancing']
    job_title = ['teacher', 'teacher', 'teacher', 'teacher']

    # Создаем список всех объектов
    teachers = [
        DisciplineTeacher(
            name=name[item],
            lastname=lastname[item],
            education=education[item],
            experience=experience[item],
            discipline=discipline[item],
            job_title=job_title[item]
        )
        for item in range(len(name))
    ]

    # Возвращаем список всех объектов
    return teachers

