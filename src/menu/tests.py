from django.test import TestCase
from django.test import Client
from menu.services.tree_service import TreeService
from menu.models import Directory


class TreeServiceTestCase(TestCase):
    def setUp(self):
        self.active_dirs = ['root', 'directory']
        self.root = Directory.objects.create(name='root', is_root=True)
        self.directory = Directory.objects.create(name='directory', parent=self.root)
        self.subdir = Directory.objects.create(name='subdirectory', parent=self.directory)
        self.tree_service = TreeService(
            [self.directory, self.subdir, self.root], self.active_dirs
        )
    
    def test_get_root(self):
        self.assertEqual(self.tree_service.get_root(), self.root)
    
    def test_get_childs_of(self):
        self.assertEqual(self.tree_service.get_childs_of(self.directory), [self.subdir])
        self.assertEqual(self.tree_service.get_childs_of(self.root), [self.directory])

    def test_prepare_data(self):
        self.tree_service.prepare_data(self.root)
        self.assertEqual(self.root.url, '/panel/root/')
        self.assertEqual(self.directory.url, '/panel/root/directory/')
        self.assertEqual(self.subdir.url, '/panel/root/directory/subdirectory/')
        self.assertEqual(self.root.is_active, True)
        self.assertEqual(self.directory.is_active, True)
        with self.assertRaises(AttributeError):
            self.subdir.is_active


class RequestsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_root(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, '/panel')
