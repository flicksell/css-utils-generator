import os
# import rcssmin

# Configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_CSS_PATH = os.path.join(BASE_DIR, "../../static/css/generated.css")
OUTPUT_DOCS_PATH = os.path.join(BASE_DIR, "../../static/css/style-guide.md")

# Utility Patterns
SPACING_DIRECTIONS = {
    "": ["padding", "margin"],
    "t": ["padding-top", "margin-top"],
    "b": ["padding-bottom", "margin-bottom"],
    "s": ["padding-left", "margin-left"], # LTR assumption
    "e": ["padding-right", "margin-right"],
    "x": ["padding-left", "padding-right", "margin-left", "margin-right"],
    "y": ["padding-top", "padding-bottom", "margin-top", "margin-bottom"],
}

# 0-6 levels (multiples of 0.25rem or 4px)
SPACING_LEVELS = {
    0: "0",
    1: "0.25rem",
    2: "0.5rem",
    3: "1rem",
    4: "1.5rem",
    5: "3rem",
    6: "4rem",
}

COLORS = [
    "primary", "secondary", "success", "danger", "warning", "info",
    "light", "dark", "white", "black", "muted", "body", "surface"
]

displays = ["none", "inline", "inline-block", "block", "grid", "table", "flex", "inline-flex"]
positions = ["static", "relative", "absolute", "fixed", "sticky"]
flex_directions = ["row", "row-reverse", "column", "column-reverse"]
flex_wraps = ["nowrap", "wrap", "wrap-reverse"]
justify_contents = ["start", "end", "center", "space-between", "space-around", "space-evenly"]
align_items = ["start", "end", "center", "baseline", "stretch"]
align_contents = ["start", "end", "center", "space-between", "space-around", "stretch"]
align_selfs = ["auto", "start", "end", "center", "baseline", "stretch"]

css_rules = []

def add_rule(selector, properties, is_important=False):
    suffix = "-imp" if is_important else ""
    imp_str = " !important" if is_important else ""
    
    props_str = ""
    for prop, val in properties.items():
        props_str += f"{prop}: {val}{imp_str};"
    
    css_rules.append(f"{selector}{suffix} {{{props_str}}}")

# Generator Functions
def generate_spacing(is_important):
    # Levels 0-6
    for level, value in SPACING_LEVELS.items():
        for code, props in SPACING_DIRECTIONS.items():
            # Padding
            p_props = {}
            p_list = [p for p in props if p.startswith("padding")]
            if p_list:
                for p in p_list: p_props[p] = value
                selector = f".p{code}-{level}"
                add_rule(selector, p_props, is_important)
            
            # Margin
            m_props = {}
            m_list = [p for p in props if p.startswith("margin")]
            if m_list:
                for p in m_list: m_props[p] = value
                selector = f".m{code}-{level}"
                add_rule(selector, m_props, is_important)

    # Pixels 1-100
    for px in range(1, 101):
        value = f"{px}px"
        for code, props in SPACING_DIRECTIONS.items():
            # Padding
            p_props = {}
            p_list = [p for p in props if p.startswith("padding")]
            if p_list:
                for p in p_list: p_props[p] = value
                selector = f".p{code}-{px}px"
                add_rule(selector, p_props, is_important)
            
            # Margin
            m_props = {}
            m_list = [p for p in props if p.startswith("margin")]
            if m_list:
                for p in m_list: m_props[p] = value
                selector = f".m{code}-{px}px"
                add_rule(selector, m_props, is_important)
    
    # Auto margins
    for code, props in SPACING_DIRECTIONS.items():
        m_props = {}
        m_list = [p for p in props if p.startswith("margin")]
        if m_list:
            for p in m_list: m_props[p] = "auto"
            selector = f".m{code}-auto"
            add_rule(selector, m_props, is_important)

def generate_display(is_important):
    for d in displays:
        add_rule(f".d-{d}", {"display": d}, is_important)

def generate_position(is_important):
    for p in positions:
        add_rule(f".position-{p}", {"position": p}, is_important)
    
    for side in ["top", "bottom", "left", "right"]:
        for val in [0, 50, 100]:
            add_rule(f".{side}-{val}", {side: f"{val}%"}, is_important)

def generate_flex(is_important):
    for d in flex_directions:
        add_rule(f".flex-{d}", {"flex-direction": d}, is_important)
    for w in flex_wraps:
        add_rule(f".flex-{w}", {"flex-wrap": w}, is_important)
    
    # Justify Content
    for j in justify_contents:
        val = j
        if j in ["start", "end"]: val = f"flex-{j}"
        add_rule(f".justify-content-{j}", {"justify-content": val}, is_important)
    
    # Align Items
    for a in align_items:
        val = a
        if a in ["start", "end"]: val = f"flex-{a}"
        add_rule(f".align-items-{a}", {"align-items": val}, is_important)
        
    # Align Content
    for a in align_contents:
        val = a
        if a in ["start", "end"]: val = f"flex-{a}"
        add_rule(f".align-content-{a}", {"align-content": val}, is_important)
        
    # Align Self
    for a in align_selfs:
        val = a
        if a in ["start", "end"]: val = f"flex-{a}"
        add_rule(f".align-self-{a}", {"align-self": val}, is_important)

    # Grow/Shrink
    for i in [0, 1]:
        add_rule(f".flex-grow-{i}", {"flex-grow": str(i)}, is_important)
        add_rule(f".flex-shrink-{i}", {"flex-shrink": str(i)}, is_important)
    
    add_rule(".flex-fill", {"flex": "1 1 auto"}, is_important)
    
    # Gap 0-10 (0.25rem steps)
    for i in range(11):
        add_rule(f".gap-{i}", {"gap": f"{i*0.25}rem"}, is_important)

def generate_typography(is_important):
    # Align
    for a in ["start", "end", "center", "justify"]:
        add_rule(f".text-{a}", {"text-align": a}, is_important)
    
    # Transform
    for t in ["lowercase", "uppercase", "capitalize"]:
        add_rule(f".text-{t}", {"text-transform": t}, is_important)
        
    # Decoration
    for d in ["none", "underline", "line-through"]:
        add_rule(f".text-decoration-{d}", {"text-decoration": d}, is_important)
        
    # Wrap
    for w in ["wrap", "nowrap", "break"]:
        val = "normal"
        if w == "nowrap": val = "nowrap"
        if w == "break": val = "break-word" # simplistic
        add_rule(f".text-{w}", {"white-space": val}, is_important)
        
    # Weight
    for w in ["light", "lighter", "normal", "bold", "bolder"]:
        add_rule(f".fw-{w}", {"font-weight": w}, is_important)
    for w in range(100, 1000, 100):
        add_rule(f".fw-{w}", {"font-weight": str(w)}, is_important)
        
    # Size 1-6 (headings) and fs-1 to fs-6 where fs-1 is biggest
    # Bootstrap logic: fs-1: 2.5rem, fs-2: 2rem, fs-3: 1.75rem, fs-4: 1.5rem, fs-5: 1.25rem, fs-6: 1rem
    sizes = {
        1: "2.5rem", 2: "2rem", 3: "1.75rem", 4: "1.5rem", 5: "1.25rem", 6: "1rem"
    }
    for level, size in sizes.items():
        add_rule(f".fs-{level}", {"font-size": size}, is_important)
        
    # Colors
    for c in COLORS:
        add_rule(f".text-{c}", {"color": f"var(--color-{c})"}, is_important)
        add_rule(f".bg-{c}", {"background-color": f"var(--color-{c})"}, is_important)

def generate_sizing(is_important):
    # Width/Height %
    for i in [25, 50, 75, 100, "auto"]:
        val = "auto" if i == "auto" else f"{i}%"
        add_rule(f".w-{i}", {"width": val}, is_important)
        add_rule(f".h-{i}", {"height": val}, is_important)
        
    add_rule(".mw-100", {"max-width": "100%"}, is_important)
    add_rule(".mh-100", {"max-height": "100%"}, is_important)
    add_rule(".vw-100", {"width": "100vw"}, is_important)
    add_rule(".vh-100", {"height": "100vh"}, is_important)
    
    # Width/Height px (1-100)
    for px in range(1, 101):
        add_rule(f".w-{px}px", {"width": f"{px}px"}, is_important)
        add_rule(f".h-{px}px", {"height": f"{px}px"}, is_important)

def generate_borders(is_important):
    add_rule(".border", {"border": "1px solid var(--border-default)"}, is_important)
    for side in ["top", "bottom", "left", "right"]:
        add_rule(f".border-{side}", {f"border-{side}": "1px solid var(--border-default)"}, is_important)
    
    add_rule(".border-0", {"border": "0"}, is_important)
    for side in ["top", "bottom", "left", "right"]:
        add_rule(f".border-{side}-0", {f"border-{side}": "0"}, is_important)
        
    for c in COLORS:
        add_rule(f".border-{c}", {"border-color": f"var(--color-{c})"}, is_important)
        
    # Radius
    add_rule(".rounded", {"border-radius": "var(--radius-md)"}, is_important)
    add_rule(".rounded-0", {"border-radius": "0"}, is_important)
    add_rule(".rounded-circle", {"border-radius": "50%"}, is_important)
    add_rule(".rounded-pill", {"border-radius": "50rem"}, is_important)
    add_rule(".rounded-sm", {"border-radius": "var(--radius-sm)"}, is_important)
    add_rule(".rounded-lg", {"border-radius": "var(--radius-lg)"}, is_important)
    add_rule(".rounded-xl", {"border-radius": "var(--radius-xl)"}, is_important)

def generate_effects(is_important):
    # Opacity
    for i in range(0, 101, 5): # 0, 5, 10... 100
        add_rule(f".opacity-{i}", {"opacity": str(i/100)}, is_important)
        
    # Cursor
    for c in ["auto", "default", "pointer", "text", "wait", "move", "not-allowed"]:
        add_rule(f".cursor-{c}", {"cursor": c}, is_important)
        
    # Visibility
    add_rule(".visible", {"visibility": "visible"}, is_important)
    add_rule(".invisible", {"visibility": "hidden"}, is_important)

def main():
    print("Generating CSS...")
    
    # Generate standard rules
    generate_spacing(False)
    generate_display(False)
    generate_position(False)
    generate_flex(False)
    generate_typography(False)
    generate_sizing(False)
    generate_borders(False)
    generate_effects(False)
    
    # Generate !important rules
    generate_spacing(True)
    generate_display(True)
    generate_position(True)
    generate_flex(True)
    generate_typography(True)
    generate_sizing(True)
    generate_borders(True)
    generate_effects(True)
    
    # full_css = "\n".join(css_rules)
    # minified_css = rcssmin.cssmin(full_css)
    
    # Simple manual minification
    minified_css = "".join(css_rules).replace(": ", ":").replace("; ", ";").replace(" {", "{").replace("} ", "}")
    
    # Write CSS
    os.makedirs(os.path.dirname(OUTPUT_CSS_PATH), exist_ok=True)
    with open(OUTPUT_CSS_PATH, "w") as f:
        f.write(minified_css)
        
    print(f"Generated {len(css_rules)} rules into {OUTPUT_CSS_PATH}")

    # Compress with Brotli (using system command)
    try:
        import subprocess
        br_path = OUTPUT_CSS_PATH + ".br"
        subprocess.run(["brotli", "-f", "-q", "11", "-o", br_path, OUTPUT_CSS_PATH], check=True)
        print(f"Compressed to {br_path}")
    except Exception as e:
        print(f"Failed to compress with brotli: {e}")
    
    # Write Documentation
    docs = """# CSS Utility Classes

This file is auto-generated. Do not edit manually.

## Features
- **Suffix:** Add `-imp` to any class to apply `!important`.

## Spacing
- **Padding:** `.p{side}-{level}` or `.p{side}-{px}px`
- **Margin:** `.m{side}-{level}` or `.m{side}-{px}px` or `.m{side}-auto`
  - Sides: `t` (top), `b` (bottom), `s` (left), `e` (right), `x` (horiz), `y` (vert), `` (all)
  - Levels: 0-6 (0, 0.25rem, 0.5rem, 1rem, 1.5rem, 3rem, 4rem)
  - Pixels: 1-100px

## Display & Position
- `.d-{none|inline|block|flex|grid...}`
- `.position-{static|relative|absolute|fixed|sticky}`
- `.{top|bottom|left|right}-{0|50|100}`

## Flexbox
- `.flex-{row|column|...}`
- `.flex-{wrap|nowrap}`
- `.justify-content-{start|end|center|between|around|evenly}`
- `.align-items-{start|end|center|baseline|stretch}`
- `.align-content-{start|end|center|between|around|stretch}`
- `.align-self-{auto|start|end|center|baseline|stretch}`
- `.flex-grow-{0|1}`, `.flex-shrink-{0|1}`, `.flex-fill`
- `.gap-{0-10}` (0.25rem steps)

## Typography
- `.text-{start|end|center|justify}`
- `.text-{lowercase|uppercase|capitalize}`
- `.text-decoration-{none|underline|line-through}`
- `.text-{wrap|nowrap|break}`
- `.fw-{light|normal|bold|bolder|100-900}`
- `.fs-{1-6}` (headings scale)
- `.text-{color}`, `.bg-{color}` (using `var(--color-{name})`)

## Sizing
- `.w-{25|50|75|100|auto}`, `.h-{25|50|75|100|auto}`
- `.w-{1-100}px`, `.h-{1-100}px`
- `.mw-100`, `.mh-100`, `.vw-100`, `.vh-100`

## Borders
- `.border`, `.border-{side}`, `.border-0`, `.border-{side}-0`
- `.border-{color}`
- `.rounded`, `.rounded-{0|circle|pill|sm|lg|xl}`

## Effects
- `.opacity-{0-100}` (step 5)
- `.cursor-{auto|pointer|...}`
- `.visible`, `.invisible`
"""
    
    with open(OUTPUT_DOCS_PATH, "w") as f:
        f.write(docs)
        
    print(f"Generated documentation at {OUTPUT_DOCS_PATH}")

if __name__ == "__main__":
    main()
