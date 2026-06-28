

from textnode import TextNode, TextType


def main() -> None:
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)


main()


