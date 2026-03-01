# Frontend Folder Structure

## Updated Structure After UI Upgrade

```
frontend/
├── node_modules/              # Dependencies (not tracked)
├── public/                    # Static assets
├── src/
│   ├── components/            # React components (unchanged)
│   │   ├── .gitkeep
│   │   ├── ChallengeDisplay.tsx
│   │   ├── ConfidenceDisplay.tsx
│   │   ├── QueryInterface.tsx
│   │   └── SimplificationToggle.tsx
│   │
│   ├── services/              # API services (unchanged)
│   │   ├── .gitkeep
│   │   └── api.ts
│   │
│   ├── styles/                # ✨ NEW - Design system
│   │   ├── variables.css      # Design tokens
│   │   └── theme.css          # Theme system
│   │
│   ├── types/                 # TypeScript types (unchanged)
│   │   ├── .gitkeep
│   │   └── index.ts
│   │
│   ├── App.tsx                # ✏️ UPDATED - Added contrast toggle
│   ├── index.css              # ✏️ UPDATED - Complete redesign
│   ├── main.tsx               # Entry point (unchanged)
│   └── vite-env.d.ts          # Vite types (unchanged)
│
├── index.html                 # HTML template (unchanged)
├── package.json               # Dependencies (unchanged)
├── package-lock.json          # Lock file (unchanged)
├── tsconfig.json              # TypeScript config (unchanged)
├── tsconfig.node.json         # Node TypeScript config (unchanged)
├── vite.config.ts             # Vite config (unchanged)
│
├── README.md                  # Project readme (unchanged)
├── IMPLEMENTATION_SUMMARY.md  # Implementation notes (unchanged)
├── TESTING.md                 # Testing guide (unchanged)
│
└── 📚 NEW DOCUMENTATION
    ├── UI_UPGRADE_SUMMARY.md          # Comprehensive upgrade details
    ├── DESIGN_COMPARISON.md           # Before/after comparison
    ├── DESIGN_SYSTEM.md               # Design system reference
    ├── COLOR_PALETTE_REFERENCE.md     # Color palette guide
    ├── FOLDER_STRUCTURE.md            # This file
    └── UPGRADE_COMPLETE.md            # Completion summary
```

## File Descriptions

### Core Application Files

#### `src/App.tsx` ✏️ UPDATED
- Main application component
- Added high contrast mode toggle
- Manages global theme state
- Renders header, main content, and footer

#### `src/index.css` ✏️ UPDATED
- Main stylesheet with complete redesign
- Imports theme and variables
- Implements all component styles
- Responsive design rules
- Print styles

#### `src/main.tsx` (unchanged)
- Application entry point
- Renders React app to DOM
- No changes needed

### New Design System Files

#### `src/styles/variables.css` ✨ NEW
- CSS custom properties (variables)
- Color palette definitions
- Typography scale
- Spacing scale
- Border radius values
- Shadow definitions
- Focus outline styles

#### `src/styles/theme.css` ✨ NEW
- Base theme styles
- Typography rules
- Focus state definitions
- Button base styles
- Card patterns
- Handwritten underline effect
- Dashed box pattern
- High contrast mode overrides

### Component Files (Logic Unchanged)

#### `src/components/QueryInterface.tsx`
- Main query interface
- Handles user input
- Displays AI responses
- Manages loading states
- Coordinates child components
- **No logic changes** - only styled via CSS

#### `src/components/ConfidenceDisplay.tsx`
- Displays confidence score
- Shows breakdown indicators
- Renders justification
- Warning banner logic
- **No logic changes** - only styled via CSS

#### `src/components/ChallengeDisplay.tsx`
- Displays challenge questions
- Close button functionality
- **No logic changes** - only styled via CSS

#### `src/components/SimplificationToggle.tsx`
- Toggles between original/simplified
- Manages toggle state
- **No logic changes** - only styled via CSS

### Service Files (Unchanged)

#### `src/services/api.ts`
- API client functions
- HTTP request handling
- Error handling
- **No changes**

### Type Files (Unchanged)

#### `src/types/index.ts`
- TypeScript type definitions
- Interface declarations
- **No changes**

### Configuration Files (Unchanged)

#### `package.json`
- Project dependencies
- Scripts
- **No changes**

#### `tsconfig.json`
- TypeScript compiler options
- **No changes**

#### `vite.config.ts`
- Vite build configuration
- **No changes**

### Documentation Files

#### `README.md` (unchanged)
- Project overview
- Setup instructions
- Usage guide

#### `IMPLEMENTATION_SUMMARY.md` (unchanged)
- Original implementation notes
- Component descriptions

#### `TESTING.md` (unchanged)
- Testing instructions
- Test scenarios

#### `UI_UPGRADE_SUMMARY.md` ✨ NEW
- Comprehensive upgrade documentation
- Design goals and implementation
- Component refactoring details
- Accessibility enhancements
- File changes summary

#### `DESIGN_COMPARISON.md` ✨ NEW
- Before/after visual comparison
- Component-by-component changes
- Color palette transformation
- Typography changes
- Layout changes

#### `DESIGN_SYSTEM.md` ✨ NEW
- Complete design system reference
- Color usage guidelines
- Typography guidelines
- Spacing guidelines
- Component patterns
- Do's and don'ts

#### `COLOR_PALETTE_REFERENCE.md` ✨ NEW
- Detailed color specifications
- RGB, HSL, hex values
- Usage examples
- Opacity variations
- Accessibility notes

#### `FOLDER_STRUCTURE.md` ✨ NEW
- This file
- Folder organization
- File descriptions

#### `UPGRADE_COMPLETE.md` ✨ NEW
- Completion summary
- Testing instructions
- Success criteria
- Next steps

## Import Structure

### CSS Imports
```
index.css
  └── imports theme.css
        └── imports variables.css
```

### Component Imports
```
main.tsx
  └── imports App.tsx
        └── imports QueryInterface.tsx
              ├── imports ConfidenceDisplay.tsx
              ├── imports ChallengeDisplay.tsx
              └── imports SimplificationToggle.tsx
```

### Service Imports
```
QueryInterface.tsx
  └── imports api.ts
```

### Type Imports
```
All components
  └── import types from types/index.ts
```

## File Size Overview

### CSS Files
- `variables.css`: ~1KB
- `theme.css`: ~2KB
- `index.css`: ~9KB
- **Total CSS**: ~12KB

### Component Files
- `App.tsx`: ~1KB
- `QueryInterface.tsx`: ~6KB
- `ConfidenceDisplay.tsx`: ~2KB
- `ChallengeDisplay.tsx`: ~1KB
- `SimplificationToggle.tsx`: ~1KB
- **Total Components**: ~11KB

### Documentation Files
- `UI_UPGRADE_SUMMARY.md`: ~8KB
- `DESIGN_COMPARISON.md`: ~6KB
- `DESIGN_SYSTEM.md`: ~10KB
- `COLOR_PALETTE_REFERENCE.md`: ~8KB
- `FOLDER_STRUCTURE.md`: ~4KB
- `UPGRADE_COMPLETE.md`: ~6KB
- **Total Documentation**: ~42KB

## Key Changes Summary

### ✨ New Files (8)
1. `src/styles/variables.css`
2. `src/styles/theme.css`
3. `UI_UPGRADE_SUMMARY.md`
4. `DESIGN_COMPARISON.md`
5. `DESIGN_SYSTEM.md`
6. `COLOR_PALETTE_REFERENCE.md`
7. `FOLDER_STRUCTURE.md`
8. `UPGRADE_COMPLETE.md`

### ✏️ Updated Files (2)
1. `src/App.tsx` - Added contrast toggle
2. `src/index.css` - Complete redesign

### 🔒 Unchanged Files (11)
1. `src/components/QueryInterface.tsx`
2. `src/components/ConfidenceDisplay.tsx`
3. `src/components/ChallengeDisplay.tsx`
4. `src/components/SimplificationToggle.tsx`
5. `src/services/api.ts`
6. `src/types/index.ts`
7. `src/main.tsx`
8. `package.json`
9. `tsconfig.json`
10. `vite.config.ts`
11. `index.html`

## Development Workflow

### Starting Development
```bash
cd frontend
npm install  # If needed
npm run dev  # Start dev server
```

### Building for Production
```bash
npm run build  # Build optimized bundle
npm run preview  # Preview production build
```

### File Organization Best Practices

#### When adding new components:
1. Create in `src/components/`
2. Use existing CSS classes from `index.css`
3. Follow design system in `DESIGN_SYSTEM.md`
4. Use colors from `COLOR_PALETTE_REFERENCE.md`

#### When modifying styles:
1. Check `variables.css` for design tokens
2. Use existing CSS variables
3. Follow patterns in `theme.css`
4. Maintain consistency with design system

#### When adding documentation:
1. Place in `frontend/` root
2. Use `.md` extension
3. Follow existing documentation style
4. Update this file if structure changes

## Maintenance Notes

### To update colors:
1. Edit `src/styles/variables.css`
2. Update `COLOR_PALETTE_REFERENCE.md`
3. Test all components
4. Verify accessibility

### To update typography:
1. Edit `src/styles/variables.css`
2. Update `DESIGN_SYSTEM.md`
3. Test readability
4. Verify accessibility

### To add new components:
1. Create in `src/components/`
2. Use existing CSS patterns
3. Follow design system
4. Document if needed

### To modify layout:
1. Edit `src/index.css`
2. Maintain single-column structure
3. Keep max-width: 720px
4. Test responsiveness

---

## Quick Navigation

- **Design System**: See `DESIGN_SYSTEM.md`
- **Color Reference**: See `COLOR_PALETTE_REFERENCE.md`
- **Upgrade Details**: See `UI_UPGRADE_SUMMARY.md`
- **Before/After**: See `DESIGN_COMPARISON.md`
- **Completion Status**: See `UPGRADE_COMPLETE.md`

---

**Last Updated**: After UI upgrade to Clean Academic Minimal theme  
**Structure Status**: ✅ Organized and documented  
**Breaking Changes**: None  
**Backward Compatibility**: 100%
