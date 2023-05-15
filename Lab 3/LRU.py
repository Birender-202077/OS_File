class LRU:
    def __init__(self, size):
        self.size = size        # maximum number of pages that the memory can hold
        self.pages = []         # list that holds the page IDs in memory in the order they were added  
        self.access_times = {}  # keeps track of the last access time of each page in memory.


# This method checks if a given page ID is present in the memory,
    def page_fault(self, page_id):
        return page_id not in self.pages
    
# This method adds a page to the memory by appending it to the end of the list
    def add_page(self, page_id):
        if len(self.pages) < self.size:
            self.pages.append(page_id)
        else:
            lru_page = self.get_lru_page()
            self.pages.remove(lru_page)
            self.pages.append(page_id)

        self.access_times[page_id] = len(self.pages)

# This method returns the least recently used page by iterating over the pages list 
# and finding the page with the smallest value in the access_times dictionary

    def get_lru_page(self):
        lru_page = None      #initialize lrp to 0
        min_access_time = float('inf')      #initialize min. access time to infinity
        for page_id in self.pages:
            if self.access_times[page_id] < min_access_time:
                lru_page = page_id
                min_access_time = self.access_times[page_id]
        return lru_page



lru = LRU(size=3)

pages = [1, 2, 3, 4, 5, 6, 7, 8, 7, 8, 9, 3, 9, 5, 4, 1]

for page in pages:
    if lru.page_fault(page):
        print("Page fault:", page)
        lru.add_page(page)
    else:
        print("Page hit:", page)
        lru.access_times[page] = len(lru.pages)

print("Pages in memory:", lru.pages)
