from django.urls import reverse
from rest_framework import test, status

from school.models import Course


class CourseTestCase(test.APITestCase):
    def setUp(self) -> None:
        self.list_url = reverse('Courses-list')
        self.course_1 = Course(
            cod='COD1', description='Course Test 1', level='E'
        )
        self.course_1.save()
        self.course_2 = Course(
            cod='COD2', description='Course Test 2', level='M'
        )
        self.course_2.save()

    # def test_failed(self):
    #     self.fail('Test failed!!!')

    def test_request_to_get_list_courses(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_request_to_post_create_course(self):
        data = {
            'cod': 'COD3',
            'description': 'Course Test 3',
            'level': 'H',
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_request_to_put_update_course(self):
        data = {
            'cod': 'COD1',
            'description': 'Course Test 1 Updated',
            'level': 'H',
        }
        response = self.client.put('/courses/1/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_request_to_delete_have_not_permission_for_destroy_course(self):
        data = {'id': '1'}
        response = self.client.delete(self.list_url, data=data)
        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)
