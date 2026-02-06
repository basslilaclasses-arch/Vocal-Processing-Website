import re

# Read the file
with open('index.html', 'r') as f:
    content = f.read()

# Pattern to find all pricing CSS sections
pattern = r'/\* Pricing Grid Styles \*/.*?/\* End Pricing Grid Styles \*/'

# Remove all existing pricing CSS sections
content = re.sub(pattern, '', content, flags=re.DOTALL)

# New clean CSS
new_css = """/* Pricing Grid Styles */
.section_success .padding-global {
  padding-left: 1.5rem !important;
  padding-right: 1.5rem !important;
}

.pricing-cards-container {
  display: flex;
  flex-direction: row;
  gap: 2rem;
  justify-content: center;
  align-items: stretch;
  flex-wrap: nowrap;
  max-width: 1100px;
  margin: 0 auto;
  padding: 0 1rem;
}

.pricing-card-wrapper {
  position: relative;
  flex: 0 1 480px;
  min-width: 320px;
  max-width: 480px;
}

.pricing-card-wrapper > .glowing-card-lc {
  height: 100%;
}

.pricing-card-wrapper.bundle-card {
  border: 3px solid transparent;
  border-radius: clamp(19px, 3vw, 27px);
  background: linear-gradient(135deg, #1a1a2e, #16213e, #0f0f23) padding-box,
              linear-gradient(135deg, #FFD700, #FFA500, #FF8C00, #FFD700) border-box;
  animation: borderGlow 3s ease-in-out infinite;
}

@keyframes borderGlow {
  0%, 100% { box-shadow: 0 0 20px rgba(255, 215, 0, 0.3), 0 0 40px rgba(255, 165, 0, 0.2); }
  50% { box-shadow: 0 0 30px rgba(255, 215, 0, 0.5), 0 0 60px rgba(255, 165, 0, 0.3); }
}

.sale-badge {
  position: absolute;
  top: -12px;
  right: 20px;
  background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%);
  color: #000;
  padding: 8px 16px;
  border-radius: 20px;
  font-size: 0.85rem;
  font-weight: 800;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  box-shadow: 0 4px 15px rgba(255, 215, 0, 0.4);
  z-index: 10;
  animation: badgePulse 2s ease-in-out infinite;
}

@keyframes badgePulse {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.05); }
}

.bundle-enroll-btn {
  display: block;
  width: 100%;
  background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%);
  color: #000;
  text-align: center;
  padding: clamp(14px, 4vw, 20px) clamp(24px, 6vw, 48px);
  border-radius: clamp(8px, 2vw, 12px);
  font-weight: 700;
  font-size: clamp(14px, 4vw, 18px);
  text-decoration: none;
  transition: transform 0.2s, box-shadow 0.2s;
  box-shadow: 0 4px 20px rgba(255, 215, 0, 0.3);
  box-sizing: border-box;
}

.bundle-enroll-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 25px rgba(255, 215, 0, 0.5);
}

@media (max-width: 900px) {
  .pricing-cards-container {
    flex-direction: column;
    align-items: center;
    gap: 2.5rem;
  }
  
  .pricing-card-wrapper {
    width: 100%;
    max-width: 450px;
    flex: none;
  }
}

@media (max-width: 479px) {
  .pricing-cards-container {
    gap: 2rem;
    padding: 0 0.5rem;
  }
  
  .pricing-card-wrapper {
    min-width: unset;
    max-width: 100%;
  }
  
  .sale-badge {
    top: -10px;
    right: 15px;
    padding: 6px 12px;
    font-size: 0.75rem;
  }
}
/* End Pricing Grid Styles */"""

# Find where to insert (after Audio Section Styles)
insert_marker = '/* End Audio Section Styles */'
insert_point = content.find(insert_marker)
if insert_point != -1:
    insert_point = insert_point + len(insert_marker)
    # Find the newline after the marker
    newline_pos = content.find('\n', insert_point)
    if newline_pos != -1:
        insert_point = newline_pos + 1
    content = content[:insert_point] + new_css + '\n' + content[insert_point:]

# Write back
with open('index.html', 'w') as f:
    f.write(content)

print('CSS cleaned and rewritten successfully!')
