from PIL import Image, ImageDraw, ImageFont
import os

# --- CONFIGURATION ---
INPUT_FOLDER = "input_images"
OUTPUT_FOLDER = "output_images"
WATERMARK_TEXT = "© RIYAZ357 PHOTOGRAPHY"  # Default text
OPACITY = 128  # 0 (Invisible) to 255 (Solid)

# Ensure folders exist
if not os.path.exists(INPUT_FOLDER):
    os.makedirs(INPUT_FOLDER)
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

def apply_watermark(filename, text):
    """Opens an image, adds a watermark, and saves it."""
    input_path = os.path.join(INPUT_FOLDER, filename)
    output_path = os.path.join(OUTPUT_FOLDER, filename)

    try:
        # 1. Open Image & Convert to RGBA (Red, Green, Blue, Alpha/Transparency)
        original = Image.open(input_path).convert("RGBA")
        
        # 2. Create a separate transparent layer for text
        # Make a blank image the same size as the original
        txt_layer = Image.new("RGBA", original.size, (255, 255, 255, 0))
        
        # 3. Initialize Drawing Context
        draw = ImageDraw.Draw(txt_layer)
        
        # 4. Load Font (Try to load Arial, fallback to default if missing)
        try:
            # Scale font size based on image width (5% of width)
            font_size = int(original.width / 20)
            font = ImageFont.truetype("arial.ttf", font_size)
        except IOError:
            font = ImageFont.load_default() # Fallback (very small)

        # 5. Calculate Position (Bottom Right)
        # Get bounding box of text to know its width/height
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        # X = Image Width - Text Width - Padding
        x = original.width - text_width - 20
        y = original.height - text_height - 20

        # 6. Draw Text on the Transparent Layer
        # (255, 255, 255, OPACITY) -> White text with transparency
        draw.text((x, y), text, font=font, fill=(255, 255, 255, OPACITY))

        # 7. Merge Layers (Composite)
        watermarked = Image.alpha_composite(original, txt_layer)

        # 8. Save (Convert back to RGB to save as JPG)
        watermarked = watermarked.convert("RGB")
        watermarked.save(output_path, "JPEG")
        
        print(f"✅ Processed: {filename}")

    except Exception as e:
        print(f"❌ Error processing {filename}: {e}")

# --- MAIN LOOP ---
if __name__ == "__main__":
    print("--- 🖼️ Batch Watermarker ---")
    
    # Optional: Ask user for custom text
    user_text = input(f"Enter watermark text (Press Enter for '{WATERMARK_TEXT}'): ")
    if user_text.strip():
        WATERMARK_TEXT = user_text

    files = [f for f in os.listdir(INPUT_FOLDER) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    if not files:
        print(f"⚠️ No images found in '{INPUT_FOLDER}'. Please add some photos!")
    else:
        print(f"🚀 Starting process for {len(files)} images...")
        for img_file in files:
            apply_watermark(img_file, WATERMARK_TEXT)
        
        print("\n✨ All done! Check the 'output_images' folder.")