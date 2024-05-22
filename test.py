import unittest
from main import analiz
import codecs

class TextAnalizing(unittest.TestCase):

  def test_text1(self):
      with codecs.open('test_texts/text1.txt', 'r', 'utf-8') as f:
          file_content = f.read()
      self.assertEqual(('и', 65), analiz(file_content))


  def test_text2(self):
      with codecs.open('test_texts/text2.txt', 'r', 'utf-8') as f:
          file_content = f.read()
      self.assertEqual(('когда-либо', 12), analiz(file_content))


  def test_text3(self):
      with codecs.open('test_texts/text3.txt', 'r', 'utf-8') as f:
          file_content = f.read()
      self.assertEqual(('и', 28), analiz(file_content))


if __name__ == '__main__':
    unittest.main()