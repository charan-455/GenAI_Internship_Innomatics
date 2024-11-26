import re

def remove_markdown(markdown_text):

    if not isinstance(markdown_text, str):
        raise TypeError("Expected a string, but got {}".format(type(markdown_text)))

    # Remove headers (e.g., # Header 1, ## Header 2, etc.)
    markdown_text = re.sub(r'^(#{1,6})\s*', '', markdown_text, flags=re.MULTILINE)

    # Remove bold and italic markdown (e.g., **bold**, *italic*, or combinations like ***bold+italic***)
    markdown_text = re.sub(r'(\*\*|\*|__|_)(.*?)\1', r'\2', markdown_text)

    # Remove links (e.g., [text](http://example.com))
    markdown_text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', markdown_text)

    # Remove images (e.g., ![alt text](image.jpg))
    markdown_text = re.sub(r'!\[([^\]]*)\]\([^\)]+\)', r'\1', markdown_text)

    # Remove code blocks (e.g., ```code block```)
    markdown_text = re.sub(r'```[\s\S]*?```', '', markdown_text)

    # Remove inline code (e.g., `code`)
    markdown_text = re.sub(r'`([^`]+)`', r'\1', markdown_text)

    # Remove unordered lists (e.g., - item, * item, + item)
    markdown_text = re.sub(r'^[\*\-\+]\s+', '', markdown_text, flags=re.MULTILINE)

    # Remove ordered lists (e.g., 1. item)
    markdown_text = re.sub(r'^\d+\.\s+', '', markdown_text, flags=re.MULTILINE)

    # Remove horizontal rules (e.g., --- or *** or ___)
    markdown_text = re.sub(r'^[\*\-\_]{3,}', '', markdown_text, flags=re.MULTILINE)

    # Remove blockquotes (e.g., > quote)
    markdown_text = re.sub(r'^\>\s+', '', markdown_text, flags=re.MULTILINE)

    # Remove any stray markdown symbols (like `[]`, `{} etc.` that could have been missed)
    markdown_text = re.sub(r'[^\S\r\n]+', ' ', markdown_text)

    # Strip leading/trailing whitespace
    return markdown_text.strip()