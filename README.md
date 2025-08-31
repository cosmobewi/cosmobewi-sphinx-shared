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
  https://github.com/cosmobewi/cosmobewi-sphinx-shared.git docs/cosmobewi-shared
```

### Minimum `conf.py`

In your project’s `docs/conf.py`, import the shared configuration and enable local overrides:

```python
# docs/conf.py
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parent / "cosmobewi-shared"))

from conf_shared import *     # shared theme & config
include_local_paths(__file__) # enable local overrides
```

This way, you inherit the **shared theme & settings** but can still add project-specific extensions, templates, or static files if needed.
