# Cinematic Sites — Agent Skill

**Version:** 1.0
**Purpose:** Transform websites into cinematic, interactive experiences
**Pipeline:** 4 steps (Brand → Scene → Build → Deploy)
**Output:** Live website on Vercel

---

## STEP 1: BRAND ANALYSIS

**Goal:** Extract brand identity from existing website

**Instructions:**
1. Fetch the current website (HTML/visual)
2. Extract:
   - Primary color palette (3-5 colors)
   - Typography (fonts, sizes, weights)
   - Brand story/mission
   - Industry/niche
   - Tone of voice
   - Key products/services
   - Tagline/headline
3. Create HTML brand card showing:
   - Color swatches
   - Typography samples
   - Brand narrative
   - Industry positioning
   - Suggested hero animation direction
4. Present for user approval before continuing

**Tools Needed:**
- Web scraping (read HTML)
- Color extraction (analyze design)
- Text analysis (extract brand voice)

**Pause Point:** User approves brand card

---

## STEP 2: SCENE GENERATION

**Goal:** Create cinematic hero videos

**Instructions:**
1. Suggest 3 hero scene concepts based on brand
   - Each concept: emoji + description
   - Focus on product-in-action
   - Consider brand aesthetic
2. Let user select 1-2 concepts OR refine
3. Generate images using Nano Banana (Google):
   - Model: `imagegeneration@006` or `imagegeneration-pro`
   - Prompt: Cinematic, well-lit, professional photography
   - Resolution: 1920x1080
4. Generate videos using Cling (Wavespeed API):
   - Model: `cling-v3-image-to-video`
   - Animation: Cinematic movement, camera work
   - Duration: 5-8 seconds
5. Present videos in generations tab
6. User selects final video for website

**API Setup:**
```
Google Nano Banana:
- Endpoint: https://generativelanguage.googleapis.com/v1beta/models/
- Method: POST /generateImages
- Auth: API key (Google $300 free credit)
- Cost: Very cheap (~$0.01-0.05 per image)

Wavespeed Cling:
- Endpoint: https://api.wavespeed.io/v1/models/cling-v3/generate
- Method: POST /generate
- Auth: API key
- Cost: Pay-per-use, reasonable rates
```

**Pause Point:** User selects final video

---

## STEP 3: WEBSITE BUILD

**Goal:** Create full responsive HTML website

**Instructions:**
1. Create HTML structure:
   - Hero section with video scroll animation
   - Brand colors from Step 1
   - Typography from Step 1
   - Responsive grid layout
   - Mobile-first approach

2. Extract content from original website:
   - Headings, copy
   - Product descriptions
   - Contact info, hours
   - Menu/services
   - Address, phone

3. Add cinematic modules:
   - Video scroll frame mapping
   - Text reveal effects
   - Accordion sliders (for menus)
   - Image trails
   - Flip cards
   - Kinetic typography
   - Smooth scrolling
   - Interactive buttons

4. Implement interactive sections:
   - About/story (with animations)
   - Services/products (accordion or cards)
   - Menu (if restaurant)
   - Contact form
   - Testimonials (flip cards)
   - Call-to-action sections

5. Ensure:
   - Fully responsive (mobile, tablet, desktop)
   - Fast load time (<3s)
   - Accessibility (alt text, contrast, labels)
   - SEO basics (meta tags, structure)
   - Forms functional (if applicable)

**Cinematic Modules Available:**
- Text reveal (fade, slide, typewriter)
- Video scroll (frame-based animation)
- Image trails (hover effect)
- Flip cards (3D reveal)
- Accordion slider (expandable)
- Kinetic text (animated typography)
- Glitch effects
- Smooth scroll animations
- Hover effects
- Interactive buttons
- Animated counters
- Gradient animations
- SVG animations

**Code Structure:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[Brand Name]</title>
  <style>
    /* Color system from brand analysis */
    :root {
      --primary: [color1];
      --secondary: [color2];
      --accent: [color3];
      --text: [color4];
      --bg: [color5];
    }
    
    /* Cinematic animations */
    @keyframes videoScroll { ... }
    @keyframes textReveal { ... }
    @keyframes imageTrail { ... }
    
    /* Responsive design */
    @media (max-width: 768px) { ... }
  </style>
</head>
<body>
  <!-- Hero with video scroll -->
  <section class="hero cinematic-hero">
    <video src="[hero-video]"></video>
    <h1 class="text-reveal">[Brand Headline]</h1>
    <button class="cta">[Call to Action]</button>
  </section>
  
  <!-- Brand story -->
  <section class="story">
    <h2>Our Story</h2>
    <p class="kinetic-text">[Brand narrative from Step 1]</p>
  </section>
  
  <!-- Services/Products -->
  <section class="services">
    <div class="accordion-slider">
      <!-- Cinematic modules here -->
    </div>
  </section>
  
  <!-- Contact/CTA -->
  <section class="cta-final">
    <!-- High-contrast call to action -->
  </section>
  
  <script>
    // Scroll-based video frame animation
    // Cinematic module interactions
    // Smooth scroll effects
  </script>
</body>
</html>
```

**Pause Point:** User can request modifications

---

## STEP 4: DEPLOY

**Goal:** Make website live immediately

**Instructions:**
1. Create Vercel project:
   - Connect GitHub or upload files
   - Auto-build & deploy
   - Generate live URL
   
2. Optimize:
   - Image compression
   - CSS minification
   - JS bundling
   - CDN distribution

3. Setup:
   - Custom domain (optional)
   - SSL certificate (automatic)
   - Analytics
   - Form handling (if needed)

4. Share:
   - Live URL to client
   - Demo link
   - Ready for feedback

**Vercel Setup:**
```bash
# Install Vercel CLI
npm install -g vercel

# Deploy
vercel --prod

# Result: https://[project-name].vercel.app (live!)
```

**No cost:** Vercel free tier covers this perfectly

---

## 🎬 FULL PIPELINE SUMMARY

```
INPUT:  Existing website URL
  ↓
STEP 1: Brand Analysis (colors, fonts, story)
  → User approves brand card
  ↓
STEP 2: Scene Generation (hero video)
  → Generate images (Nano Banana)
  → Animate to video (Cling)
  → User selects final video
  ↓
STEP 3: Website Build (full HTML/CSS/JS)
  → Extract content
  → Add cinematic modules
  → Responsive design
  → User can request changes
  ↓
STEP 4: Deploy (Vercel)
  → Live URL
  → Fully functional
  → Ready for clients
  ↓
OUTPUT: Professional cinematic website
```

---

## 💡 TIPS FOR SUCCESS

**Image Generation (Nano Banana):**
- Be specific with prompts (cinematic, professional, well-lit)
- Request high resolution (1920x1080+)
- Generate multiple variations (pick best)
- Cost: ~$300 Google credit = 1000+ images

**Video Generation (Cling):**
- Describe camera movement (zoom, pan, orbit)
- Specify duration (5-8 seconds ideal)
- Keep prompts clear and direct
- Test multiple prompts (more volume = better odds)

**Website Design:**
- Keep scroll interactions smooth
- Don't overcomplicate animations
- Mobile experience is critical
- Fast load times = better conversion
- Clear CTAs throughout

**Deployment:**
- Test all forms before deploy
- Check mobile responsiveness
- Verify all links work
- Set up analytics
- Get client feedback before final push

---

## 🚀 NEXT STEPS (Street Rulz Version)

When running this for Street Rulz:

1. **Input:** Current Street Rulz website
2. **Step 1:** Extract brand (football, premium, community-focused)
3. **Step 2:** Hero video ideas:
   - Live game footage (animated)
   - Ball scoring slow-motion
   - Team celebration (cinematic)
4. **Step 3:** Build with:
   - Video scroll hero
   - League table (animated)
   - Testimonials (flip cards)
   - Pricing (interactive)
   - Booking flow (smooth)
5. **Step 4:** Deploy to Vercel
6. **Result:** Premium cinematic site (vs. current static redesign)

---

**STATUS:** Agent skill ready. Execute when ready. 🚀
