# Design System Reference
## Trust-Aware AI Learning Platform

## Quick Reference

### Color Variables
```css
--color-primary: #C46A4A        /* Terracotta - Primary actions */
--color-soft-accent: #F2C1AE    /* Soft peach - Secondary elements */
--color-background: #FAF6F3     /* Warm cream - Page background */
--color-card: #FFFDFB           /* Off-white - Card backgrounds */
--color-text-primary: #3A2E2A   /* Dark brown - Main text */
--color-warning: #E57373        /* Soft coral - Low confidence */
--color-success: #6B8E6B        /* Sage green - High confidence */
```

### Typography Scale
```css
--font-base: 16px      /* Body text, labels */
--font-large: 20px     /* Headings, important text */
--font-xlarge: 24px    /* Section titles */
--font-score: 28px     /* Confidence score display */
```

### Spacing Scale
```css
--spacing-xs: 0.5rem   /* 8px - Tight spacing */
--spacing-sm: 1rem     /* 16px - Small gaps */
--spacing-md: 1.5rem   /* 24px - Medium gaps */
--spacing-lg: 2rem     /* 32px - Large gaps */
--spacing-xl: 3rem     /* 48px - Section spacing */
```

### Border Radius
```css
--border-radius: 12px     /* Cards, large elements */
--border-radius-sm: 8px   /* Buttons, small elements */
```

### Shadows
```css
--shadow-soft: 0 2px 8px rgba(58, 46, 42, 0.08)
--shadow-card: 0 4px 12px rgba(58, 46, 42, 0.06)
```

## Component Patterns

### Card Pattern
```css
.card {
  background-color: var(--color-card);
  border: 1px solid var(--color-soft-accent);
  border-radius: var(--border-radius);
  box-shadow: var(--shadow-card);
  padding: var(--spacing-lg);
}
```

### Primary Button
```css
.primary-button {
  background-color: var(--color-primary);
  color: white;
  border: none;
  padding: 14px 32px;
  font-size: var(--font-large);
  font-weight: 600;
  border-radius: var(--border-radius-sm);
  cursor: pointer;
}
```

### Secondary Button
```css
.secondary-button {
  background-color: var(--color-soft-accent);
  color: var(--color-text-primary);
  border: 2px solid var(--color-soft-accent);
  padding: 12px 20px;
  font-size: var(--font-base);
  font-weight: 600;
  border-radius: var(--border-radius-sm);
  cursor: pointer;
}
```

### Handwritten Underline
```css
.handwritten-underline::after {
  content: '';
  position: absolute;
  left: 0;
  bottom: -4px;
  width: 100%;
  height: 2px;
  background-color: var(--color-primary);
  opacity: 0.6;
}
```

### Dashed Box (Pencil Sketch)
```css
.dashed-box {
  border: 2px dashed var(--color-soft-accent);
  border-radius: var(--border-radius-sm);
  padding: var(--spacing-md);
}
```

### Uncertain Text Highlight
```css
.uncertain-text {
  background-color: rgba(229, 115, 115, 0.12);
  padding: 2px 6px;
  border-radius: 4px;
  border-bottom: 2px solid var(--color-warning);
  font-weight: 500;
}
```

## Usage Guidelines

### When to Use Each Color

#### Primary (#C46A4A)
- Primary action buttons
- Important headings
- Focus states
- Active states
- Handwritten underlines

#### Soft Accent (#F2C1AE)
- Borders
- Secondary buttons
- Background tints (10-20% opacity)
- Dividers
- Subtle highlights

#### Background (#FAF6F3)
- Page background
- Header background
- Large sections

#### Card (#FFFDFB)
- Card backgrounds
- Input fields
- Content areas
- Modal backgrounds

#### Text Primary (#3A2E2A)
- All body text
- Headings
- Labels
- Icons

#### Warning (#E57373)
- Low confidence indicators
- Error states
- Uncertain text highlights
- Warning banners

#### Success (#6B8E6B)
- High confidence indicators
- Success states
- Positive feedback
- Completion indicators

### Typography Guidelines

#### Font Family
- **Primary**: Georgia, 'Times New Roman', serif
- **Fallback**: System serif stack
- **Never use**: Sans-serif fonts (breaks academic theme)

#### Font Sizes
- **Minimum**: 16px (accessibility requirement)
- **Body**: 16px
- **Large body**: 20px
- **Headings**: 20-24px
- **Display**: 28px+

#### Line Height
- **Body text**: 1.7-1.8
- **Headings**: 1.3
- **Tight**: 1.0 (scores, numbers)

#### Font Weight
- **Regular**: 400 (body text)
- **Semi-bold**: 600 (headings, buttons)
- **Bold**: 700 (emphasis only)

### Spacing Guidelines

#### Vertical Rhythm
- Between sections: `var(--spacing-xl)` (3rem)
- Between elements: `var(--spacing-lg)` (2rem)
- Between related items: `var(--spacing-md)` (1.5rem)
- Between labels and inputs: `var(--spacing-sm)` (1rem)
- Between inline elements: `var(--spacing-xs)` (0.5rem)

#### Padding
- Cards: `var(--spacing-lg)` (2rem)
- Buttons: 12-16px vertical, 20-32px horizontal
- Inputs: `var(--spacing-md)` (1.5rem)
- Small elements: `var(--spacing-sm)` (1rem)

### Border Guidelines

#### Border Styles
- **Subtle**: 1px solid `var(--color-soft-accent)`
- **Emphasis**: 2-3px solid `var(--color-primary)`
- **Dashed**: 2px dashed `var(--color-soft-accent)`
- **None**: For seamless elements

#### Border Radius
- **Cards**: 12px
- **Buttons**: 8px
- **Small elements**: 4-6px
- **Circles**: 50%

### Shadow Guidelines

#### When to Use Shadows
- Cards (always)
- Elevated buttons (on hover)
- Modals and overlays
- Dropdowns

#### When NOT to Use Shadows
- Flat buttons
- Text elements
- Borders (use borders instead)
- Background elements

### Accessibility Guidelines

#### Color Contrast
- Text on background: Minimum 4.5:1 ratio
- Large text: Minimum 3:1 ratio
- Interactive elements: Clear visual distinction

#### Focus States
- Always visible: 2px solid outline
- Color: `var(--color-primary)`
- Offset: 2px
- Never remove: `outline: none` forbidden

#### Touch Targets
- Minimum size: 44x44px
- Spacing: 8px between targets
- Clear hit areas

#### Text
- Minimum size: 16px
- Maximum line length: 720px
- Clear hierarchy
- Sufficient contrast

## Responsive Breakpoints

```css
/* Mobile */
@media (max-width: 768px) {
  /* Stack elements vertically */
  /* Increase touch targets */
  /* Reduce font sizes slightly */
}

/* Tablet */
@media (min-width: 769px) and (max-width: 1024px) {
  /* Optimize for medium screens */
}

/* Desktop */
@media (min-width: 1025px) {
  /* Full layout */
  /* Max width: 720px centered */
}
```

## Animation Guidelines

### Allowed Animations
- Color transitions (0.2s ease)
- Opacity fades (0.2s ease)
- Subtle scale (max 1.02x)

### Forbidden Animations
- Transform translateY
- Rotate
- Skew
- Complex keyframes
- Flashy effects

### Timing
- Fast: 0.15s (micro-interactions)
- Standard: 0.2s (most transitions)
- Slow: 0.3s (large elements)

## High Contrast Mode

### Overrides
```css
.high-contrast {
  --color-background: #FFFFFF;
  --color-card: #FFFFFF;
  --color-text-primary: #000000;
  --color-primary: #8B4513;
}

.high-contrast .card {
  border: 2px solid var(--color-text-primary);
}
```

### When to Use
- User preference
- Low vision users
- Bright environments
- Accessibility compliance

## Common Patterns

### Section Header
```html
<h3 class="section-header">Section Title</h3>
```
```css
.section-header {
  font-size: var(--font-xlarge);
  color: var(--color-text-primary);
  margin-bottom: var(--spacing-md);
  position: relative;
  display: inline-block;
}

.section-header::after {
  content: '';
  position: absolute;
  left: 0;
  bottom: -4px;
  width: 100%;
  height: 2px;
  background-color: var(--color-primary);
  opacity: 0.4;
}
```

### Info Card
```html
<div class="info-card">
  <h4>Card Title</h4>
  <p>Card content...</p>
</div>
```
```css
.info-card {
  background-color: rgba(242, 193, 174, 0.1);
  border-left: 3px solid var(--color-primary);
  padding: var(--spacing-md);
  border-radius: var(--border-radius-sm);
}
```

### Warning Banner
```html
<div class="warning-banner">
  ⚠️ Warning message
</div>
```
```css
.warning-banner {
  background-color: rgba(229, 115, 115, 0.15);
  border: 2px solid var(--color-warning);
  color: var(--color-text-primary);
  padding: var(--spacing-md);
  border-radius: var(--border-radius-sm);
  font-weight: 600;
}
```

## Do's and Don'ts

### ✅ Do
- Use warm, muted colors from palette
- Maintain generous spacing
- Use serif fonts
- Keep animations subtle
- Ensure high contrast
- Make touch targets large
- Use handwritten underlines
- Apply dashed borders for emphasis

### ❌ Don't
- Use colors outside palette
- Add gradients
- Use sans-serif fonts
- Create flashy animations
- Use tiny text (< 16px)
- Add gamification elements
- Use harsh shadows
- Create multi-column layouts

---

## Quick Start Checklist

When creating a new component:
- [ ] Use colors from palette only
- [ ] Set minimum font size to 16px
- [ ] Add generous padding (1.5-2rem)
- [ ] Use serif font (Georgia)
- [ ] Add focus states
- [ ] Ensure 44x44px touch targets
- [ ] Test in high contrast mode
- [ ] Verify keyboard navigation
- [ ] Check color contrast ratio
- [ ] Apply consistent border radius

---

**Remember**: This is a trustworthy study notebook, not a flashy tech product. Keep it warm, calm, and accessible.
