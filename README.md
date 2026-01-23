# Story Hero Academy Website

This is a locally-hosted version of the Story Hero Academy website, downloaded and configured for offline use.

## Quick Start

Run the website locally using one of these methods:

### Method 1: Using npm/npx (Recommended)
```bash
# From the project root directory
npm start
# OR
npx serve -l 3000
```
Then open: http://localhost:3000

### Method 2: Using Python (if Node.js is not available)
```bash
# Python 3
python3 -m http.server 3000

# Python 2
python -m SimpleHTTPServer 3000
```
Then open: http://localhost:3000

### Method 3: Using PHP
```bash
php -S localhost:3000
```
Then open: http://localhost:3000

## Project Structure

```
├── index.html              # Main homepage
├── waitlist.html           # Waitlist page
├── legal/                  # Legal pages
│   ├── cookie-policy.html
│   ├── legal-notice.html
│   ├── privacy-policy.html
│   └── terms-conditions.html
├── assets/
│   ├── css/               # Stylesheets
│   ├── js/                # JavaScript files
│   ├── images/            # All images (SVG, PNG, WEBP, AVIF, etc.)
│   ├── videos/            # Video files
│   ├── fonts/             # Web fonts
│   └── other/             # Other assets (RIV files, etc.)
├── package.json           # npm configuration
└── README.md              # This file
```

## Features

- ✅ Fully offline - no external CDN dependencies
- ✅ All images, videos, CSS, and JS downloaded locally
- ✅ Navigation between pages works correctly
- ✅ Responsive design preserved
- ✅ Animations and interactions preserved (Webflow, GSAP, Lenis, etc.)

## Notes

- This website was originally built with Webflow
- Some external services (forms, analytics) may not work offline
- Vimeo embedded videos require internet connection to play
