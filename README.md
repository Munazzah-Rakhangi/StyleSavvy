---
title: StyleSavvy
emoji: 🏆
colorFrom: gray
colorTo: purple
sdk: gradio
sdk_version: 5.29.0
app_file: app.py
pinned: false
short_description: Style Savvy - AI Style Fashion Consultant
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

# 👗 StyleSavvy — AI Fashion Consultant

StyleSavvy is an AI-powered virtual stylist that uses computer vision and natural language generation to give personalized fashion advice.

## ✨ Features
- Detects clothing from uploaded photos using YOLOS-Fashionpedia
- Removes background for better detection (optional)
- Provides tailored styling tips based on:
  - Body type
  - Face shape
  - Gender
  - Occasion
- Uses `google/flan-t5-large` to generate expert-level suggestions

## 📸 How to Use
1. Upload a clear photo of your outfit
2. Select your body type, face shape, and gender
3. Enter the event or occasion
4. Click **Generate Style Tips**
5. Enjoy your personalized fashion advice! 🪞

## 🛠️ Tech Stack
- Gradio UI
- Hugging Face Transformers
- YOLOS object detection
- FLAN-T5 language model
- remove.bg API for optional background removal

## 🧠 Example Use Case
> “A curvy woman with a round face going to a summer wedding”  
> → StyleSavvy suggests breathable floral fabrics, statement earrings, and pastel tones that match the event ambiance.

## 🔐 API Key
Make sure to add a Hugging Face **Secret**:
- `REMOVE_BG_API_KEY`: your remove.bg key

---

🚀 Try it live: [StyleSavvy on Hugging Face](https://huggingface.co/spaces/Munazz/StyleSavvy)
