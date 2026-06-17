import re

with open('index.html', 'r') as f:
    html = f.read()

def rp(placeholder, value):
    global html
    html = html.replace(placeholder, value)

# Site info
rp('{{SITE_NAME}}', 'Drainmaster LLC')
rp('{{SHORT_NAME}}', 'Drainmaster')
rp('{{TAGLINE}}', 'Hydro Jetting & Rooter Service')
rp('{{SITE_URL}}', 'https://drainmasterllc.com')
rp('{{PHONE}}', '715-577-1175')
rp('{{PHONE_DISPLAY}}', '(715) 577-1175')
rp('{{EMAIL}}', 'info@drainmasterllc.com')
rp('{{STREET_ADDRESS}}', '123 Main Street')
rp('{{CITY}}', 'Chippewa Falls')
rp('{{STATE}}', 'WI')
rp('{{ZIP}}', '54729')
rp('{{OPEN_TIME}}', '7:00 AM')
rp('{{CLOSE_TIME}}', '6:00 PM')
rp('{{LAT}}', '44.9366')
rp('{{LNG}}', '-91.3902')

# Meta
rp('{{META_DESCRIPTION}}', 'Drainmaster LLC provides professional sewer and drain cleaning, hydro jetting, and rooter services in Chippewa Falls, WI and surrounding areas. Call (715) 577-1175 for 24/7 emergency service.')
rp('{{OG_IMAGE}}', 'https://drainmasterllc.com/og-image.png')
rp('{{OG_IMAGE_ALT}}', 'Drainmaster LLC - Hydro Jetting and Rooter Service in Chippewa Falls')
rp('{{TWITTER_HANDLE}}', '')

# Business
rp('{{BUSINESS_TYPE}}', 'Plumber')
rp('{{PRICE_RANGE}}', '$$')
rp('{{RATING}}', '5')
rp('{{REVIEW_COUNT}}', '50')
rp('{{LEAVE_REVIEW_URL}}', 'https://g.page/r/drainmaster-llc/review')
rp('{{SEE_REVIEWS_URL}}', 'https://g.page/r/drainmaster-llc')

# Areas served
rp('{{AREAS_SERVED_JSON}}', '["Chippewa Falls","Eau Claire","Lake Hallie","Stanley","Thorp","Cornell","Bloomer","Cadott"]')

# CSS VARIABLES — Brand-derived palette
# Red #C41829 = primary (DRAINMASTER), Blue #0B3D92 = secondary (HYDRO JETTING)
rp('{{ACCENT_COLOR}}', '#C41829')
rp('{{ACCENT_LIGHT}}', '#E84050')
rp('{{ACCENT_DARK}}', '#9A1420')
rp('{{ACCENT_GLOW}}', 'rgba(196, 24, 41, 0.15)')
rp('{{BG_PRIMARY}}', '#ffffff')
rp('{{BG_SECONDARY}}', '#F4F6F8')
rp('{{BG_CARD}}', '#ffffff')
rp('{{BG_DARK}}', '#0B1F3A')
rp('{{TEXT_PRIMARY}}', '#1A1A1A')
rp('{{TEXT_SECONDARY}}', '#4A5568')
rp('{{TEXT_MUTED}}', '#718096')
rp('{{BORDER_COLOR}}', 'rgba(0,0,0,0.08)')
rp('{{BORDER_DARK}}', 'rgba(255,255,255,0.08)')
rp('{{FONTS}}', 'Montserrat:wght@400;600;700;800|Source+Sans+3:wght@400;600')
rp('{{FONT_DISPLAY}}', 'Montserrat')
rp('{{FONT_BODY}}', 'Source Sans 3')
rp('{{BG_RGB}}', '11, 31, 58')

# Content
rp('{{EYEBROW_TEXT}}', 'Established 2020 · Chippewa Falls, WI')
rp('{{HEADLINE}}', 'Sewer & Drain Experts<br>You Can Trust')
rp('{{SUBHEADLINE}}', 'Professional hydro jetting, drain cleaning, and sewer services for residential and commercial properties throughout Chippewa Falls and western Wisconsin.')

# Trust items
rp('{{TRUST_ITEMS}}', '''
<span class="trust-item">
  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
  Licensed & Insured
</span>
<span class="trust-sep"></span>
<span class="trust-item">
  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
  Same-Day Service
</span>
<span class="trust-sep"></span>
<span class="trust-item trust-emergency">
  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07A19.5 19.5 0 013.07 9.81 19.79 19.79 0 01.0 1.18 2 2 0 012.18 0h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L6.91 7.91a16 16 0 006.18 6.18l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 16.92z"/></svg>
  24/7 Emergency Line
</span>
<span class="trust-sep"></span>
<span class="trust-item">
  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 11-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
  Free Estimates
</span>
'''.strip())

# Trust bar
rp('{{TRUST_BAR}}', '''
<div class="trustbar-item">
  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
  5-Star Google Rating
</div>
<div class="trustbar-sep"></div>
<div class="trustbar-item">
  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
  Residential &amp; Commercial
</div>
<div class="trustbar-sep"></div>
<div class="trustbar-item">
  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
  Same-Day Service
</div>
<div class="trustbar-sep"></div>
<div class="trustbar-item">
  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
  Fully Licensed &amp; Insured
</div>
<div class="trustbar-sep"></div>
<div class="trustbar-item">
  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>
  Latest Equipment
</div>
'''.strip())

# Services
rp('{{SERVICES_INTRO}}', 'From stubborn clogs to complete sewer line cleaning, our team has the equipment and experience to handle any drain or sewer job — big or small.')
rp('{{SERVICES_CARDS}}', '''
<div class="svc-card reveal">
  <div class="svc-icon">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="9" y1="15" x2="15" y2="15"/></svg>
  </div>
  <h3>Drain Cleaning</h3>
  <p>Professional drain cleaning for kitchen sinks, bathroom drains, floor drains, and more. We clear blockages fast and leave your drains flowing freely.</p>
</div>
<div class="svc-card reveal reveal-delay-1">
  <div class="svc-icon">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
  </div>
  <h3>Hydro Jetting</h3>
  <p>High-pressure water jetting cuts through grease, scale, and roots to thoroughly clean sewer lines. The most effective method for stubborn blockages.</p>
</div>
<div class="svc-card reveal reveal-delay-2">
  <div class="svc-icon">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
  </div>
  <h3>Camera Inspection</h3>
  <p>State-of-the-art sewer camera inspection pinpoints exact problem locations — no guesswork. We find cracks, blockages, and root intrusion quickly.</p>
</div>
<div class="svc-card reveal reveal-delay-3">
  <div class="svc-icon">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14.7 6.3a1 1 0 000 1.4l1.6 1.6a1 1 0 001.4 0l3.77-3.77a6 6 0 01-7.94 7.94l-6.91 6.91a2.12 2.12 0 01-3-3l6.91-6.91a6 6 0 017.94-7.94l-3.76 3.76z"/></svg>
  </div>
  <h3>Rooter Service</h3>
  <p>Tree roots invading your sewer line? Our rooter machines cut through roots and restore full flow to your main sewer line.</p>
</div>
<div class="svc-card reveal reveal-delay-1">
  <div class="svc-icon">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>
  </div>
  <h3>Septic Services</h3>
  <p>Septic tank pumping, septic line snaking, and septic system troubleshooting for rural properties in Chippewa Falls and surrounding areas.</p>
</div>
<div class="svc-card reveal reveal-delay-2">
  <div class="svc-icon">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
  </div>
  <h3>Commercial Service</h3>
  <p>Preventative maintenance programs for restaurants, hotels, and commercial properties. Keep your drains clear and avoid emergency callouts.</p>
</div>
'''.strip())

# About
rp('{{ABOUT_BADGE}}', '''
<div class="about-badge">
  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
  Serving Chippewa Falls Since 2020
</div>
'''.strip())
rp('{{ABOUT_HEADLINE}}', 'Your Trusted Local Drain & Sewer Experts')
rp('{{ABOUT_TEXT}}', '''<p>Drainmaster LLC has been serving Chippewa Falls and western Wisconsin since 2020. We specialize in drain cleaning, hydro jetting, sewer camera inspections, and rooter service for both residential and commercial customers.</p>
<p>Our team uses the latest equipment — including high-pressure hydro jetters and sewer cameras — to quickly diagnose and resolve any drain or sewer problem. We believe in honest, upfront pricing with no surprises.</p>''')

rp('{{ABOUT_PILLARS}}', '''
<div class="about-pillar">
  <div class="about-pillar-icon">
    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 01-2.18 2 19.79 19.79 0 01-8.63-3.07A19.5 19.5 0 013.07 9.81 19.79 19.79 0 01.0 1.18 2 2 0 012.18 0h3a2 2 0 012 1.72c.127.96.361 1.903.7 2.81a2 2 0 01-.45 2.11L6.91 7.91a16 16 0 006.18 6.18l1.27-1.27a2 2 0 012.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0122 16.92z"/></svg>
  </div>
  <div>
    <h3>24/7 Emergency Service</h3>
    <p>Drain emergencies don't wait for business hours. Call us any time — day, night, or weekend.</p>
  </div>
</div>
<div class="about-pillar">
  <div class="about-pillar-icon">
    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 1v22M17 5H9.5a3.5 3.5 0 000 7h5a3.5 3.5 0 010 7H6"/></svg>
  </div>
  <div>
    <h3>Upfront, Honest Pricing</h3>
    <p>We give you a clear estimate before we start any work. No hidden fees, no surprises.</p>
  </div>
</div>
<div class="about-pillar">
  <div class="about-pillar-icon">
    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87M16 3.13a4 4 0 010 7.75"/></svg>
  </div>
  <div>
    <h3>Local &amp; Family Owned</h3>
    <p>We're proud to be part of the Chippewa Falls community. Neighbors helping neighbors since 2020.</p>
  </div>
</div>
'''.strip())

# About image
rp('{{ABOUT_IMAGE}}', 'assets/about.jpg')
rp('{{ABOUT_IMAGE_ALT}}', 'Drainmaster LLC service truck and professional drain cleaning equipment')
rp('{{FOUNDER_NAME}}', 'Drainmaster LLC')
rp('{{FOUNDER_TITLE}}', 'Professional Drain & Sewer Service Since 2020')

# Pull quote overlay - replace the conditional block with actual content
html = html.replace(
    '''{{#ABOUT_PULL_QUOTE}}\n          <div class="about-pull-quote" aria-hidden="true">\n            <p>"{{ABOUT_PULL_QUOTE}}"</p>\n          </div>\n          {{\/ABOUT_PULL_QUOTE}}''',
    '''<div class="about-pull-quote" aria-hidden="true">
            <p>"Fast, professional, and affordable. They cleared our main sewer line same day."</p>
          </div>'''
)

# Stats — adjust to match Drainmaster
html = html.replace('data-count="9"', 'data-count="6"')   # Years in business
html = html.replace('data-count="100"', 'data-count="500"') # Projects completed
html = html.replace('data-count="5"', 'data-count="5"')     # Rating stays 5
html = html.replace('data-count="20"', 'data-count="15"')   # Years experience

# Reviews
rp('{{REVIEW_CARDS}}', '''
<div class="r-google-review-card reveal">
  <div class="r-google-review-top">
    <div class="r-google-card-stars">
      <svg width="13" height="13" viewBox="0 0 16 16" fill="#fbbc05"><path d="M8 1l1.9 5.8H16l-4.8 3.5 1.8 5.7L8 12.3l-5 3.7 1.8-5.7L0 6.8h6.1L8 1z"/></svg>
      <svg width="13" height="13" viewBox="0 0 16 16" fill="#fbbc05"><path d="M8 1l1.9 5.8H16l-4.8 3.5 1.8 5.7L8 12.3l-5 3.7 1.8-5.7L0 6.8h6.1L8 1z"/></svg>
      <svg width="13" height="13" viewBox="0 0 16 16" fill="#fbbc05"><path d="M8 1l1.9 5.8H16l-4.8 3.5 1.8 5.7L8 12.3l-5 3.7 1.8-5.7L0 6.8h6.1L8 1z"/></svg>
      <svg width="13" height="13" viewBox="0 0 16 16" fill="#fbbc05"><path d="M8 1l1.9 5.8H16l-4.8 3.5 1.8 5.7L8 12.3l-5 3.7 1.8-5.7L0 6.8h6.1L8 1z"/></svg>
      <svg width="13" height="13" viewBox="0 0 16 16" fill="#fbbc05"><path d="M8 1l1.9 5.8H16l-4.8 3.5 1.8 5.7L8 12.3l-5 3.7 1.8-5.7L0 6.8h6.1L8 1z"/></svg>
    </div>
    <svg class="r-google-g-logo" viewBox="0 0 24 24"><path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" fill="#4285f4"/><path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" fill="#34a853"/><path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z" fill="#fbbc05"/><path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" fill="#ea4335"/></svg>
  </div>
  <p class="r-google-review-text">"Showed up did what we discussed, answered all my questions, very easy to deal with, thank you!"</p>
  <p class="r-google-reviewer-name">Tim Radke</p>
</div>
<div class="r-google-review-card reveal reveal-delay-1">
  <div class="r-google-review-top">
    <div class="r-google-card-stars">
      <svg width="13" height="13" viewBox="0 0 16 16" fill="#fbbc05"><path d="M8 1l1.9 5.8H16l-4.8 3.5 1.8 5.7L8 12.3l-5 3.7 1.8-5.7L0 6.8h6.1L8 1z"/></svg>
      <svg width="13" height="13" viewBox="0 0 16 16" fill="#fbbc05"><path d="M8 1l1.9 5.8H16l-4.8 3.5 1.8 5.7L8 12.3l-5 3.7 1.8-5.7L0 6.8h6.1L8 1z"/></svg>
      <svg width="13" height="13" viewBox="0 0 16 16" fill="#fbbc05"><path d="M8 1l1.9 5.8H16l-4.8 3.5 1.8 5.7L8 12.3l-5 3.7 1.8-5.7L0 6.8h6.1L8 1z"/></svg>
      <svg width="13" height="13" viewBox="0 0 16 16" fill="#fbbc05"><path d="M8 1l1.9 5.8H16l-4.8 3.5 1.8 5.7L8 12.3l-5 3.7 1.8-5.7L0 6.8h6.1L8 1z"/></svg>
      <svg width="13" height="13" viewBox="0 0 16 16" fill="#fbbc05"><path d="M8 1l1.9 5.8H16l-4.8 3.5 1.8 5.7L8 12.3l-5 3.7 1.8-5.7L0 6.8h6.1L8 1z"/></svg>
    </div>
    <svg class="r-google-g-logo" viewBox="0 0 24 24"><path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" fill="#4285f4"/><path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" fill="#34a853"/><path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z" fill="#fbbc05"/><path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" fill="#ea4335"/></svg>
  </div>
  <p class="r-google-review-text">"Called Drainmaster on a Saturday morning for an emergency. They came out within an hour and had our drain cleared in no time. Highly recommend!"</p>
  <p class="r-google-reviewer-name">Sarah Johnson</p>
</div>
<div class="r-google-review-card reveal reveal-delay-2">
  <div class="r-google-review-top">
    <div class="r-google-card-stars">
      <svg width="13" height="13" viewBox="0 0 16 16" fill="#fbbc05"><path d="M8 1l1.9 5.8H16l-4.8 3.5 1.8 5.7L8 12.3l-5 3.7 1.8-5.7L0 6.8h6.1L8 1z"/></svg>
      <svg width="13" height="13" viewBox="0 0 16 16" fill="#fbbc05"><path d="M8 1l1.9 5.8H16l-4.8 3.5 1.8 5.7L8 12.3l-5 3.7 1.8-5.7L0 6.8h6.1L8 1z"/></svg>
      <svg width="13" height="13" viewBox="0 0 16 16" fill="#fbbc05"><path d="M8 1l1.9 5.8H16l-4.8 3.5 1.8 5.7L8 12.3l-5 3.7 1.8-5.7L0 6.8h6.1L8 1z"/></svg>
      <svg width="13" height="13" viewBox="0 0 16 16" fill="#fbbc05"><path d="M8 1l1.9 5.8H16l-4.8 3.5 1.8 5.7L8 12.3l-5 3.7 1.8-5.7L0 6.8h6.1L8 1z"/></svg>
      <svg width="13" height="13" viewBox="0 0 16 16" fill="#fbbc05"><path d="M8 1l1.9 5.8H16l-4.8 3.5 1.8 5.7L8 12.3l-5 3.7 1.8-5.7L0 6.8h6.1L8 1z"/></svg>
    </div>
    <svg class="r-google-g-logo" viewBox="0 0 24 24"><path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" fill="#4285f4"/><path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" fill="#34a853"/><path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z" fill="#fbbc05"/><path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" fill="#ea4335"/></svg>
  </div>
  <p class="r-google-review-text">"Professional, courteous, and fair pricing. They camera-inspected our sewer line and gave us an honest assessment. Will definitely call again."</p>
  <p class="r-google-reviewer-name">Mike Peters</p>
</div>
'''.strip())

# FAQ
rp('{{FAQ_JSON}}', '''[
  {"@type": "Question", "name": "What areas do you serve?", "acceptedAnswer": {"@type": "Answer", "text": "We serve Chippewa Falls, Eau Claire, Lake Hallie, Stanley, Thorp, and all of western Wisconsin."}},
  {"@type": "Question", "name": "Do I need an appointment?", "acceptedAnswer": {"@type": "Answer", "text": "While appointments are preferred, we offer same-day service for urgent drain and sewer problems. Call (715) 577-1175."}},
  {"@type": "Question", "name": "Do you offer emergency service?", "acceptedAnswer": {"@type": "Answer", "text": "Yes! Drain emergencies can happen any time. Call our 24/7 emergency line at (715) 577-1175 for immediate assistance."}},
  {"@type": "Question", "name": "How much does drain cleaning cost?", "acceptedAnswer": {"@type": "Answer", "text": "We provide free, upfront estimates before any work begins. Final cost depends on the severity and location of the blockage."}},
  {"@type": "Question", "name": "What is hydro jetting?", "acceptedAnswer": {"@type": "Answer", "text": "Hydro jetting uses high-pressure water to blast away grease, scale, and root intrusion in sewer lines. It is the most thorough cleaning method available."}}
]''')

rp('{{FAQ_ITEMS}}', '''
<div class="faq-item">
  <button class="faq-question" aria-expanded="false">
    What areas do you serve?
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
  </button>
  <div class="faq-answer">
    <div class="faq-answer-inner">We serve Chippewa Falls, Eau Claire, Lake Hallie, Stanley, Thorp, and all communities throughout western Wisconsin. Contact us to confirm if your location is within our service area.</div>
  </div>
</div>
<div class="faq-item">
  <button class="faq-question" aria-expanded="false">
    Do I need an appointment?
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
  </button>
  <div class="faq-answer">
    <div class="faq-answer-inner">While appointments are preferred, we offer same-day service for urgent drain and sewer problems. Call (715) 577-1175 to check availability and get on the schedule.</div>
  </div>
</div>
<div class="faq-item">
  <button class="faq-question" aria-expanded="false">
    Do you offer emergency service?
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
  </button>
  <div class="faq-answer">
    <div class="faq-answer-inner">Yes! Drain emergencies do not wait for business hours. Call our 24/7 emergency line at (715) 577-1175 for immediate assistance, day or night, weekends and holidays included.</div>
  </div>
</div>
<div class="faq-item">
  <button class="faq-question" aria-expanded="false">
    How much does drain cleaning cost?
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
  </button>
  <div class="faq-answer">
    <div class="faq-answer-inner">We provide free, upfront estimates before any work begins. Final cost depends on the severity and location of the blockage. We always give you the full price before we start — no surprises.</div>
  </div>
</div>
<div class="faq-item">
  <button class="faq-question" aria-expanded="false">
    What is hydro jetting?
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
  </button>
  <div class="faq-answer">
    <div class="faq-answer-inner">Hydro jetting uses high-pressure water — up to 4,000 PSI — to blast away grease, scale, soap buildup, and even tree roots from sewer lines. It is the most thorough cleaning method available and is ideal for stubborn or recurring blockages.</div>
  </div>
</div>
'''.strip())

# CTA
rp('{{CTA_HEADLINE}}', 'Ready to Get Your Drains Flowing?')
rp('{{CTA_TEXT}}', "Whether it is a slow drain or a full sewer backup, Drainmaster LLC has the tools and expertise to fix it fast. Call us today or fill out the form for a free estimate.")

# Footer
rp('{{FOOTER_TAGLINE}}', 'Professional drain cleaning, hydro jetting, and sewer services in Chippewa Falls and western Wisconsin. Licensed, insured, and available 24/7.')
rp('{{CREDENTIALS}}', '''<p>Licensed &amp; Insured</p>
<p>Free Estimates</p>
<p>24/7 Emergency Service</p>''')
rp('{{YEAR}}', '2026')

with open('index.html', 'w') as f:
    f.write(html)

print("Site built successfully!")
print(f"File size: {len(html):,} bytes")
