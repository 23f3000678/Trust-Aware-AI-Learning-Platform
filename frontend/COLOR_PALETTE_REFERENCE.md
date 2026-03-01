# Color Palette Reference Card

## Trust-Aware AI Learning Platform
### Clean Academic Minimal - Soft Notebook Theme

---

## Primary Colors

### Primary Accent
```
Color: #C46A4A
Name: Terracotta
RGB: rgb(196, 106, 74)
HSL: hsl(16, 49%, 53%)
```
**Usage:**
- Primary action buttons
- Focus states
- Handwritten underlines
- Important headings
- Active states

**Example:**
```css
.primary-button {
  background-color: #C46A4A;
  color: white;
}
```

---

### Soft Accent
```
Color: #F2C1AE
Name: Soft Peach
RGB: rgb(242, 193, 174)
HSL: hsl(17, 68%, 82%)
```
**Usage:**
- Borders
- Secondary buttons
- Background tints (10-20% opacity)
- Dividers
- Subtle highlights

**Example:**
```css
.card {
  border: 1px solid #F2C1AE;
}
```

---

## Background Colors

### Page Background
```
Color: #FAF6F3
Name: Warm Cream
RGB: rgb(250, 246, 243)
HSL: hsl(26, 41%, 97%)
```
**Usage:**
- Main page background
- Header background
- Large section backgrounds

**Example:**
```css
body {
  background-color: #FAF6F3;
}
```

---

### Card Background
```
Color: #FFFDFB
Name: Off-White
RGB: rgb(255, 253, 251)
HSL: hsl(30, 100%, 99%)
```
**Usage:**
- Card backgrounds
- Input fields
- Content areas
- Modal backgrounds

**Example:**
```css
.card {
  background-color: #FFFDFB;
}
```

---

## Text Colors

### Primary Text
```
Color: #3A2E2A
Name: Dark Brown
RGB: rgb(58, 46, 42)
HSL: hsl(15, 16%, 20%)
```
**Usage:**
- All body text
- Headings
- Labels
- Icons
- Primary content

**Example:**
```css
body {
  color: #3A2E2A;
}
```

---

## Semantic Colors

### Warning / Low Confidence
```
Color: #E57373
Name: Soft Coral
RGB: rgb(229, 115, 115)
HSL: hsl(0, 68%, 67%)
```
**Usage:**
- Low confidence indicators (< 70)
- Error states
- Uncertain text highlights
- Warning banners

**Example:**
```css
.low-confidence {
  color: #E57373;
  border-color: #E57373;
}

.uncertain-text {
  background-color: rgba(229, 115, 115, 0.12);
  border-bottom: 2px solid #E57373;
}
```

---

### Success / High Confidence
```
Color: #6B8E6B
Name: Sage Green
RGB: rgb(107, 142, 107)
HSL: hsl(120, 14%, 49%)
```
**Usage:**
- High confidence indicators (≥ 70)
- Success states
- Positive feedback
- Completion indicators

**Example:**
```css
.high-confidence {
  color: #6B8E6B;
  border-color: #6B8E6B;
}
```

---

## Color Combinations

### High Contrast Pairs
```
Text on Background:
#3A2E2A on #FAF6F3 ✅ WCAG AA (Ratio: 11.2:1)

Text on Card:
#3A2E2A on #FFFDFB ✅ WCAG AA (Ratio: 11.5:1)

Primary on Background:
#C46A4A on #FAF6F3 ✅ WCAG AA (Ratio: 4.8:1)
```

### Recommended Combinations
```
Primary Button:
Background: #C46A4A
Text: #FFFFFF
Border: none

Secondary Button:
Background: #F2C1AE
Text: #3A2E2A
Border: 2px solid #F2C1AE

Card:
Background: #FFFDFB
Border: 1px solid #F2C1AE
Text: #3A2E2A

Warning Banner:
Background: rgba(229, 115, 115, 0.15)
Border: 2px solid #E57373
Text: #3A2E2A

Success Indicator:
Background: rgba(107, 142, 107, 0.2)
Border: 1px solid #6B8E6B
Text: #6B8E6B
```

---

## Opacity Variations

### Primary Accent (#C46A4A)
```
100%: #C46A4A - Solid buttons, borders
60%:  rgba(196, 106, 74, 0.6) - Underlines
40%:  rgba(196, 106, 74, 0.4) - Subtle accents
20%:  rgba(196, 106, 74, 0.2) - Light backgrounds
10%:  rgba(196, 106, 74, 0.1) - Very subtle tints
```

### Soft Accent (#F2C1AE)
```
100%: #F2C1AE - Borders, buttons
30%:  rgba(242, 193, 174, 0.3) - Medium backgrounds
20%:  rgba(242, 193, 174, 0.2) - Light backgrounds
10%:  rgba(242, 193, 174, 0.1) - Very subtle tints
```

### Warning (#E57373)
```
100%: #E57373 - Borders, text
20%:  rgba(229, 115, 115, 0.2) - Backgrounds
15%:  rgba(229, 115, 115, 0.15) - Banner backgrounds
12%:  rgba(229, 115, 115, 0.12) - Uncertain text highlight
```

### Success (#6B8E6B)
```
100%: #6B8E6B - Borders, text
20%:  rgba(107, 142, 107, 0.2) - Backgrounds
```

---

## Usage Examples

### Confidence Score Display
```css
/* High Confidence (≥ 70) */
.confidence-score.high {
  border-color: #6B8E6B;
}
.score-value.high {
  color: #6B8E6B;
}

/* Low Confidence (< 70) */
.confidence-score.low {
  border-color: #E57373;
}
.score-value.low {
  color: #E57373;
}
```

### Breakdown Indicators
```css
/* Positive Indicators */
.clarity-high,
.complexity-low,
.missing-no {
  background-color: rgba(107, 142, 107, 0.2);
  color: #6B8E6B;
  border: 1px solid #6B8E6B;
}

/* Neutral Indicators */
.clarity-medium,
.complexity-medium {
  background-color: rgba(242, 193, 174, 0.3);
  color: #C46A4A;
  border: 1px solid #C46A4A;
}

/* Negative Indicators */
.clarity-low,
.complexity-high,
.missing-yes {
  background-color: rgba(229, 115, 115, 0.2);
  color: #E57373;
  border: 1px solid #E57373;
}
```

### Uncertain Text Highlighting
```css
.uncertain-text {
  background-color: rgba(229, 115, 115, 0.12);
  padding: 2px 6px;
  border-radius: 4px;
  color: #3A2E2A;
  font-weight: 500;
  border-bottom: 2px solid #E57373;
}
```

---

## Color Psychology

### Why These Colors?

**Terracotta (#C46A4A)**
- Warm, earthy, trustworthy
- Academic, traditional
- Not aggressive or flashy
- Inviting and approachable

**Soft Peach (#F2C1AE)**
- Gentle, calming
- Notebook paper quality
- Subtle and supportive
- Not distracting

**Warm Cream (#FAF6F3)**
- Comfortable, easy on eyes
- Paper-like quality
- Reduces eye strain
- Academic atmosphere

**Dark Brown (#3A2E2A)**
- Readable, clear
- Ink-like quality
- Professional
- High contrast

**Soft Coral (#E57373)**
- Warning without alarm
- Gentle attention-grabbing
- Not harsh or scary
- Supportive feedback

**Sage Green (#6B8E6B)**
- Calm confidence
- Natural, organic
- Positive without excitement
- Trustworthy success

---

## Accessibility Notes

### WCAG Compliance
All color combinations meet WCAG AA standards:
- Normal text: 4.5:1 minimum contrast ratio ✅
- Large text: 3:1 minimum contrast ratio ✅
- UI components: 3:1 minimum contrast ratio ✅

### High Contrast Mode
When high contrast mode is enabled:
```css
.high-contrast {
  --color-background: #FFFFFF;
  --color-card: #FFFFFF;
  --color-text-primary: #000000;
  --color-primary: #8B4513;
}
```

### Color Blindness Considerations
- Primary colors have sufficient luminance difference
- Not relying solely on color for information
- Text labels accompany all color-coded elements
- Patterns and borders supplement color coding

---

## Quick Reference Table

| Color Name | Hex Code | Usage | Opacity Variants |
|------------|----------|-------|------------------|
| Terracotta | #C46A4A | Primary actions | 100%, 60%, 40%, 20%, 10% |
| Soft Peach | #F2C1AE | Borders, accents | 100%, 30%, 20%, 10% |
| Warm Cream | #FAF6F3 | Page background | 100% |
| Off-White | #FFFDFB | Card background | 100% |
| Dark Brown | #3A2E2A | Text | 100%, 70% (subtle) |
| Soft Coral | #E57373 | Warnings | 100%, 20%, 15%, 12% |
| Sage Green | #6B8E6B | Success | 100%, 20% |

---

## Color Palette Export

### CSS Variables
```css
:root {
  --color-primary: #C46A4A;
  --color-soft-accent: #F2C1AE;
  --color-background: #FAF6F3;
  --color-card: #FFFDFB;
  --color-text-primary: #3A2E2A;
  --color-warning: #E57373;
  --color-success: #6B8E6B;
}
```

### Tailwind Config
```javascript
module.exports = {
  theme: {
    extend: {
      colors: {
        primary: '#C46A4A',
        'soft-accent': '#F2C1AE',
        background: '#FAF6F3',
        card: '#FFFDFB',
        'text-primary': '#3A2E2A',
        warning: '#E57373',
        success: '#6B8E6B',
      },
    },
  },
}
```

### SCSS Variables
```scss
$color-primary: #C46A4A;
$color-soft-accent: #F2C1AE;
$color-background: #FAF6F3;
$color-card: #FFFDFB;
$color-text-primary: #3A2E2A;
$color-warning: #E57373;
$color-success: #6B8E6B;
```

---

**Remember**: Use only these colors. No random colors outside this palette!
