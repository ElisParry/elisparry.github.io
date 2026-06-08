import os
import shutil
import tempfile
from PIL import Image

ROOT = os.path.dirname(__file__)
IMAGE_DIRS = [
    os.path.join(ROOT, 'assets', 'images'),
    os.path.join(ROOT, 'assets', 'images_dithered'),
]
EXTS = {'.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG'}
summary = []


def optimize_image(path):
    try:
        with Image.open(path) as img:
            img_format = img.format
            orig_size = os.path.getsize(path)
            with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(path)[1]) as tmp:
                tmp_path = tmp.name
            try:
                if img_format in ('JPEG', 'MPO'):
                    img = img.convert('RGB')
                    img.save(tmp_path, 'JPEG', quality=75, optimize=True, progressive=True)
                elif img_format == 'PNG':
                    img.save(tmp_path, 'PNG', optimize=True)
                elif img_format == 'AVIF':
                    img = img.convert('RGBA')
                    img.save(tmp_path, 'PNG', optimize=True)
                else:
                    os.unlink(tmp_path)
                    return None
                new_size = os.path.getsize(tmp_path)
                if new_size < orig_size:
                    shutil.move(tmp_path, path)
                    saved = orig_size - new_size
                    percent = saved / orig_size * 100 if orig_size else 0
                    return orig_size, new_size, saved, percent
                os.unlink(tmp_path)
                return orig_size, orig_size, 0, 0.0
            except Exception:
                os.unlink(tmp_path)
                raise
    except Exception as exc:
        return f'ERROR: {exc}'

for image_dir in IMAGE_DIRS:
    if not os.path.isdir(image_dir):
        continue
    for root, _, files in os.walk(image_dir):
        for fname in files:
            if os.path.splitext(fname)[1] in EXTS:
                path = os.path.join(root, fname)
                result = optimize_image(path)
                if isinstance(result, tuple):
                    summary.append((path,) + result)
                else:
                    summary.append((path, result, None, None, None))

summary = sorted(summary, key=lambda item: item[3] if isinstance(item[3], (int, float)) else 0, reverse=True)
for item in summary:
    if item[2] is None:
        print(f'{item[0]}: {item[1]}')
    elif item[2] == item[1]:
        print(f'{item[0]}: no savings')
    else:
        print(f'{item[0]}: {item[1]} -> {item[2]} ({item[4]:.1f}% saved)')

print('\nTotal images checked:', len(summary))
print('Compression complete. Only smaller files were kept.')
