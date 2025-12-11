# CSS utils generator
## Features
> Generates a minified file for CSS utility classes.
> Generates a guide file for quick explaination and for feeding into AI models with as few tokens as possible.

## Requirements:
> Tested on Python 3.13, will probably work on Python 3.6 and newer
> Requires a `../../static/css` directory by default.
> The brotli command line tool

## CSS Variables
The following CSS variables are used:

```css
:root {
  /* Primary action (buttons, focus states) */
  --color-primary-from: #2a2d35;
  --color-primary-to: #3d4150;
  --color-primary: #2a2d35;

  /* Semantic colors */
  --color-danger-from: #c94a4a;
  --color-danger-to: #e86b6b;
  --color-danger: #c94a4a;

  --color-success-from: #3d9447;
  --color-success-to: #5cb866;
  --color-success: #3d9447;

  --color-warning: #c9940a;
  --color-info: #4f56c2;

  --color-link: #8ab4f8;

  /* Surfaces */
  --bg-page: #f5f6f8;
  --bg-surface: #ffffff;
  --bg-surface-elevated: #ffffff;
  --bg-surface-hover: #f0f1f4;
  --bg-surface-sunken: #f8f9fa;

  /* Borders */
  --border-subtle: rgba(0, 0, 0, 0.06);
  --border-default: rgba(0, 0, 0, 0.1);
  --border-focus: rgba(42, 45, 53, 0.4);

  /* Text */
  --text-primary: #1a1d27;
  --text-secondary: rgba(26, 29, 39, 0.7);
  --text-tertiary: rgba(26, 29, 39, 0.5);
  --text-on-primary: #ffffff;

  /* Buttons */
  --btn-primary-from: var(--color-primary-from);
  --btn-primary-to: var(--color-primary-to);
  --btn-primary-inset: rgba(255, 255, 255, 0.2);
  --btn-primary-shadow: 0 2px 8px -2px rgba(42, 45, 53, 0.3);

  --btn-secondary-bg: rgba(0, 0, 0, 0.04);
  --btn-secondary-border: rgba(0, 0, 0, 0.12);

  --btn-danger-from: var(--color-danger-from);
  --btn-danger-to: var(--color-danger-to);
  --btn-danger-shadow: 0 2px 8px -2px rgba(201, 74, 74, 0.3);

  --btn-success-from: var(--color-success-from);
  --btn-success-to: var(--color-success-to);
  --btn-success-shadow: 0 2px 8px -2px rgba(61, 148, 71, 0.3);

  /* Inputs */
  --input-bg: linear-gradient(
    180deg,
    rgba(0, 0, 0, 0.02) 0%,
    rgba(0, 0, 0, 0.01) 100%
  );
  --input-bg-hover: linear-gradient(
    180deg,
    rgba(0, 0, 0, 0.03) 0%,
    rgba(0, 0, 0, 0.015) 100%
  );
  --input-bg-focus: linear-gradient(
    180deg,
    rgba(42, 45, 53, 0.06) 0%,
    rgba(42, 45, 53, 0.02) 100%
  );
  --input-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.06);

  /* Checkbox */
  --checkbox-bg: linear-gradient(
    180deg,
    rgba(0, 0, 0, 0.04) 0%,
    rgba(0, 0, 0, 0.02) 100%
  );
  --checkbox-bg-hover: linear-gradient(
    180deg,
    rgba(0, 0, 0, 0.06) 0%,
    rgba(0, 0, 0, 0.03) 100%
  );
  --checkbox-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.08);
  --checkbox-check-color: #ffffff;

  /* Focus/Glow */
  --focus-glow: rgba(42, 45, 53, 0.1);
  --focus-glow-strong: rgba(42, 45, 53, 0.2);

  /* Shadows */
  --dropdown-shadow: 0 8px 30px -8px rgba(0, 0, 0, 0.15),
    0 4px 12px -4px rgba(0, 0, 0, 0.1);
  --card-shadow: 0 2px 8px -2px rgba(0, 0, 0, 0.08);
  --card-shadow-elevated: 0 4px 24px -4px rgba(0, 0, 0, 0.12);

  /* Accent (for highlights, selections, active states) */
  --accent: #4f56c2;
  --accent-dim: rgba(79, 86, 194, 0.12);

  /* Spacing */
  --spacing-xs: 4px;
  --spacing-sm: 8px;
  --spacing-md: 12px;
  --spacing-lg: 16px;
  --spacing-xl: 24px;
  --spacing-2xl: 32px;

  /* Typography */
  --font-family: "Satoshi", -apple-system, BlinkMacSystemFont, "Segoe UI",
    Roboto, sans-serif;
  --font-size-xs: 11px;
  --font-size-sm: 13px;
  --font-size-md: 14px;
  --font-size-lg: 16px;
  --font-size-xl: 20px;
  --font-size-2xl: 24px;

  /* Border Radius */
  --radius-sm: 6px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --radius-xl: 16px;

  /* Layout */
  --sidebar-width: 240px;
  --sidebar-gap: 12px;
  --topbar-height: 56px;
}

body.dark-mode {
  /* Primary action */
  --color-primary-from: #5b63d3;
  --color-primary-to: #7c87f7;
  --color-primary: #7c87f7;

  /* Semantic colors */
  --color-danger-from: #d35b5b;
  --color-danger-to: #f77c7c;
  --color-danger: #f77c7c;

  --color-success-from: #4aa854;
  --color-success-to: #6fcf7a;
  --color-success: #6fcf7a;

  --color-warning: #f7c77c;
  --color-info: #7c87f7;

  --color-link: #8ab4f8;

  /* Surfaces */
  --bg-page: #0f1117;
  --bg-surface: #1a1d27;
  --bg-surface-elevated: #242836;
  --bg-surface-hover: #2a2f3d;
  --bg-surface-sunken: #14161e;

  /* Borders */
  --border-subtle: rgba(255, 255, 255, 0.08);
  --border-default: rgba(255, 255, 255, 0.12);
  --border-focus: rgba(124, 135, 247, 0.5);

  /* Text */
  --text-primary: #ffffff;
  --text-secondary: rgba(255, 255, 255, 0.7);
  --text-tertiary: rgba(255, 255, 255, 0.5);
  --text-on-primary: #ffffff;

  /* Buttons */
  --btn-primary-from: var(--color-primary-from);
  --btn-primary-to: var(--color-primary-to);
  --btn-primary-inset: rgba(255, 255, 255, 0.25);
  --btn-primary-shadow: 0 2px 8px -2px rgba(91, 99, 211, 0.4);

  --btn-secondary-bg: rgba(255, 255, 255, 0.08);
  --btn-secondary-border: rgba(255, 255, 255, 0.15);

  --btn-danger-from: var(--color-danger-from);
  --btn-danger-to: var(--color-danger-to);
  --btn-danger-shadow: 0 2px 8px -2px rgba(211, 91, 91, 0.4);

  --btn-success-from: var(--color-success-from);
  --btn-success-to: var(--color-success-to);
  --btn-success-shadow: 0 2px 8px -2px rgba(74, 168, 84, 0.4);

  /* Inputs */
  --input-bg: linear-gradient(
    180deg,
    rgba(0, 0, 0, 0.2) 0%,
    rgba(0, 0, 0, 0.1) 100%
  );
  --input-bg-hover: linear-gradient(
    180deg,
    rgba(0, 0, 0, 0.15) 0%,
    rgba(0, 0, 0, 0.05) 100%
  );
  --input-bg-focus: linear-gradient(
    180deg,
    rgba(91, 99, 211, 0.08) 0%,
    rgba(91, 99, 211, 0.02) 100%
  );
  --input-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.1);

  /* Checkbox */
  --checkbox-bg: linear-gradient(
    180deg,
    rgba(0, 0, 0, 0.3) 0%,
    rgba(0, 0, 0, 0.15) 100%
  );
  --checkbox-bg-hover: linear-gradient(
    180deg,
    rgba(0, 0, 0, 0.25) 0%,
    rgba(0, 0, 0, 0.1) 100%
  );
  --checkbox-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.2);
  --checkbox-check-color: #0f1117;

  /* Focus/Glow */
  --focus-glow: rgba(124, 135, 247, 0.15);
  --focus-glow-strong: rgba(124, 135, 247, 0.3);

  /* Shadows */
  --dropdown-shadow: 0 12px 40px -8px rgba(0, 0, 0, 0.6),
    0 4px 16px -4px rgba(0, 0, 0, 0.4);
  --card-shadow: 0 2px 8px -2px rgba(0, 0, 0, 0.3);
  --card-shadow-elevated: 0 4px 24px -4px rgba(0, 0, 0, 0.5),
    inset 0 1px 0 rgba(255, 255, 255, 0.05);

  /* Accent */
  --accent: #7c87f7;
  --accent-dim: rgba(124, 135, 247, 0.15);
}
```
