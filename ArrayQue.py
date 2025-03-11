""" Sam want to read exactly ‘TARGET’ number of pages.

He has an array ‘BOOK’ containing the number of pages for ‘N’ books.

Return YES/NO, if it is possible for him to read any 2 books and he can meet his ‘TARGET’ number of pages. """

def can_read_target_pages(BOOK, TARGET):
    seen_pages = set()  
    for i in BOOK:
        seen_pages.add(i)
    
    
    for pages in BOOK:
        
        complement = TARGET - pages
        
        
        if complement in seen_pages:
            return "YES"
        
        
        
    
    return "NO"

