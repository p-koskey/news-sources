import unittest
from models import source

Source = source.Source

class  SourceTest(unittest.TestCase):
    '''
    Testing behaviour of source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every test
        '''
        self.news_source = Source('abc-news','ABC News', 'https://abcnews.go.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.news_source,Source))


if __name__ == '__main__':
    unittest.main()