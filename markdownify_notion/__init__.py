from urllib.parse import urlparse


SUPPORTED_BLOCKS = [
    "heading_1",
    "heading_2",
    "heading_3",
    "paragraph",
    "bookmark",
    "code",
    "divider",
    "image",
    "numbered_list_item",
    "bulleted_list_item",
]


def markdownify_block(block: dict) -> str:
    """Markdownifies a Notion block extracting it's contents and
    adding the markdown syntax surrounding the plain text.

    Parameters
    ----------
    block : dict
        A Notion block. These are obtained through the Notion API
        when requesting a Page object's contents.
        A list of block types can be found at:

    Returns
    -------
    str
        A string with the block's contents in markdown syntax.
    """

    _type = block["type"]
    _content = block[_type]

    if _type not in SUPPORTED_BLOCKS:
        return ""

    # Non-text types
    if _type == "bookmark":
        _url = _content["url"]
        _, netloc, path, *_ = urlparse(_url)
        return f"[{netloc + path}]({_content['url']})\n"

    if _type == "divider":
        return "\n***\n"

    if _type == "image":
        _hosted_local = _content["type"]
        _url = _content[_hosted_local]["url"]
        _, netloc, path, *_ = urlparse(_url)
        _name = path.split("/")[-1].split(".")[0]
        return f"\n![{_name}]({_url})\n"

    # Text types
    _text_objs = _content.get("rich_text", [])
    md_text = ""
    _text_chunks = []

    for element in _text_objs:
        md_text = element["plain_text"].strip()
        annotations = element["annotations"]
        if annotations["bold"]:
            md_text = f"**{md_text}**"
        if annotations["italic"]:
            md_text = f"_{md_text}_"
        if annotations["strikethrough"]:
            md_text = f"~~{md_text}~~"
        if annotations["code"]:
            md_text = f"`{md_text}`"

        _text_chunks.append(md_text)

    if "heading" in _type:
        n_heading = int(_type.split("_")[-1])
        _text_chunks.insert(0, f"{'#' * n_heading}")

    if _type == "code":
        _language = _content["language"]
        _text_chunks.insert(0, f"```{_language}\n")
        _text_chunks.append("\n```")
        return "".join(_text_chunks)

    if _type == "bulleted_list_item":
        return "* " + " ".join(_text_chunks)
    if _type == "numbered_list_item":
        return "1. " + " ".join(_text_chunks)

    return " ".join(_text_chunks)
