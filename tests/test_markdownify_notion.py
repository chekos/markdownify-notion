from markdownify_notion import markdownify_block


def test_markdownify_block():
    block = {
    'object': 'block',
    'id': '0abddae0-328b-4b38-93c1-a330935c21e9',
    'created_time': '2022-01-23T20:22:00.000Z',
    'last_edited_time': '2022-01-23T20:24:00.000Z',
    'has_children': False,
    'archived': False,
    'type': 'paragraph',
    'paragraph': {
        'text': [
            {
                'type': 'text',
                'text': {'content': 'I wonder if the ', 'link': None},
                'annotations': {
                    'bold': False,
                    'italic': False,
                    'strikethrough': False,
                    'underline': False,
                    'code': False,
                    'color': 'default'
                },
                'plain_text': 'I wonder if the ',
                'href': None
            },
            {
                'type': 'text',
                'text': {'content': 'markdown', 'link': None},
                'annotations': {
                    'bold': False,
                    'italic': True,
                    'strikethrough': False,
                    'underline': False,
                    'code': False,
                    'color': 'default'
                },
                'plain_text': 'markdown',
                'href': None
            },
            {
                'type': 'text',
                'text': {'content': ' works - or ', 'link': None},
                'annotations': {
                    'bold': False,
                    'italic': False,
                    'strikethrough': False,
                    'underline': False,
                    'code': False,
                    'color': 'default'
                },
                'plain_text': ' works - or ',
                'href': None
            },
            {
                'type': 'text',
                'text': {'content': 'how', 'link': None},
                'annotations': {
                    'bold': True,
                    'italic': False,
                    'strikethrough': False,
                    'underline': False,
                    'code': False,
                    'color': 'default'
                },
                'plain_text': 'how',
                'href': None
            },
            {
                'type': 'text',
                'text': {'content': ' it looks like in the json returned. ', 'link': None},
                'annotations': {
                    'bold': False,
                    'italic': False,
                    'strikethrough': False,
                    'underline': False,
                    'code': False,
                    'color': 'default'
                },
                'plain_text': ' it looks like in the json returned. ',
                'href': None
            }
        ]
    }
}
    assert markdownify_block(block) == "I wonder if the _markdown_ works - or **how** it looks like in the json returned."
