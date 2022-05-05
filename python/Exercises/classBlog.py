class Blog:

    def __init__(self, blog, number):
        self.blog = blog
        self.number = number
    
    def printBlog(self):
        print('Your blog: ')
        print(' ')
        print('Blog #', self.number)
        print(self.blog)

blog1 = Blog("how do you, how do you do, diziz ma blog, just trying thangs!", 1)
blog1.printBlog()