"""Check generated pages, internal links and public artifact boundaries."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import json
import re

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / 'docs'

class Page(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.ids, self.links, self.h1 = set(), [], 0
        self.feed(source)
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            assert a['id'] not in self.ids, f'Duplicate id: {a["id"]}'
            self.ids.add(a['id'])
        if tag == 'h1': self.h1 += 1
        if tag in {'a', 'link'} and 'href' in a: self.links.append(a['href'])
        if tag in {'script','iframe','form'}: raise AssertionError(f'Unexpected external interaction: {tag}')
        if tag == 'img': assert 'alt' in a

pages = {p.resolve(): Page(p.read_text()) for p in DOCS.rglob('*.html')}
assert len(pages) == 5
links = 0
for p, parsed in pages.items():
    assert parsed.h1 == 1, p
    for url in parsed.links:
        u = urlsplit(url)
        if u.scheme:
            assert u.scheme == 'https' and u.netloc == 'github.com', url
            assert u.path in {'/jnamor','/jnamor/reddit-news-monitor','/jnamor/recommander-system','/jnamor/chat-bot'}, url
            continue
        target = (p.parent / unquote(u.path)).resolve() if u.path else p
        assert target.is_relative_to(DOCS.resolve()), (p,url)
        if target.is_dir(): target /= 'index.html'
        assert target.exists(), (p,url)
        if u.fragment: assert unquote(u.fragment) in pages[target].ids, (p,url)
        links += 1
for p in DOCS.rglob('*'):
    if not p.is_file(): continue
    assert p.suffix in {'.html','.css','.svg'} or p.name == '.nojekyll', p
    text = p.read_text()
    assert not re.search(r'(?i)(?:AKIA[A-Z0-9]{16}|github_pat_|ghp_[a-zA-Z0-9]{20}|-----BEGIN .*PRIVATE KEY|hooks\.slack\.com/services/)', text), f'Sensitive pattern in {p}'
    if p.suffix == '.html':
        assert not re.search(r'\b\d+(?:[.,]\d+)?\s*(?:USD|EUR|€|\$|%)', text), f'Financial figure in {p}'
    assert not any(s in text for s in ['Transition-Professionnelle','PARCOURS_REPONSES','DVK-','SRC-OBS','/home/','127.0.0.1']), p
public_text=json.loads((ROOT/'content.json').read_text())
assert len(public_text['cases']) == 4
print(f'OK: {len(pages)} pages, {links} liens internes et ancres, limites de contenu public vérifiées.')
