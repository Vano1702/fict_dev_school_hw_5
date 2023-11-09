class PaginationHelper:
    def __init__(self, items, ipp):
        self.items = items
        self.ipp = ipp  # items per page

    def page_count(self):
        return (len(self.items) // self.ipp) + 1 if len(self.items) % self.ipp else len(self.items) // self.ipp

    def item_count(self):
        return len(self.items)

    def page_item_count(self, page):
        if 0 <= page < self.page_count():
            return self.ipp if (page + 1) * self.ipp <= len(self.items) else self.ipp - ((page + 1) * self.ipp - len(self.items))
        else:
            return -1

    def page_index(self, ind):
        if 0 <= ind < len(self.items):
            return 0 if ind < self.ipp else ind // self.ipp
        else:
            return -1
