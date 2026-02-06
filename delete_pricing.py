import re

with open('index.html', 'r') as f:
    content = f.read()

# Remove the pricing CSS section
css_pattern = r'/\* Pricing Grid Styles \*/.*?/\* End Pricing Grid Styles \*/'
content = re.sub(css_pattern, '', content, flags=re.DOTALL)

# Remove the pricing cards container (from <!-- Card 1 to the closing </div> of pricing-cards-container)
# The pattern: <div class="pricing-cards-container">...both cards...</div>
cards_pattern = r'<div class="pricing-cards-container"><!-- Card 1:.*?</div></div></div>'
content = re.sub(cards_pattern, '', content, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(content)

print('Both pricing cards and CSS deleted successfully!')
