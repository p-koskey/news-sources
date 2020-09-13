class Article:
    '''
    Article class to define article objects
    '''

    def __init__(self, name, author, title,  description, link, image, publishDate):

        self.name = name 
        self.author = author
        self.title = title
        self.description = description
        self.link = link
        self.image = image
        self.publishDate = publishDate