import re

ALLOWED_TAGS_REGEX = re.compile(
    r'^(?:[^<]*|'
    r'<a\s+href="[^"]*"\s+title="[^"]*"\s*>[^<]*</a>|'
    r'<code>[^<]*</code>|'
    r'<i>[^<]*</i>|'
    r'<strong>[^<]*</strong>'
    r')*$'
)