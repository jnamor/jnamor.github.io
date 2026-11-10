# Jordan Namor — portfolio

Site personnel statique en français. Les études de cas présentent des expériences professionnelles à un niveau de détail choisi pour le public ; les configurations et documents d’entreprise ne sont pas inclus. Les projets de formation et les explorations personnelles sont identifiés séparément.

## Modifier et vérifier

Python 3, sans dépendance externe :

```sh
python3 build.py
python3 verify.py
python3 -m http.server 8080 --bind 127.0.0.1 --directory docs
```

Ouvrir `http://127.0.0.1:8080`. Les textes sont dans `content.json`, le gabarit dans `build.py` et le style dans `style.css`. Le dossier `docs/` contient le résultat statique, à versionner avec les sources. Il ne dépend d’aucun serveur Python une fois publié.

Après modification, relancer la génération et vérifier l’accueil, les quatre cas et les liens sur ordinateur et téléphone. La génération n’effectue aucun accès au cloud ni publication.

## GitHub Pages

Destination prévue après validation : dépôt public `jnamor/jnamor.github.io`, adresse `https://jnamor.github.io/`.

Dans Settings → Pages, choisir **Deploy from a branch**, branche `main`, dossier `/docs`, puis Save. Les fichiers `.nojekyll` et les liens relatifs sont déjà prévus. Aucun domaine personnalisé n’est nécessaire.

La publication depuis la racine de `main` est également prise en charge : le fichier `index.html` redirige vers `docs/`, qui contient le portfolio. L’adresse `https://jnamor.github.io/` reste ainsi utilisable avec les deux réglages.

Références : [création du site](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site), [source de publication](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site), [limites de Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits).

## Historique et retour arrière

Conserver les changements dans Git. Pour revenir à une version déjà publiée, utiliser `git revert` sur le commit concerné, régénérer si nécessaire, vérifier, puis publier ce retour. Ne pas réécrire l’historique partagé. Le README de profil est géré séparément dans `jnamor/jnamor`.

## Périmètre éditorial

Ce dépôt contient uniquement les sources du portfolio et les pages destinées au public. Il ne contient ni données financières d’entreprise, ni documents de candidature, ni inventaires de machines, ni secrets. Les exemples de principe ne reproduisent pas la topologie de l’employeur.
