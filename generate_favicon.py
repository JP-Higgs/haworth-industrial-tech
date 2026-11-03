from PIL import Image, ImageDraw, ImageFont
import os

os.makedirs('/home/jp/clients/Haworth Industrial Technologies/.worktrees/t_5a961c7d/public/assets/images', exist_ok=True)

# Create SVG favicon directly without svgwrite
svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">
  <rect width="512" height="512" fill="#ffffff" rx="96"/>
  <text x="256" y="380" font-family="Impact, Arial Black, sans-serif" font-weight="900" font-size="380" fill="#000000" text-anchor="middle">H</text>
</svg>'''

svg_path = '/home/jp/clients/Haworth Industrial Technologies/.worktrees/t_5a961c7d/public/assets/images/favicon.svg'
with open(svg_path, 'w') as f:
    f.write(svg_content)
print("Saved SVG favicon to:", svg_path)

# Create PNG and ICO using Pillow
img = Image.new('RGB', (512, 512), color='white')
d = ImageDraw.Draw(img)
try:
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 360)
except Exception:
    font = ImageFont.load_default()

bbox = d.textbbox((0, 0), "H", font=font)
w = bbox[2] - bbox[0]
h = bbox[3] - bbox[1]
x = (512 - w) / 2 - bbox[0]
y = (512 - h) / 2 - bbox[1]

d.text((x, y), "H", fill="black", font=font)

png_path = '/home/jp/clients/Haworth Industrial Technologies/.worktrees/t_5a961c7d/public/assets/images/favicon.png'
ico_path = '/home/jp/clients/Haworth Industrial Technologies/.worktrees/t_5a961c7d/public/favicon.ico'

img.save(png_path)
img.resize((32, 32), Image.Resampling.LANCZOS).save(ico_path, format='ICO')
print("Saved PNG and ICO favicons successfully.")
