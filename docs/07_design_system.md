# Design System Guide

## Philosophy
The KofC design system prioritizes **Clarity, Consistency, and Professionalism**. It uses a dedicated CSS variable system to ensure theming capabilities and ease of maintenance.

## Color Palette

### Primary Colors (Blue)
Used for primary actions, headers, and active states.
- `--primary-50`: `#eff6ff` (Backgrounds)
- `--primary-100`: `#dbeafe`
- `--primary-500`: `#3b82f6` (Primary Buttons/Links)
- `--primary-600`: `#2563eb` (Hover states)
- `--primary-900`: `#1e3a8a` (Headers/Dark accents)

### Neutral Colors (Grays)
Used for text, borders, and backgrounds.
- `--neutral-50`: `#f9fafb` (Page Background)
- `--neutral-200`: `#e5e7eb` (Borders)
- `--neutral-900`: `#111827` (Body Text)

### Semantic Colors
- **Success**: `--success-600` (Green) - Completed actions, approvals.
- **Warning**: `--warning-600` (Yellow/Orange) - Pending states.
- **Danger**: `--danger-600` (Red) - Deletions, errors, rejections.

## Components

### 1. Cards
Standard container for content.
```html
<div class="card">
  <div class="card-header">Title</div>
  <div class="card-body">Content</div>
</div>
```
*Rounding*: `var(--radius-xl)` (12px or 16px).

### 2. Buttons
```html
<button class="btn btn--primary">Primary Action</button>
<button class="btn btn--secondary">Secondary Action</button>
<button class="btn btn--danger">Destructive Action</button>
<button class="btn btn--ghost">Transparent/Text Button</button>
```

### 3. Breadcrumbs
Deep navigation aid.
```html
<div class="breadcrumbs">
  <span class="breadcrumb-item">Section</span>
  <span class="breadcrumb-separator">/</span>
  <span class="breadcrumb-item current">Current Page</span>
</div>
```

### 4. Tables
Modern, clean data display.
```html
<table class="table">
  <thead>...</thead>
  <tbody>...</tbody>
</table>
```
- Use `<thead>` with light gray background.
- Row hover effects enabled by default.

### 5. Forms
- Inputs should have `border-radius: var(--radius-lg)`.
- Focus states must have a ring shadow (`box-shadow: 0 0 0 3px ...`).

## Typography
- **Font Family**: 'Inter', sans-serif.
- **Headings**: semi-bold/bold.
- **Body**: regular (400) or medium (500).

## Layout
- **Sidebar**: Fixed width, dark/primary styled.
- **Content Area**: Flexible width, padded (`var(--space-6)`).
- **Grid Systems**: Use CSS Grid for dashboards (`grid-template-columns: repeat(auto-fit, minmax(250px, 1fr))`).
