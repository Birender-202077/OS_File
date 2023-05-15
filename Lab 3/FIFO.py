class FIFO:
    def __init__(self, size):
        self.size = size    # max. pages that the memory can hold
        self.queue = []     # hols page IDs in memory.

# This method checks if a given page ID is present in the memory,
    def page_fault(self, page_id):
        return page_id not in self.queue

# This method adds a page to the memory by appending it to the end of the list
    def add_page(self, page_id):
        if len(self.queue) < self.size:
            self.queue.append(page_id)
        else:
            self.queue.pop(0)
            self.queue.append(page_id)

fifo = FIFO(size=3)

pages = [1, 2, 3, 4, 5, 6, 7, 8, 7, 8, 9, 3, 9, 5, 4, 1]

for page in pages:
    if fifo.page_fault(page):
        print("Page fault:", page)
        fifo.add_page(page)
    else:
        print("Page hit:", page)

print("Pages in memory:", fifo.queue)
