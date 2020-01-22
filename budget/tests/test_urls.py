from django.test import SimpleTestCase
from django.urls import resolve, reverse
from budget.views import project_list, project_detail, ProjectCreateView
 
class TestUrls(SimpleTestCase):
    def test_list_urls_resolves(self):
        url = reverse('list')
        self.assertEquals(resolve(url).func, project_list)

    def test_projectcreate_addurls_resolves(self):
        url = reverse('add')
        self.assertEquals(resolve(url).func.view_class, ProjectCreateView)

    def test_details_urls_resolves(self):
        url = reverse('detail', args=['some_slug'])
        self.assertEquals(resolve(url).func, project_detail)