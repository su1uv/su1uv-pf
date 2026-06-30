from extract_markdown_images import extract_markdown_links, extract_markdown_images
from textnode import TextNode, TextType


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    splitted: list[TextNode] = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN_TEXT:
            splitted.append(node)
            continue
        matches: list[tuple[str, str]] = extract_markdown_images(node.text)
        if len(matches) == 0:
            splitted.append(node)
            continue

        temp_text : str = node.text
        for match in matches:
            temp_list: list[str] = temp_text.split(f"![{match[0]}]({match[1]})", 1)
            if temp_list[0] != "":
                splitted.append(TextNode(temp_list[0], TextType.PLAIN_TEXT))
            splitted.append(TextNode(match[0], TextType.IMAGE, match[1]))
            temp_text = "".join(temp_list[1:])

        if temp_text != "":
            splitted.append(TextNode(temp_text, TextType.PLAIN_TEXT))

    return splitted



def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    splitted: list[TextNode] = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN_TEXT:
            splitted.append(node)
            continue
        matches: list[tuple[str, str]] = extract_markdown_links(node.text)
        if len(matches) == 0:
            splitted.append(node)
            continue

        temp_text : str = node.text
        for match in matches:
            temp_list: list[str] = temp_text.split(f"[{match[0]}]({match[1]})", 1)
            if temp_list[0] != "":
                splitted.append(TextNode(temp_list[0], TextType.PLAIN_TEXT))
            splitted.append(TextNode(match[0], TextType.LINK, match[1]))
            temp_text = "".join(temp_list[1:])

        if temp_text != "":
            splitted.append(TextNode(temp_text, TextType.PLAIN_TEXT))

    return splitted
