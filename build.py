"""Build the public static portfolio; Python standard library only."""
from html import escape as e
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'docs'
DATA = json.loads((ROOT / 'content.json').read_text())
OUT.mkdir(exist_ok=True)

def paragraphs(items):
    return ''.join(f'<p>{e(p)}</p>' for p in items)

def tags(items):
    return '<ul class="tags" aria-label="Technologies">' + ''.join(f'<li>{e(t)}</li>' for t in items) + '</ul>'

def layout(title, description, body, prefix='./'):
    return f'''<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="{e(description, quote=True)}"><meta name="color-scheme" content="light">
<meta property="og:title" content="{e(title, quote=True)}"><meta property="og:description" content="{e(description, quote=True)}"><meta property="og:type" content="website">
<title>{e(title)}</title><link rel="icon" href="{prefix}favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="{prefix}style.css"></head>
<body><a class="skip" href="#contenu">Aller au contenu</a>
<header class="nav"><a class="wordmark" href="{prefix}index.html" aria-label="Jordan Namor, accueil"><span class="monogram">jn<span>↗</span></span><span>Jordan Namor<span class="wordmark-sub">DevOps & Cloud</span></span></a>
<nav aria-label="Navigation principale"><a href="{prefix}index.html#realisations">Réalisations</a><a href="{prefix}index.html#parcours">Parcours</a><a class="github-link" href="https://github.com/jnamor">GitHub ↗</a></nav></header>
<main id="contenu">{body}</main>
<footer><div><strong>Jordan Namor</strong><span>Ingénieur DevOps & Cloud</span></div><p>Portfolio personnel · Retours d’expérience sélectionnés.<br>Schémas de principe ; documents et configurations d’entreprise non publiés.</p><a href="https://github.com/jnamor">GitHub ↗</a></footer>
</body></html>'''

def diagram(d):
    rows = ''
    for track in d['tracks']:
        nodes = ''.join(f'<li>{e(s)}</li>' for s in track['steps'])
        rows += f'<div class="track"><p class="track-name">{e(track["name"])}</p><ol class="flow">{nodes}</ol></div>'
    return f'<figure class="diagram"><h3>{e(d["label"])}</h3>{rows}<figcaption>{e(d["caption"])}</figcaption></figure>'

def home():
    cases = ''
    for c in DATA['cases']:
        cases += f'''<article class="case-row"><div class="case-index">{c['number']}<span>↗</span></div><div class="case-copy"><p class="eyebrow">{e(c['category'])}</p><h3><a href="cas/{c['slug']}/index.html">{e(c['short_title'])}</a></h3><p>{e(c['summary'])}</p>{tags(c['tags'])}</div><div class="case-aside"><p>{e(c['outcome'])}</p><a class="text-link" href="cas/{c['slug']}/index.html">Lire le cas <span aria-hidden="true">↗</span></a></div></article>'''
    skills = ''.join(f'<article><span class="small-rule"></span><h3>{e(x["title"])}</h3><p>{e(x["text"])}</p></article>' for x in DATA['practice'])
    experiments = ''
    for x in DATA['experiments']:
        second = f'<a href="{x["second_url"]}">{e(x["second_link"])} ↗</a>' if x.get('second_url') else ''
        experiments += f'<article><p class="eyebrow">{e(x["label"])}</p><h3>{e(x["title"])}</h3><p>{e(x["text"])}</p><div class="experiment-links"><a href="{x["url"]}">{e(x["link"])} ↗</a>{second}</div></article>'
    earlier_education = "".join(f'<article><p class="timeline-label">FORMATION · {e(x["period"])}</p><div><h3>{e(x["title"])}</h3><p><strong>{e(x["school"])}</strong></p><p>{e(x["text"])}</p></div></article>' for x in DATA["earlier_education"])
    return f'''<section class="hero shell"><div class="hero-copy"><p class="eyebrow"><span class="status-dot"></span> Jordan Namor · Ingénieur DevOps & Cloud chez Kikleo</p><h1>Construire.<br>Automatiser.<br><em>Fiabiliser.</em></h1><p class="hero-intro">{e(DATA['intro'])}</p><div class="hero-actions"><a class="button" href="#realisations">Explorer mes réalisations <span aria-hidden="true">↘</span></a><a class="text-link" href="https://github.com/jnamor">Mon GitHub ↗</a></div></div>
<aside class="hero-note" aria-label="Ma démarche"><div class="note-top"><span>DE L’INTENTION À L’EXPLOITATION</span><span aria-hidden="true">↗</span></div><div class="blueprint" aria-hidden="true"><div class="blueprint-node">git</div><div class="blueprint-line"></div><div class="node-pair"><span>livrer</span><span>observer</span></div><div class="blueprint-line"></div><div class="blueprint-node">améliorer</div></div><p>Des choix techniques,<br><strong>expliqués par leur usage.</strong></p><div class="note-bottom">Cloud · Linux · Kubernetes · Automatisation</div></aside></section>
<div class="context-band"><div class="shell"><p><strong>Mon quotidien</strong> Infrastructure, déploiements et exploitation.</p><p><strong>Mon approche</strong> Comprendre, outiller, transmettre.</p></div></div>
<section id="realisations" class="shell section"><div class="section-heading"><div><p class="eyebrow">01 / RETOURS D’EXPÉRIENCE PROFESSIONNELS</p><h2>Le travail derrière<br>les technologies.</h2></div><p>Du contexte aux résultats : mon rôle, les choix faits avec l’équipe et les limites de chaque réalisation.</p></div><div class="case-list">{cases}</div></section>
<section class="practice"><div class="shell section"><p class="eyebrow">02 / EN PRATIQUE</p><h2>Ce que je sais prendre en charge.</h2><div class="skill-grid">{skills}</div></div></section>
<section id="parcours" class="shell section"><div class="section-heading"><div><p class="eyebrow">03 / PARCOURS</p><h2>Une spécialisation<br>ancrée dans la pratique.</h2></div><p>Expérience professionnelle, formation et explorations sont présentées dans leur contexte.</p></div><div class="timeline"><article><p class="timeline-label">EXPÉRIENCE PROFESSIONNELLE</p><div><h3>Ingénieur DevOps & Cloud · Kikleo</h3><p>J’ai rejoint Kikleo en alternance en 2022, puis poursuivi en CDI après ma formation. J’assure aujourd’hui la responsabilité opérationnelle de l’infrastructure, des déploiements, des automatisations et des optimisations, en collaboration avec le directeur technique et les développeurs.</p><p>La fondation AWS initiale revient au directeur technique ; mes contributions couvrent sa reprise opérationnelle et les évolutions décrites dans les études de cas.</p></div></article><article><p class="timeline-label">FORMATION · 2023–2025</p><div><h3>Master DevOps et Cloud</h3><p><strong>Sup de Vinci ISI Paris</strong></p><p>{e(DATA['education'])}</p><details><summary>Exemples de projets de formation</summary><p>Les dossiers de master conservés comprennent des travaux de livraison avec GitLab CI/CD et Argo CD, de déploiement Azure/AKS avec Terraform et Kustomize, et d’outillage Python en ligne de commande. Ils sont en cours de revue pour préciser les contributions individuelles et les supports réutilisés.</p><p>Ces exemples ne sont pas présentés comme des réalisations de production chez Kikleo. Aucun dépôt de formation ni configuration n’est recopié dans ce portfolio.</p></details></div></article>{earlier_education}</div></section>
<section class="experiments shell section"><p class="eyebrow">04 / EXPLORATIONS PUBLIQUES</p><h2>La curiosité, au-delà du quotidien.</h2><div class="experiment-grid">{experiments}</div><p class="subtle">Les forks et ressources pédagogiques présents sur mon compte ne sont pas présentés comme des créations personnelles.</p></section>
<section class="closing shell"><p class="eyebrow">POUR ALLER PLUS LOIN</p><h2>Un choix technique<br>à approfondir ensemble ?</h2><p>Chaque étude de cas propose des questions pour ouvrir la discussion en entretien.</p><a class="button" href="#realisations">Choisir un cas <span aria-hidden="true">↗</span></a></section>'''

def case_page(c):
    actions = ''.join(f'<article class="decision"><span>{i:02d}</span><div><h3>{e(a["title"])}</h3><p>{e(a["text"])}</p></div></article>' for i,a in enumerate(c['actions'],1))
    results = ''.join(f'<li>{e(x)}</li>' for x in c['results'])
    questions = ''.join(f'<li>{e(x)}</li>' for x in c['interview'])
    retrospective = f'<h3>Ce que je ferais plus tôt</h3><p>{e(c["retrospective"])}</p>' if c.get('retrospective') else '<p class="subtle">Les points que je ferais différemment restent à préciser dans mon retour personnel. Les questions ci-dessous permettent d’ouvrir cette discussion.</p>'
    nxt = DATA['cases'][int(c['number']) % len(DATA['cases'])]
    return f'''<div class="shell case-shell"><a class="back" href="../../index.html#realisations">← Toutes les réalisations</a><header class="case-hero"><p class="eyebrow">CAS {c['number']} / {e(c['category'])} · EXPÉRIENCE CHEZ KIKLEO</p><h1>{e(c['title'])}</h1><p class="case-lead">{e(c['summary'])}</p>{tags(c['tags'])}</header><div class="case-overview"><strong>Résultat à retenir</strong><p>{e(c['outcome'])}</p></div><div class="case-body"><aside class="case-toc"><p class="eyebrow">DANS CE CAS</p><a href="#contexte">Le contexte</a><a href="#role">Mon rôle</a><a href="#choix">Actions & choix</a><a href="#resultats">Résultats & limites</a><a href="#recul">Recul & discussion</a></aside><div class="case-prose"><section id="contexte"><p class="eyebrow">01 / COMPRENDRE</p><h2>Le contexte et le besoin.</h2>{paragraphs(c['context'])}</section><section id="role"><p class="eyebrow">02 / ATTRIBUER</p><h2>Mon rôle et celui de l’équipe.</h2>{paragraphs(c['role'])}</section><section id="choix"><p class="eyebrow">03 / AGIR</p><h2>Les actions et les choix.</h2>{actions}{diagram(c['diagram'])}</section><section id="resultats"><p class="eyebrow">04 / ÉVALUER</p><h2>Les résultats et leur portée.</h2><ul class="result-list">{results}</ul><details><summary>Comment lire ces résultats et leurs limites</summary><h3>Mesure et qualification</h3><p>{e(c['measure'])}</p><h3>Limites</h3><p>{e(c['limits'])}</p></details></section><section id="recul"><p class="eyebrow">05 / PRENDRE DU RECUL</p><h2>Ce que le cas met en évidence.</h2><p>{e(c['learning'])}</p>{retrospective}<details><summary>Ouvrir la discussion en entretien</summary><ul>{questions}</ul></details></section></div></div><a class="next-case" href="../{nxt['slug']}/index.html"><span>CAS SUIVANT</span><strong>{e(nxt['short_title'])}</strong><span aria-hidden="true">↗</span></a></div>'''

(OUT / 'index.html').write_text(layout('Jordan Namor — Ingénieur DevOps & Cloud', DATA['intro'], home()))
for c in DATA['cases']:
    dest = OUT / 'cas' / c['slug']
    dest.mkdir(parents=True, exist_ok=True)
    (dest / 'index.html').write_text(layout(c['short_title'] + ' — Jordan Namor', c['summary'], case_page(c), '../../'))
(OUT / '.nojekyll').touch()
(OUT / 'favicon.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="12" fill="#123f38"/><text x="10" y="44" font-family="sans-serif" font-size="38" font-weight="700" fill="#e5f29a">jn</text></svg>')
(OUT / 'style.css').write_text((ROOT / 'style.css').read_text())
print(f'Built {len(DATA["cases"])+1} pages in {OUT}')
