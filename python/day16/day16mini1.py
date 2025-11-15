class PaginationIterator:
    def __init__(self, items, page_size):
        self.items = items
        self.page_size = page_size
        self.current_page = 0
        self.total_pages = (len(items) - 1) // page_size + 1

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        """Go to next page"""
        if self.current_page < self.total_pages - 1:
            self.current_page += 1
            return self.get_page_items()
        else:
            raise StopIteration("No more next pages!")

    def prev(self):
        """Go to previous page"""
        if self.current_page > 0:
            self.current_page -= 1
            return self.get_page_items()
        else:
            raise StopIteration("No more previous pages!")

    def get_page_items(self):
        """Get items in the current page"""
        start = self.current_page * self.page_size
        end = start + self.page_size
        return self.items[start:end]

    def show_page(self):
        """Display current page with page number"""
        print(f"\nPage {self.current_page + 1}/{self.total_pages}")
        print(self.get_page_items())



items = ["A", "B", "C", "D", "E", "F", "G", "H"]
pager = PaginationIterator(items, page_size=3)

pager.show_page()

print(pager.next())
pager.show_page()

print(pager.next())
pager.show_page()

print(pager.prev())
pager.show_page()
