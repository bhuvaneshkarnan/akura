import os
import re
import urllib.parse

with open('shared.min.css', 'r', encoding='utf-8') as f:
    css = f.read()

def replace_font_url(m):
    url = m.group(1)
    filename = urllib.parse.unquote(os.path.basename(url))
    return f'url("fonts/{filename}")'

new_css = re.sub(r'url\((https://cdn\.prod\.website-files\.com/[^)]+\.woff2)\)', replace_font_url, css)

with open('shared.min.css', 'w', encoding='utf-8') as f:
    f.write(new_css)

print('Successfully localized font URLs in shared.min.css')
