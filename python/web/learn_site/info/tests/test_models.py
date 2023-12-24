import django

django.setup()

from info.models import Pages

class TestPage:
    def test_create(self):
        title = "hello"
        data = """
            This is sample data
        """

        new_id = Pages.add_page(title=title, data=data)

        assert Pages.objects.get(id=new_id).title == title