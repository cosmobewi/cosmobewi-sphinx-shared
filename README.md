# cosmobewi-sphinx-shared

📚 **Shared Sphinx assets for CosmoBEWI documentation**

This repository centralizes the **theme, templates, and base configuration** used across all CosmoBEWI projects 
(e.g. [Balabewi](https://cosmobewi.github.io/balabewi/), [PDV-TO-LAMBDA](https://cosmobewi.github.io/PDV-TO-LAMBDA/), [ScanBEWI](https://cosmobewi.github.io/scanbewi/)).

It provides a **consistent look & feel** for our documentation sites and simplifies maintenance by sharing:

- 🖼️ `_static/` → shared CSS/JS, logos, favicon  
- 🧩 `_templates/` → Jinja2 templates (layout, footer, header)  
- ⚙️ `conf_shared.py` → base Sphinx configuration (theme, extensions, paths)

---

## Usage

### As a submodule
Add this repository as a submodule inside your project’s `docs/` folder:

```bash
git submodule add -b main \
  git@github.com:cosmobewi/cosmobewi-sphinx-shared.git docs/iobewi-shared
