import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node: HTMLNode = HTMLNode("p", "This is a test paragraph")
        node2: HTMLNode = HTMLNode("p", "This is a test paragraph")
        self.assertEqual(str(node), str(node2))

    def test_value_not_eq(self):
        node = HTMLNode("p", "This is not a test paragraph")
        node2 = HTMLNode("p", "This is a test paragraph")
        self.assertNotEqual(node.value, node2.value)

    def test_props_to_html(self):
        props: dict[str, str] = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode("a", "google here", props=props)
        formatted_props = node.props_to_html()
        self.assertEqual(
            formatted_props, ' href="https://www.google.com" target="_blank"'
        )


if __name__ == "__main__":
    unittest.main()
