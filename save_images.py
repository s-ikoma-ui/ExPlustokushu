"""
Run this script once to verify image files exist.
Images should be placed in the same folder as index.html with these names:
  - ExPlus_series_ガードフェンス_ベースプレートあり.png  (slide 2: guard fence with base)
  - ExPlus_series_スタイルポール_ベースプレートあり.png  (slide 3: 3 style poles with base)
"""
import os
folder = os.path.dirname(os.path.abspath(__file__))
for name in [
    'ExPlus_series_ガードフェンス_ベースプレートあり.png',
    'ExPlus_series_スタイルポール_ベースプレートあり.png',
]:
    path = os.path.join(folder, name)
    print('EXISTS' if os.path.exists(path) else 'MISSING', path)
