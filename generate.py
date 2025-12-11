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

def generate_overflow(is_important):
    for val in ["hidden", "scroll", "auto", "visible"]:
        add_rule(f".overflow-{val}", {"overflow": val}, is_important)
    add_rule(".overflow-x-auto", {"overflow-x": "auto"}, is_important)
    add_rule(".overflow-y-auto", {"overflow-y": "auto"}, is_important)
    add_rule(".overflow-x-hidden", {"overflow-x": "hidden"}, is_important)
    add_rule(".overflow-y-hidden", {"overflow-y": "hidden"}, is_important)
    add_rule(".overflow-x-scroll", {"overflow-x": "scroll"}, is_important)
    add_rule(".overflow-y-scroll", {"overflow-y": "scroll"}, is_important)

def generate_zindex(is_important):
    for z in [0, 10, 20, 30, 40, 50]:
        add_rule(f".z-{z}", {"z-index": str(z)}, is_important)
    add_rule(".z-auto", {"z-index": "auto"}, is_important)
    # Negative z-index
    for z in [1, 10]:
        add_rule(f".z-n{z}", {"z-index": str(-z)}, is_important)

def generate_object(is_important):
    # Object-fit
    for fit in ["cover", "contain", "fill", "none", "scale-down"]:
        add_rule(f".object-fit-{fit}", {"object-fit": fit}, is_important)
    # Object-position
    for pos in ["center", "top", "bottom", "left", "right", "top-left", "top-right", "bottom-left", "bottom-right"]:
        css_val = pos.replace("-", " ")
        add_rule(f".object-position-{pos}", {"object-position": css_val}, is_important)

def generate_aspect_ratio(is_important):
    ratios = {
        "square": "1 / 1",
        "video": "16 / 9",
        "4-3": "4 / 3",
        "3-2": "3 / 2",
        "16-9": "16 / 9",
        "21-9": "21 / 9",
        "1": "1 / 1",
    }
    for name, val in ratios.items():
        add_rule(f".aspect-{name}", {"aspect-ratio": val}, is_important)

def generate_typography_extended(is_important):
    # Line-height
    line_heights = {
        "1": "1",
        "sm": "1.25",
        "base": "1.5",
        "lg": "1.75",
        "xl": "2",
    }
    for name, val in line_heights.items():
        add_rule(f".lh-{name}", {"line-height": val}, is_important)

    # Letter-spacing
    letter_spacings = {
        "tighter": "-0.05em",
        "tight": "-0.025em",
        "normal": "0",
        "wide": "0.025em",
        "wider": "0.05em",
        "widest": "0.1em",
    }
    for name, val in letter_spacings.items():
        add_rule(f".ls-{name}", {"letter-spacing": val}, is_important)

    # Font-family
    add_rule(".font-sans", {"font-family": "var(--font-sans, system-ui, -apple-system, sans-serif)"}, is_important)
    add_rule(".font-serif", {"font-family": "var(--font-serif, Georgia, serif)"}, is_important)
    add_rule(".font-mono", {"font-family": "var(--font-mono, ui-monospace, monospace)"}, is_important)

    # Text truncate (single line ellipsis)
    add_rule(".text-truncate", {"overflow": "hidden", "text-overflow": "ellipsis", "white-space": "nowrap"}, is_important)
    add_rule(".truncate", {"overflow": "hidden", "text-overflow": "ellipsis", "white-space": "nowrap"}, is_important)

    # White-space (more complete)
    for ws in ["normal", "nowrap", "pre", "pre-wrap", "pre-line", "break-spaces"]:
        add_rule(f".ws-{ws}", {"white-space": ws}, is_important)

    # Line-clamp (multi-line truncation)
    for lines in range(1, 7):
        add_rule(f".line-clamp-{lines}", {
            "display": "-webkit-box",
            "-webkit-line-clamp": str(lines),
            "-webkit-box-orient": "vertical",
            "overflow": "hidden"
        }, is_important)

def generate_interaction(is_important):
    # Pointer-events
    add_rule(".pointer-events-none", {"pointer-events": "none"}, is_important)
    add_rule(".pointer-events-auto", {"pointer-events": "auto"}, is_important)

    # User-select
    for sel in ["none", "text", "all", "auto"]:
        add_rule(f".user-select-{sel}", {"user-select": sel}, is_important)

    # Touch-action
    for ta in ["none", "pan-x", "pan-y", "manipulation", "auto"]:
        add_rule(f".touch-action-{ta}", {"touch-action": ta}, is_important)

def generate_transforms(is_important):
    # Translate X/Y percentages
    for axis in ["x", "y"]:
        for pct in [0, 25, 50, 100]:
            add_rule(f".translate-{axis}-{pct}", {"transform": f"translate{axis.upper()}({pct}%)"}, is_important)
        # Negative translations
        for pct in [25, 50, 100]:
            add_rule(f".translate-{axis}-n{pct}", {"transform": f"translate{axis.upper()}(-{pct}%)"}, is_important)

    # Rotate
    for deg in [0, 45, 90, 180, 270]:
        add_rule(f".rotate-{deg}", {"transform": f"rotate({deg}deg)"}, is_important)
    # Negative rotations
    for deg in [45, 90, 180]:
        add_rule(f".rotate-n{deg}", {"transform": f"rotate(-{deg}deg)"}, is_important)

    # Scale
    for scale in [0, 50, 75, 90, 95, 100, 105, 110, 125, 150]:
        add_rule(f".scale-{scale}", {"transform": f"scale({scale/100})"}, is_important)

def generate_sizing_extended(is_important):
    # Min-width
    add_rule(".min-w-0", {"min-width": "0"}, is_important)
    add_rule(".min-w-full", {"min-width": "100%"}, is_important)

    # Min-height
    add_rule(".min-h-0", {"min-height": "0"}, is_important)
    add_rule(".min-h-full", {"min-height": "100%"}, is_important)
    add_rule(".min-h-screen", {"min-height": "100vh"}, is_important)

    # Max-width (container widths)
    max_widths = {
        "xs": "20rem",      # 320px
        "sm": "24rem",      # 384px
        "md": "28rem",      # 448px
        "lg": "32rem",      # 512px
        "xl": "36rem",      # 576px
        "2xl": "42rem",     # 672px
        "3xl": "48rem",     # 768px
        "4xl": "56rem",     # 896px
        "5xl": "64rem",     # 1024px
        "6xl": "72rem",     # 1152px
        "7xl": "80rem",     # 1280px
        "full": "100%",
        "prose": "65ch",
        "screen-sm": "640px",
        "screen-md": "768px",
        "screen-lg": "1024px",
        "screen-xl": "1280px",
    }
    for name, val in max_widths.items():
        add_rule(f".max-w-{name}", {"max-width": val}, is_important)

    # Max-height
    add_rule(".max-h-full", {"max-height": "100%"}, is_important)
    add_rule(".max-h-screen", {"max-height": "100vh"}, is_important)

def generate_flexgrid_extended(is_important):
    # Order
    for i in range(13):  # 0-12
        add_rule(f".order-{i}", {"order": str(i)}, is_important)
    add_rule(".order-first", {"order": "-9999"}, is_important)
    add_rule(".order-last", {"order": "9999"}, is_important)
    add_rule(".order-none", {"order": "0"}, is_important)

    # Grid template columns
    for cols in range(1, 13):
        add_rule(f".grid-cols-{cols}", {"grid-template-columns": f"repeat({cols}, minmax(0, 1fr))"}, is_important)
    add_rule(".grid-cols-none", {"grid-template-columns": "none"}, is_important)

    # Column span
    for span in range(1, 13):
        add_rule(f".col-span-{span}", {"grid-column": f"span {span} / span {span}"}, is_important)
    add_rule(".col-span-full", {"grid-column": "1 / -1"}, is_important)

    # Grid rows
    for rows in range(1, 7):
        add_rule(f".grid-rows-{rows}", {"grid-template-rows": f"repeat({rows}, minmax(0, 1fr))"}, is_important)
    add_rule(".grid-rows-none", {"grid-template-rows": "none"}, is_important)

    # Row span
    for span in range(1, 7):
        add_rule(f".row-span-{span}", {"grid-row": f"span {span} / span {span}"}, is_important)
    add_rule(".row-span-full", {"grid-row": "1 / -1"}, is_important)

    # Place-items
    for val in ["center", "start", "end", "stretch"]:
        add_rule(f".place-items-{val}", {"place-items": val}, is_important)

    # Place-content
    for val in ["center", "start", "end", "stretch", "between", "around", "evenly"]:
        css_val = f"space-{val}" if val in ["between", "around", "evenly"] else val
        add_rule(f".place-content-{val}", {"place-content": css_val}, is_important)

    # Place-self
    for val in ["center", "start", "end", "stretch", "auto"]:
        add_rule(f".place-self-{val}", {"place-self": val}, is_important)

def generate_accessibility(is_important):
    # Screen reader only
    add_rule(".sr-only", {
        "position": "absolute",
        "width": "1px",
        "height": "1px",
        "padding": "0",
        "margin": "-1px",
        "overflow": "hidden",
        "clip": "rect(0, 0, 0, 0)",
        "white-space": "nowrap",
        "border-width": "0"
    }, is_important)

    # Not screen reader only (undo sr-only)
    add_rule(".not-sr-only", {
        "position": "static",
        "width": "auto",
        "height": "auto",
        "padding": "0",
        "margin": "0",
        "overflow": "visible",
        "clip": "auto",
        "white-space": "normal"
    }, is_important)

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
    generate_overflow(False)
    generate_zindex(False)
    generate_object(False)
    generate_aspect_ratio(False)
    generate_typography_extended(False)
    generate_interaction(False)
    generate_transforms(False)
    generate_sizing_extended(False)
    generate_flexgrid_extended(False)
    generate_accessibility(False)

    # Generate !important rules
    generate_spacing(True)
    generate_display(True)
    generate_position(True)
    generate_flex(True)
    generate_typography(True)
    generate_sizing(True)
    generate_borders(True)
    generate_effects(True)
    generate_overflow(True)
    generate_zindex(True)
    generate_object(True)
    generate_aspect_ratio(True)
    generate_typography_extended(True)
    generate_interaction(True)
    generate_transforms(True)
    generate_sizing_extended(True)
    generate_flexgrid_extended(True)
    generate_accessibility(True)
    
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

## Overflow
- `.overflow-{hidden|scroll|auto|visible}`
- `.overflow-x-{auto|hidden|scroll}`, `.overflow-y-{auto|hidden|scroll}`

## Z-Index
- `.z-{0|10|20|30|40|50|auto}`
- `.z-n{1|10}` (negative)

## Object Fit & Position
- `.object-fit-{cover|contain|fill|none|scale-down}`
- `.object-position-{center|top|bottom|left|right|top-left|...}`

## Aspect Ratio
- `.aspect-{square|video|4-3|3-2|16-9|21-9|1}`

## Flexbox
- `.flex-{row|column|...}`
- `.flex-{wrap|nowrap}`
- `.justify-content-{start|end|center|between|around|evenly}`
- `.align-items-{start|end|center|baseline|stretch}`
- `.align-content-{start|end|center|between|around|stretch}`
- `.align-self-{auto|start|end|center|baseline|stretch}`
- `.flex-grow-{0|1}`, `.flex-shrink-{0|1}`, `.flex-fill`
- `.gap-{0-10}` (0.25rem steps)
- `.order-{0-12|first|last|none}`

## Grid
- `.grid-cols-{1-12|none}` (template columns)
- `.col-span-{1-12|full}`
- `.grid-rows-{1-6|none}` (template rows)
- `.row-span-{1-6|full}`
- `.place-items-{center|start|end|stretch}`
- `.place-content-{center|start|end|stretch|between|around|evenly}`
- `.place-self-{center|start|end|stretch|auto}`

## Typography
- `.text-{start|end|center|justify}`
- `.text-{lowercase|uppercase|capitalize}`
- `.text-decoration-{none|underline|line-through}`
- `.text-{wrap|nowrap|break}`
- `.fw-{light|normal|bold|bolder|100-900}`
- `.fs-{1-6}` (headings scale)
- `.text-{color}`, `.bg-{color}` (using `var(--color-{name})`)
- `.lh-{1|sm|base|lg|xl}` (line-height)
- `.ls-{tighter|tight|normal|wide|wider|widest}` (letter-spacing)
- `.font-{sans|serif|mono}`
- `.ws-{normal|nowrap|pre|pre-wrap|pre-line|break-spaces}` (white-space)
- `.text-truncate`, `.truncate` (single line ellipsis)
- `.line-clamp-{1-6}` (multi-line truncation)

## Sizing
- `.w-{25|50|75|100|auto}`, `.h-{25|50|75|100|auto}`
- `.w-{1-100}px`, `.h-{1-100}px`
- `.mw-100`, `.mh-100`, `.vw-100`, `.vh-100`
- `.min-w-{0|full}`, `.min-h-{0|full|screen}`
- `.max-w-{xs|sm|md|lg|xl|2xl|3xl|4xl|5xl|6xl|7xl|full|prose|screen-sm|screen-md|screen-lg|screen-xl}`
- `.max-h-{full|screen}`

## Borders
- `.border`, `.border-{side}`, `.border-0`, `.border-{side}-0`
- `.border-{color}`
- `.rounded`, `.rounded-{0|circle|pill|sm|lg|xl}`

## Effects
- `.opacity-{0-100}` (step 5)
- `.cursor-{auto|pointer|...}`
- `.visible`, `.invisible`

## Transforms
- `.translate-x-{0|25|50|100}`, `.translate-y-{0|25|50|100}`
- `.translate-x-n{25|50|100}`, `.translate-y-n{25|50|100}` (negative)
- `.rotate-{0|45|90|180|270}`, `.rotate-n{45|90|180}` (negative)
- `.scale-{0|50|75|90|95|100|105|110|125|150}`

## Interaction
- `.pointer-events-{none|auto}`
- `.user-select-{none|text|all|auto}`
- `.touch-action-{none|pan-x|pan-y|manipulation|auto}`

## Accessibility
- `.sr-only` (screen reader only)
- `.not-sr-only` (undo sr-only)
"""
    
    with open(OUTPUT_DOCS_PATH, "w") as f:
        f.write(docs)
        
    print(f"Generated documentation at {OUTPUT_DOCS_PATH}")

if __name__ == "__main__":
    main()
