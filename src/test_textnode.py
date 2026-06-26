import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_url_none(self):
        node = TextNode("This text does not have a url", TextType.PLAIN_TEXT)
        self.assertEqual(node.url, None)

    def test_url_not_eq(self):
        node = TextNode("This text does not have a url", TextType.PLAIN_TEXT)
        node2 = TextNode(
            "This text does not have a url",
            TextType.PLAIN_TEXT,
            "https://www.mytesturl.com",
        )
        self.assertNotEqual(node, node2)

    def test_text_type_not_eq(self):
        node = TextNode("Test code", TextType.LINK)
        node2 = TextNode("Test code", TextType.BOLD_TEXT)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
