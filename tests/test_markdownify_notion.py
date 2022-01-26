from markdownify_notion import markdownify_block
from blocks import PARAGRAPH, BOOKMARK

def test_markdownify_block_paragraph():
    assert markdownify_block(PARAGRAPH) == "I wonder if the _markdown_ works - or **how** it looks like in the json returned."

def test_markdownify_block_bookmark():
    assert markdownify_block(BOOKMARK) == "[github.com/stedolan/jq/issues/124](https://github.com/stedolan/jq/issues/124#issuecomment-17875972)"