from markdownify_notion import markdownify_block
from blocks import PARAGRAPH, BOOKMARK, CODE


def test_markdownify_block_paragraph():
    assert (
        markdownify_block(PARAGRAPH)
        == "I wonder if the _markdown_ works - or **how** it looks like in the json returned."
    )


def test_markdownify_block_bookmark():
    assert (
        markdownify_block(BOOKMARK)
        == "[github.com/stedolan/jq/issues/124](https://github.com/stedolan/jq/issues/124#issuecomment-17875972)"
    )


def test_markdownify_block_code():
    assert (
        markdownify_block(CODE)
        == '```json\n {\n\tid: "123",\n\ttitle: "page 1",\n\tcreated: "2022-01-25T23:15:00.000Z"\n}\n{\n\tid: "124",\n\ttitle: "page 2",\n\tcreated: "2022-01-26T13:18:15.000Z"\n}\n{\n\tid: "125",\n\ttitle: "page 3",\n\tcreated: "2022-01-27T18:37:05.000Z"\n} \n```'
    )
