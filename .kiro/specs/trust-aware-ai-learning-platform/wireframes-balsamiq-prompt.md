# Balsamiq Wireframe Mockup Prompt for Trust-Aware AI Learning Platform

## Overview
Create Balsamiq wireframe mockups for a Trust-Aware, Inclusive AI Learning Platform that emphasizes trust calibration, explainability, and accessibility. The platform uses cognitive engagement over gamification.

---

## Screen 1: Main Query Interface (Prototype - Phase 1)

### Layout Description
**Header Section:**
- Platform logo/title: "Trust-Aware AI Learning Platform"
- Accessibility controls: High Contrast toggle, Font Size selector
- Help icon (?)

**Main Content Area:**
- Large text input box with placeholder: "Ask your question here..."
- Submit button: "Ask AI"
- Toggle switches below input:
  - "Enable Challenge Mode" (checkbox)
  - "Simplify Response" (checkbox)

**Response Display Area:**
- Card-based layout showing AI response
- Confidence Score Badge (prominent): "Confidence: 85%" with color coding:
  - Green (70-100%): High confidence
  - Yellow (50-69%): Medium confidence  
  - Red (0-49%): Low confidence with warning icon
- Warning banner (when confidence < 70%): "⚠️ Low Confidence - Please verify this information"
- Response text with clear typography
- Citations section (if available): "Sources: [1] [2] [3]"
- Action buttons:
  - "Challenge Me" button
  - "Simplify This" button
  - "Verify Response" button

**Sidebar (Right):**
- AI Literacy Score widget: "Your AI Literacy: 72/100" with explanation icon
- Recent interactions list (3-5 items)

**Footer:**
- Privacy notice: "No ads. No data monetization."
- Links: About | Privacy | Accessibility

### Key UI Elements
```
[Logo] Trust-Aware AI Learning Platform          [🔆 High Contrast] [Aa Font Size ▼] [?]

┌─────────────────────────────────────────────────────────────────────────┐
│                                                                         │
│  ┌───────────────────────────────────────────────────────────────────┐ │
│  │ Ask your question here...                                         │ │
│  │                                                                   │ │
│  └───────────────────────────────────────────────────────────────────┘ │
│                                                                         │
│  [✓] Enable Challenge Mode    [✓] Simplify Response                   │
│                                                                         │
│  [Ask AI]                                                              │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ AI Response                                    [Confidence: 85% 🟢]     │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│ The mitochondria is the powerhouse of the cell. It produces ATP        │
│ through cellular respiration, converting glucose and oxygen into       │
│ energy that cells can use for various functions.                       │
│                                                                         │
│ Sources: [1] Biology Textbook Ch. 3  [2] Cell Biology Journal          │
│                                                                         │
│ [Challenge Me] [Simplify This] [Verify Response]                       │
└─────────────────────────────────────────────────────────────────────────┘

Sidebar:
┌──────────────────────┐
│ AI Literacy Score    │
│ 72/100 [ℹ️]          │
│ ▓▓▓▓▓▓▓░░░           │
│                      │
│ Recent Interactions  │
│ • Cell biology       │
│ • Photosynthesis     │
│ • DNA structure      │
└──────────────────────┘
```

---

## Screen 2: Challenge Mode Interface (Prototype - Phase 1)

### Layout Description
**Header:**
- Back button: "← Back to Response"
- Challenge type indicator: "Verification Challenge"

**Challenge Card:**
- Challenge title: "Test Your Understanding"
- Problem statement in clear box
- Difficulty indicator: "⭐⭐⭐ (Medium)"
- Attempt counter: "Attempt 1 of 3"

**Answer Input Area:**
- Text area or multiple choice options (depending on challenge type)
- Submit button: "Submit Answer"
- Hint button: "Need a Hint?" (appears after 3 failed attempts)

**Feedback Section (after submission):**
- Correctness indicator: ✓ Correct or ✗ Incorrect
- Explanatory feedback with reasoning
- "Try Another Challenge" button
- "Return to Learning" button

### Key UI Elements
```
[← Back to Response]                    Verification Challenge

┌─────────────────────────────────────────────────────────────────────────┐
│ Test Your Understanding                          Difficulty: ⭐⭐⭐       │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│ Based on the AI's response about mitochondria, which statement is      │
│ most accurate?                                                          │
│                                                                         │
│ ○ Mitochondria only exist in plant cells                              │
│ ○ Mitochondria produce ATP through cellular respiration               │
│ ○ Mitochondria are found in the cell nucleus                          │
│ ○ Mitochondria store genetic information                              │
│                                                                         │
│                                                  Attempt: 1 of 3        │
│                                                                         │
│ [Submit Answer]                                  [Need a Hint?]         │
└─────────────────────────────────────────────────────────────────────────┘

After Submission:
┌─────────────────────────────────────────────────────────────────────────┐
│ ✓ Correct!                                                              │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│ Excellent! You correctly identified that mitochondria produce ATP      │
│ through cellular respiration. This process involves breaking down      │
│ glucose in the presence of oxygen to create energy for the cell.       │
│                                                                         │
│ Your AI Literacy Score increased by 2 points! 🎯                       │
│                                                                         │
│ [Try Another Challenge]  [Return to Learning]                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Screen 3: Simplified Mode View (Prototype - Phase 1)

### Layout Description
Same layout as Main Query Interface but with:
- Simplified language indicator: "📖 Simplified Mode Active"
- Reading level indicator: "Reading Level: Grade 6"
- Side-by-side comparison toggle: "Show Original"
- Simpler vocabulary and shorter sentences in response
- Visual aids or icons where appropriate

### Key UI Elements
```
[Logo] Trust-Aware AI Learning Platform          [📖 Simplified Mode: ON]

┌─────────────────────────────────────────────────────────────────────────┐
│ AI Response (Simplified)                       [Confidence: 85% 🟢]     │
│                                                Reading Level: Grade 6    │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│ 🔋 The mitochondria is like a battery for cells.                       │
│                                                                         │
│ It makes energy (called ATP) that cells need to work. It does this by  │
│ using sugar and oxygen.                                                 │
│                                                                         │
│ Think of it like this: mitochondria take in food and air, then make    │
│ power for the cell to use.                                              │
│                                                                         │
│ [Show Original Version]  [Challenge Me]  [Verify Response]             │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Screen 4: AI Literacy Dashboard (Future - Phase 3)

### Layout Description
**Header:**
- User greeting: "Welcome back, [Student Name]"
- Navigation tabs: Dashboard | Learning History | Settings

**Main Dashboard:**
- AI Literacy Score card (large, prominent)
  - Overall score: 72/100
  - Breakdown by dimensions:
    - Confidence Calibration: 78/100
    - Error Recognition: 65/100
    - Limitation Awareness: 80/100
    - Verification Behavior: 70/100
    - Appropriate Reliance: 68/100
  - Progress chart over time

**Learning Progress Section:**
- Total interactions: 45
- Challenges completed: 23
- Verification rate: 65%
- Trust calibration accuracy: 72%

**Reflective Prompts Section:**
- Latest reflection: "When should you verify AI responses?"
- "Reflect Now" button

**No Gamification Elements:**
- NO points, badges, or leaderboards
- Focus on understanding and growth metrics
- Private, personal progress only

### Key UI Elements
```
Welcome back, Student                    [Dashboard] [Learning History] [Settings]

┌─────────────────────────────────────────────────────────────────────────┐
│ Your AI Literacy Score                                                  │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│         72/100                                                          │
│     ▓▓▓▓▓▓▓▓░░                                                         │
│                                                                         │
│ What this means: You're developing good habits for working with AI.    │
│ You verify responses often and recognize AI limitations.               │
│                                                                         │
│ Breakdown:                                                              │
│ • Confidence Calibration    ▓▓▓▓▓▓▓▓░░  78/100                        │
│ • Error Recognition         ▓▓▓▓▓▓░░░░  65/100                        │
│ • Limitation Awareness      ▓▓▓▓▓▓▓▓░░  80/100                        │
│ • Verification Behavior     ▓▓▓▓▓▓▓░░░  70/100                        │
│ • Appropriate Reliance      ▓▓▓▓▓▓▓░░░  68/100                        │
│                                                                         │
│ [View Progress Over Time]                                              │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ Learning Progress                                                       │
├─────────────────────────────────────────────────────────────────────────┤
│ Total Interactions: 45        Challenges Completed: 23                 │
│ Verification Rate: 65%        Trust Calibration: 72%                   │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ 💭 Reflective Prompt                                                    │
├─────────────────────────────────────────────────────────────────────────┤
│ When should you verify AI responses? Think about situations where      │
│ the AI might be less reliable.                                          │
│                                                                         │
│ [Reflect Now]                                                           │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Screen 5: Educator Dashboard (Future - Phase 3)

### Layout Description
**Header:**
- Role indicator: "Educator View"
- Class/cohort selector dropdown
- Date range filter

**Analytics Overview:**
- Cohort size: 30 students
- Average AI Literacy Score: 68/100
- Trust calibration trend chart
- Challenge engagement rate: 75%

**Student List Table:**
- Columns: Student Name | AI Literacy Score | Last Active | Interactions | Verification Rate
- Privacy controls: "Anonymize Data" toggle
- Export button: "Export Report"

**Insights Section:**
- Top performing areas
- Areas needing attention
- Recommended interventions

### Key UI Elements
```
Educator Dashboard                       [Class: Biology 101 ▼]  [Last 30 Days ▼]

┌─────────────────────────────────────────────────────────────────────────┐
│ Cohort Analytics                                                        │
├─────────────────────────────────────────────────────────────────────────┤
│ Students: 30          Avg AI Literacy: 68/100                          │
│ Challenge Engagement: 75%    Trust Calibration Trend: ↗️ Improving      │
│                                                                         │
│ [View Detailed Trends]                                                  │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ Student Progress                        [✓] Anonymize Data  [Export]   │
├──────────────┬──────────────┬────────────┬──────────────┬──────────────┤
│ Student      │ AI Literacy  │ Last Active│ Interactions │ Verify Rate  │
├──────────────┼──────────────┼────────────┼──────────────┼──────────────┤
│ Student A    │ 75/100       │ 2 hrs ago  │ 52           │ 70%          │
│ Student B    │ 68/100       │ 1 day ago  │ 38           │ 65%          │
│ Student C    │ 82/100       │ 3 hrs ago  │ 67           │ 80%          │
│ ...          │ ...          │ ...        │ ...          │ ...          │
└──────────────┴──────────────┴────────────┴──────────────┴──────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ 📊 Insights                                                             │
├─────────────────────────────────────────────────────────────────────────┤
│ ✓ Strong: Students show good verification behavior                     │
│ ⚠️ Attention: Error recognition scores below average                    │
│ 💡 Recommendation: Introduce challenges focused on identifying AI errors│
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Screen 6: Administrator Dashboard (Future - Phase 3)

### Layout Description
**Header:**
- Role: "Administrator"
- System status indicator: "🟢 All Systems Operational"

**System Health Panel:**
- API response time: 1.2s avg
- Uptime: 99.7%
- Active users: 1,247
- LLM provider status

**LLM Provider Management:**
- Current provider: GROQ GPT-4
- Cost tracking: $234.50 this month
- Request volume chart
- "Configure Providers" button

**Audit Log Viewer:**
- Recent incidents table
- Content filter triggers
- Failed authentication attempts
- "View Full Audit Log" button

**Configuration Panel:**
- Content filter settings
- Rate limiting rules
- Feature flags (enable/disable modules)

### Key UI Elements
```
Administrator Dashboard                           🟢 All Systems Operational

┌─────────────────────────────────────────────────────────────────────────┐
│ System Health                                                           │
├─────────────────────────────────────────────────────────────────────────┤
│ API Response Time: 1.2s avg    Uptime: 99.7%    Active Users: 1,247   │
│                                                                         │
│ LLM Provider Status: 🟢 GROQ (Operational)                           │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ LLM Provider Management                                                 │
├─────────────────────────────────────────────────────────────────────────┤
│ Current Provider: GROQ GPT-4                                          │
│ Monthly Cost: $234.50          Requests: 12,450                        │
│                                                                         │
│ [Configure Providers]  [View Cost Breakdown]                           │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ Recent Audit Events                              [View Full Log]       │
├──────────────┬──────────────────────┬────────────────┬─────────────────┤
│ Timestamp    │ Event Type           │ Severity       │ Details         │
├──────────────┼──────────────────────┼────────────────┼─────────────────┤
│ 10:23 AM     │ Content Filter Hit   │ ⚠️ Warning     │ Blocked harmful │
│ 09:45 AM     │ Rate Limit Exceeded  │ ℹ️ Info        │ IP: 192.168...  │
│ 08:30 AM     │ LLM API Timeout      │ ⚠️ Warning     │ Fallback used   │
└──────────────┴──────────────────────┴────────────────┴─────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ Configuration                                                           │
├─────────────────────────────────────────────────────────────────────────┤
│ [Configure Content Filters]  [Rate Limiting Rules]  [Feature Flags]   │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Screen 7: Mobile App - Voice Interface (Future - Phase 5)

### Layout Description
**Simplified Mobile Layout:**
- Large microphone button (center)
- Voice waveform animation during recording
- Transcribed text display
- Confidence score badge
- Simplified response with audio playback
- Accessibility: Large touch targets, high contrast

### Key UI Elements
```
┌─────────────────────┐
│ 🎤 Voice Mode       │
├─────────────────────┤
│                     │
│                     │
│      [  🎤  ]       │
│   Tap to Speak      │
│                     │
│                     │
├─────────────────────┤
│ You said:           │
│ "What is            │
│  photosynthesis?"   │
├─────────────────────┤
│ Confidence: 88% 🟢  │
│                     │
│ 🔊 [Play Response]  │
│                     │
│ Photosynthesis is   │
│ how plants make     │
│ food using sunlight │
│                     │
│ [Challenge] [More]  │
└─────────────────────┘
```

---

## Screen 8: Accessibility Settings (Prototype - Phase 1)

### Layout Description
**Settings Panel:**
- Visual settings:
  - High contrast mode toggle
  - Font size slider (Small | Medium | Large | Extra Large)
  - Color scheme selector
- Reading settings:
  - Simplification level (Grade 3-12)
  - Auto-simplify toggle
- Navigation settings:
  - Keyboard shortcuts reference
  - Screen reader optimization toggle
- Bandwidth settings:
  - Low connectivity mode toggle
  - Data usage indicator

### Key UI Elements
```
Accessibility Settings                                    [Save] [Cancel]

┌─────────────────────────────────────────────────────────────────────────┐
│ Visual Settings                                                         │
├─────────────────────────────────────────────────────────────────────────┤
│ [✓] High Contrast Mode                                                  │
│                                                                         │
│ Font Size:  [────●────────]  Medium                                    │
│             Small  →  Extra Large                                       │
│                                                                         │
│ Color Scheme: ○ Default  ● High Contrast  ○ Dark Mode                  │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ Reading Settings                                                        │
├─────────────────────────────────────────────────────────────────────────┤
│ Simplification Level: [──────●──]  Grade 6                             │
│                       Grade 3  →  Grade 12                              │
│                                                                         │
│ [✓] Auto-simplify complex responses                                    │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ Navigation Settings                                                     │
├─────────────────────────────────────────────────────────────────────────┤
│ [✓] Optimize for screen readers                                        │
│ [✓] Enable keyboard shortcuts                                          │
│                                                                         │
│ [View Keyboard Shortcuts Reference]                                    │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ Bandwidth Settings                                                      │
├─────────────────────────────────────────────────────────────────────────┤
│ [✓] Low connectivity mode (reduces data usage)                         │
│                                                                         │
│ Current session data usage: 2.3 MB                                     │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Design Principles for All Screens

### Accessibility Requirements:
1. **Keyboard Navigation**: All interactive elements accessible via Tab/Shift+Tab
2. **ARIA Labels**: Proper labeling for screen readers
3. **Color Contrast**: WCAG AA compliance minimum (4.5:1 for text)
4. **Focus Indicators**: Clear visual focus states
5. **Touch Targets**: Minimum 44x44px for mobile

### Typography:
- Primary font: Sans-serif (Arial, Helvetica, or system default)
- Heading sizes: H1 (24px), H2 (20px), H3 (18px)
- Body text: 16px minimum
- Line height: 1.5 for readability

### Color Palette:
- Primary: #2E7D32 (Green - for prototype features)
- Secondary: #1565C0 (Blue - for future features)
- Warning: #F57C00 (Orange - for low confidence)
- Error: #C62828 (Red - for critical warnings)
- Success: #4CAF50 (Green - for correct answers)
- Neutral: #757575 (Gray - for secondary text)

### Confidence Score Color Coding:
- 70-100%: Green (#4CAF50)
- 50-69%: Yellow/Orange (#F57C00)
- 0-49%: Red (#C62828) with warning icon

### No Gamification Elements:
- ❌ NO points system
- ❌ NO badges or achievements
- ❌ NO leaderboards or rankings
- ❌ NO streaks or daily goals
- ✅ YES to reflective metrics
- ✅ YES to personal growth indicators
- ✅ YES to understanding-focused feedback

### Responsive Breakpoints:
- Mobile: 320px - 767px
- Tablet: 768px - 1023px
- Desktop: 1024px+

---

## Implementation Notes for Balsamiq

### To create these wireframes in Balsamiq:

1. **Use these Balsamiq components:**
   - Text Input (for query box)
   - Button (for actions)
   - Label (for text)
   - Icon (for confidence indicators, warnings)
   - Panel/Container (for cards and sections)
   - Data Grid (for tables in educator/admin dashboards)
   - Toggle Switch (for settings)
   - Slider (for font size, reading level)
   - Radio Button Group (for multiple choice challenges)
   - Alert/Callout (for warnings and notifications)

2. **Create separate mockups for:**
   - Main Query Interface (Desktop)
   - Challenge Mode (Desktop)
   - Simplified Mode (Desktop)
   - AI Literacy Dashboard (Desktop)
   - Educator Dashboard (Desktop)
   - Administrator Dashboard (Desktop)
   - Mobile Voice Interface (Mobile)
   - Accessibility Settings (Desktop)

3. **Add annotations for:**
   - Prototype vs Future features
   - Interaction states (hover, focus, active)
   - Accessibility requirements
   - Responsive behavior notes

4. **Link screens together** to show user flow:
   - Main Query → Challenge Mode
   - Main Query → Simplified Mode
   - Dashboard → Settings
   - Educator Dashboard → Student Details

---

## User Flows to Demonstrate

### Flow 1: Basic Query with Confidence Display
1. User enters question
2. System displays response with confidence score
3. If confidence < 70%, warning appears
4. User can verify, challenge, or simplify

### Flow 2: Challenge Mode Engagement
1. User clicks "Challenge Me"
2. System generates contextual challenge
3. User submits answer
4. System provides explanatory feedback
5. AI Literacy Score updates

### Flow 3: Simplification Request
1. User enables "Simplify Response"
2. System adapts language to target reading level
3. User can toggle between original and simplified
4. Accuracy preserved, complexity reduced

### Flow 4: Educator Monitoring (Future)
1. Educator logs in
2. Views cohort analytics dashboard
3. Filters by date range or student group
4. Exports anonymized report
5. Identifies areas needing intervention

---

## Balsamiq Project Structure

```
trust-aware-ai-platform.bmpr
├── 01-main-query-interface.bmml
├── 02-challenge-mode.bmml
├── 03-simplified-mode.bmml
├── 04-ai-literacy-dashboard.bmml
├── 05-educator-dashboard.bmml
├── 06-administrator-dashboard.bmml
├── 07-mobile-voice-interface.bmml
├── 08-accessibility-settings.bmml
├── symbols/
│   ├── header-component.bmml
│   ├── confidence-badge.bmml
│   ├── footer-component.bmml
│   └── sidebar-widget.bmml
└── assets/
    └── notes.txt (design principles and guidelines)
```

---

## Next Steps

1. Import this prompt into Balsamiq Cloud or Desktop
2. Create each screen as a separate mockup
3. Use Balsamiq's linking feature to connect screens
4. Add notes and annotations for developers
5. Export as PDF or interactive prototype for stakeholder review
6. Iterate based on user feedback before development

---

**End of Balsamiq Wireframe Prompt**
