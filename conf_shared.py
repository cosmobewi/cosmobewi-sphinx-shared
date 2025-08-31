import os
import sys
from datetime import date
from pathlib import Path

BASE = Path(__file__).resolve().parent
SHARED_TEMPLATES = BASE / "_templates"
SHARED_STATIC = BASE / "_static"

project = "CosmoBEWI"
author = "Lionel Orcil — Édité et diffusé par IOBEWI"
copyright = f"{date.today().year}, {author}"

sys.path.insert(0, os.path.abspath(".."))

extensions = [
    "sphinx.ext.mathjax",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.todo",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinxcontrib.bibtex",
]

bibtex_bibfiles = ["references.bib"]
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
}

mathjax3_config = {
    "tex": {
        "macros": {
            r"\dd":  r"{\,\mathrm{d}}",
            r"\vect": [r"{\boldsymbol{#1}}", 1],
            r"\avg":  [r"{\langle #1 \rangle}", 1],
        }
    }
}

html_logo = str(SHARED_STATIC / "cosmobewi.jpg")
html_theme_options = {
    'logo_only': True,
}

templates_path   = [str(SHARED_TEMPLATES)]
html_static_path = [str(SHARED_STATIC)]

html_theme = "sphinx_rtd_theme"
html_css_files = ["custom.css"]
html_show_sphinx = False
html_show_copyright = False


source_suffix = ".rst"
master_doc = "index"
language = "fr"
autosummary_generate = True
nitpicky = False

rst_prolog = r"""
.. |proj| replace:: Théorie des Horloges Cosmologiques
.. |LCDM| replace:: :math:`\Lambda\mathrm{CDM}`
"""

todo_include_todos = True

html_context = {
    "display_github": True,
    "github_user": "cosmobewi",
    "github_repo": "cosmobewi.com",
    "github_version": "main/docs/",
}

# Utilitaire: à appeler dans chaque conf.py de sous-projet
def include_local_paths(conf_file: str):
    """Préfixe les chemins locaux pour permettre overrides par sous-projet."""
    here = Path(conf_file).resolve().parent
    # Local templates AVANT le shared -> prioritaire pour Jinja
    if (here / "_templates").exists():
        templates_path.insert(0, str(here / "_templates"))
    # Local static APRÈS le shared -> puis on met sa CSS/JS en dernier si besoin
    if (here / "_static").exists():
        html_static_path.append(str(here / "_static"))