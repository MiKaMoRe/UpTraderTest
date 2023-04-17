from django import template
from django.template import RequestContext
from menu.models import Directory
from menu.services.tree_service import TreeService


register = template.Library()


@register.inclusion_tag('menu/shared/menu.html', takes_context=True)
def draw_menu(context: RequestContext, name: str):
    recursive_tree_raw_query = f'''
        WITH RECURSIVE directorytree AS (
        SELECT id, name, parent_id, is_root
        FROM menu_directory
        WHERE is_root IS true AND name LIKE '{name}'
        UNION ALL
        SELECT m.id, m.name, m.parent_id, m.is_root
        FROM menu_directory AS m
        INNER JOIN directorytree mtree ON mtree.id = m.parent_id
    )
    SELECT *
    FROM directorytree;
    '''.format(name=name)
    menu_tree = Directory.objects.raw(recursive_tree_raw_query)
    tree_service = TreeService(menu_tree, context['active_path'][1:].split('/'))
    root = tree_service.get_root()
    tree_service.prepare_data(root)
    return { 'menu_tree': menu_tree }
