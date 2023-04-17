from django.db.models.query import RawQuerySet


class TreeService():
    def __init__(self, dirs: RawQuerySet, active_dirs: list=[]):
        self.dirs = dirs
        self.active_dirs = active_dirs
        self.root = self.get_root()
    
    def prepare_data(self, parent, depth=0, url='/panel/'):
        """
            Recursive preparing directories to render
        """
        url += (parent.name + '/')
        parent.url = url # Set directory url
        childs = self.get_childs_of(parent)
        if (len(self.active_dirs) > depth and
            self.active_dirs[depth] == parent.name):
            parent.is_active = True
        if not len(childs):
            return
        for child in childs:
            self.prepare_data(child, depth + 1, url)

    def get_childs_of(self, target_dir: RawQuerySet):
        """
            Getting childs of target dir
        """
        childs = []
        for directory in self.dirs:
            if directory.parent_id == target_dir.id:
                childs.append(directory)
        return childs
    
    def get_root(self):
        """
            Getting root directory
        """
        for directory in self.dirs:
            if directory.is_root:
                return directory
