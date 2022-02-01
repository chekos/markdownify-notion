from markdownify_notion import markdownify_block
from blocks import PARAGRAPH, BOOKMARK, CODE, HEADING_1, HEADING_2, HEADING_3, DIVIDER
from tests.blocks import IMAGE


def test_markdownify_block_paragraph():
    assert (
        markdownify_block(PARAGRAPH)
        == "I wonder if the _markdown_ works - or **how** it looks like in the json returned."
    )


def test_markdownify_block_bookmark():
    assert (
        markdownify_block(BOOKMARK)
        == "[github.com/stedolan/jq/issues/124](https://github.com/stedolan/jq/issues/124#issuecomment-17875972)\n"
    )


def test_markdownify_block_code():
    assert (
        markdownify_block(CODE)
        == '```json\n{\n\tid: "123",\n\ttitle: "page 1",\n\tcreated: "2022-01-25T23:15:00.000Z"\n}\n{\n\tid: "124",\n\ttitle: "page 2",\n\tcreated: "2022-01-26T13:18:15.000Z"\n}\n{\n\tid: "125",\n\ttitle: "page 3",\n\tcreated: "2022-01-27T18:37:05.000Z"\n}\n```'
    )


def test_markdownify_block_headings():
    assert markdownify_block(HEADING_1) == "# what i learned"
    assert markdownify_block(HEADING_2) == "## what i learned"
    assert markdownify_block(HEADING_3) == "### what i learned"


def test_markdownify_block_divider():
    assert markdownify_block(DIVIDER) == "\n***\n"


def test_markdownify_block_image():
    assert (
        markdownify_block(IMAGE)
        == "\n![image](https://website.domain/images/image.png)\n"
    )
