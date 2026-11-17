import re

filepath = '/Users/takasho2011/Desktop/test/\u300022\u300bExPlus\u30fbExLight\u7279\u96c6/index.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Find the product-p06 image div and replace it
old = (
    '<div class="product__image" aria-label="\u30b9\u30bf\u30a4\u30eb\u30dd\u30fc'
    '\u30eb\u30fb\u30ac\u30fc\u30c9\u30d5\u30a7\u30f3\u30b9\u7528\u30d9\u30fc\u30b9'
    '\u30d7\u30ec\u30fc\u30c8\u306e\u5546\u54c1\u753b\u50cf"><div class="product__image-track">'
    '<img src="./\u30b9\u30bf\u30a4\u30eb\u30dd\u30fc\u30eb\u30fb\u30ac\u30fc\u30c9'
    '\u30d5\u30a7\u30f3\u30b9\u7528\u30d9\u30fc\u30b9\u30d7\u30ec\u30fc\u30c8.jpg" '
    'alt="\u30b9\u30bf\u30a4\u30eb\u30dd\u30fc\u30eb\u30fb\u30ac\u30fc\u30c9\u30d5'
    '\u30a7\u30f3\u30b9\u7528\u30d9\u30fc\u30b9\u30d7\u30ec\u30fc\u30c8" loading="lazy">'
    '</div></div>'
)

new = (
    '<div class="product__image" aria-label="\u30b9\u30bf\u30a4\u30eb\u30dd\u30fc'
    '\u30eb\u30fb\u30ac\u30fc\u30c9\u30d5\u30a7\u30f3\u30b9\u7528\u30d9\u30fc\u30b9'
    '\u30d7\u30ec\u30fc\u30c8\u306e\u5546\u54c1\u753b\u50cf">\n'
    '              <div class="product__image-track">'
    '<img src="./\u30b9\u30bf\u30a4\u30eb\u30dd\u30fc\u30eb\u30fb\u30ac\u30fc\u30c9'
    '\u30d5\u30a7\u30f3\u30b9\u7528\u30d9\u30fc\u30b9\u30d7\u30ec\u30fc\u30c8.jpg" '
    'alt="\u30b9\u30bf\u30a4\u30eb\u30dd\u30fc\u30eb\u30fb\u30ac\u30fc\u30c9\u30d5'
    '\u30a7\u30f3\u30b9\u7528\u30d9\u30fc\u30b9\u30d7\u30ec\u30fc\u30c8" loading="lazy">'
    '<img src="./ExPlus_series_\u30ac\u30fc\u30c9\u30d5\u30a7\u30f3\u30b9_\u30d9\u30fc'
    '\u30b9\u30d7\u30ec\u30fc\u30c8\u3042\u308a.png" '
    'alt="\u30d9\u30fc\u30b9\u30d7\u30ec\u30fc\u30c8\u3092\u53d6\u308a\u4ed8\u3051'
    '\u305f\u30ac\u30fc\u30c9\u30d5\u30a7\u30f3\u30b9" loading="lazy">'
    '<img src="./ExPlus_series_\u30b9\u30bf\u30a4\u30eb\u30dd\u30fc\u30eb_\u30d9\u30fc'
    '\u30b9\u30d7\u30ec\u30fc\u30c8\u3042\u308a.png" '
    'alt="\u30d9\u30fc\u30b9\u30d7\u30ec\u30fc\u30c8\u3092\u53d6\u308a\u4ed8\u3051'
    '\u305f\u30b9\u30bf\u30a4\u30eb\u30dd\u30fc\u30eb" loading="lazy">'
    '</div>\n'
    '              <button class="product__image-control product__image-control--prev" '
    'type="button" aria-label="\u524d\u306e\u753b\u50cf" disabled>\u2039</button>'
    '<button class="product__image-control product__image-control--next" '
    'type="button" aria-label="\u6b21\u306e\u753b\u50cf">\u203a</button>'
    '<span class="product__image-count" aria-live="polite">1 / 3</span>\n'
    '            </div>'
)

if old in content:
    new_content = content.replace(old, new)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('SUCCESS: replaced product-p06 image block')
else:
    print('NOT FOUND - searching for partial match...')
    # Try to find the aria-label portion
    marker = '\u30b9\u30bf\u30a4\u30eb\u30dd\u30fc\u30eb\u30fb\u30ac\u30fc\u30c9\u30d5\u30a7\u30f3\u30b9\u7528\u30d9\u30fc\u30b9\u30d7\u30ec\u30fc\u30c8\u306e\u5546\u54c1\u753b\u50cf'
    idx = content.find(marker)
    if idx >= 0:
        print('Marker found at index', idx)
        print(repr(content[idx-30:idx+300]))
    else:
        print('Marker also not found')
