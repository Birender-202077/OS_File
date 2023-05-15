class LFUPageReplacement:
    def __init__(self, frame_count):
        self.frame_count = frame_count
        self.page_frames = [] # list of page frames that are currently in memory
        self.page_count = {} # dictionary that stores the number of times each page has been referenced.
    
    def page_fault(self, page):
        if page in self.page_frames:
            self.page_count[page] += 1
            return False
        if len(self.page_frames) < self.frame_count:
            self.page_frames.append(page)
            self.page_count[page] = 1
            return True
        else:
            lfu_page = min(self.page_frames, key=lambda p: self.page_count[p])
            self.page_frames.remove(lfu_page)
            del self.page_count[lfu_page]
            self.page_frames.append(page)
            self.page_count[page] = 1
            return True

lfu = LFUPageReplacement(4)  # initialize with 4 page frames
page_requests = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5, 2, 3, 4, 5]

page_fault_count = 0
for page in page_requests:
    if lfu.page_fault(page):
        page_fault_count += 1
    print(f"Page request: {page}, Page frames: {lfu.page_frames}, Page count: {lfu.page_count}")

print(f"Total page faults: {page_fault_count}")
