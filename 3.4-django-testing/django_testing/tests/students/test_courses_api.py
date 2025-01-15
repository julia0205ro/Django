import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Student, Course


@pytest.fixture()
def client():
    """Fixture for api-client."""
    return APIClient()


@pytest.fixture()
def course_factory():
    """Fixture for baked Course model."""
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


@pytest.fixture()
def student_factory():
    """Fixture for baked Student model."""
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


@pytest.mark.django_db
def test_get_courses(client, course_factory):
    """Retrieve the course list."""
    course = course_factory(_quantity=10)

    response = client.get('/api/v1/courses/')

    assert response.status_code == 200


@pytest.mark.django_db
def test_retrieve_course(client, course_factory):
    """Retrieve the specific course."""
    course = course_factory(_quantity=10)

    response = client.get(f'/api/v1/courses/{course[0].id}/', format='json')
    data = response.json()

    assert response.status_code == 200
    assert data['id'] == course[0].id


@pytest.mark.django_db
def test_course_list_filtering_by_id(client, course_factory):
    """Test course list filtering by id."""
    courses = course_factory(_quantity=10)
    filter_id = [course.id for course in courses]

    response = client.get('/api/v1/courses/', {'id': filter_id},
                          format='json')
    data = response.json()

    assert response.status_code == 200
    assert len(data) == len(filter_id)
    for obj in data:
        assert obj.get('id') in filter_id


@pytest.mark.django_db
def test_course_list_filtering_by_name(client, course_factory):
    """Test course list filtering by name."""
    courses = course_factory(_quantity=10)
    filter_name = [course.name for course in courses]

    response = client.get('/api/v1/courses/', {'name': filter_name},
                          format='json')
    data = response.json()

    assert response.status_code == 200
    for obj in data:
        assert obj.get('name') in filter_name


@pytest.mark.django_db
def test_course_creation(client):
    """Test for course creation."""
    course = {'name': 'course_name'}

    response = client.post('/api/v1/courses/', data=course)

    assert response.status_code == 201


@pytest.mark.django_db
def test_course_update(client, course_factory):
    """Test for course update."""
    course = course_factory()
    new_course_name = {'name': 'new_course_name'}

    response = client.put(f'/api/v1/courses/{course.id}/',
                          data=new_course_name, format='json')

    assert response.status_code == 200

    updated_course = Course.objects.get(id=course.id)
    assert updated_course.name == new_course_name.get('name')


@pytest.mark.django_db
def test_course_delete(client, course_factory):
    """Test for course delete."""
    course = course_factory()

    print(f'course = {course.id}')

    response = client.get('/api/v1/courses/')
    data = response.json()

    assert response.status_code == 200
    assert len(data) == 1

    response = client.delete(f'/api/v1/courses/{course.id}/')
    assert response.status_code == 204  # 301

