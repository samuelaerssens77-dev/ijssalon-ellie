# Ijssalon Whizzo - AI Coding Agent Instructions

## Project Overview
Educational learning project for an ice cream parlor (Ijssalon) website using Flask web framework with Python backend logic. The project demonstrates combining utility functions, data processing, and web templating.

## Architecture & Components

### Python Modules
- **`algemene_functies.py`**: Core utility module containing shared functions like `mijn_functie_2()` that performs arithmetic operations (addition, subtraction, multiplication, division) on two values. Used by other modules.
- **`helper.py`**: Contains the `decoreer()` function for console text decoration with asterisk borders. Simple utility for display purposes.
- **`reclame*.py` files**: Individual exercises/scripts demonstrating specific concepts:
  - `reclame5.py`, `reclame6.py`: Price calculation and income functions
  - `reclame7.py`, `reclame8.py`: Financial calculations (revenue totals, BTW/VAT)
  - `reclame10.py` onwards: Progressive exercises building on earlier concepts
  
### Web Structure (Flask Application)
- **`templates/`**: Jinja2 HTML templates
  - `layout.html`: Base template with Bootstrap 3, navigation, footer. All pages inherit from here.
  - `home.html`, `prijzen.html`, `recepten.html`: Content pages extending layout.html
- **`static/style.css`**: Global styling applied via `layout.html`. Uses custom fonts (Pushster), orange/brown color scheme (#be6c00), and responsive Bootstrap grid.

## Project-Specific Patterns

### Import Convention
- Modules use explicit imports: `from algemene_functies import mijn_functie_2` (not wildcard imports)
- Each script may redefine functions locally for learning purposes (see redundant `laag_en_hoog()` definitions across `reclame12.py` and `reclame8.py`)

### Function Design
- Functions process lists and return computed results (min/max, sums, arithmetic operations)
- Examples: `mijn_functie_2(a, b)` returns list of four arithmetic results; `laag_en_hoog()` returns [min, max] pair
- Heavy use of list operations: `append()`, `sum()`, slicing

### Web Integration
- Flask routes likely map to templates in `templates/` directory
- CSS styling via Jinja2's `url_for('static', filename='...')` helper
- Bootstrap classes used for layout (`.container`, navigation components)

## Key Files Reference
- Core logic: [algemene_functies.py](algemene_functies.py), [helper.py](helper.py)
- Web base: [templates/layout.html](templates/layout.html), [static/style.css](static/style.css)
- Exercise files: `reclame*.py` (numbered progression for learning)

## Common Issues to Watch For
- Function parameter shadowing (e.g., `reclame5.py` line 5: parameter `smaak` reassigned immediately, making parameter useless)
- Missing `from` statement in imports (e.g., `reclame.py` line 1 missing `from`)
- Inconsistent function behavior due to hardcoded values overriding parameters

## Development Notes
- This is a school project emphasizing learning core programming concepts
- Multiple versions of similar functions exist to show progression/iterations
- HTML templates use inline Bootstrap CDN links (not installed locally)
- Focus on functional programming style with list transformations
