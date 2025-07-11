import gradio as gr
from utils.detector import detect_clothing
from utils.advisor import get_advice

def run_style_savvy(image, bg_remove, body_type, face_shape, gender, occasion):
    items = detect_clothing(image, do_bg_remove=bg_remove)
    advice_list = get_advice(items, body_type, face_shape, gender, occasion)

    unique_advice = []
    seen = set()
    for tip in advice_list:
        if tip not in seen:
            unique_advice.append(tip)
            seen.add(tip)

    html = """
    <div style="
        background-color: #1e1e1e;
        color: #f5f5f5;
        padding: 24px;
        border-radius: 16px;
        max-width: 640px;
        margin: auto;
        font-family: 'Segoe UI', sans-serif;
    ">
      <h2 style="
          margin-top: 0;
          font-size: 2em;
          color: #ff8c00;
          text-align: center;
          text-transform: uppercase;
      ">
        ✨ Your Personalized Style Tips ✨
      </h2>
      <ol style="
          padding-left: 20px;
          font-size: 1.2em;
          line-height: 1.8;
      ">
    """
    for advice in unique_advice:
        html += f"<li style='margin-bottom: 12px;'>{advice}</li>"
    html += "</ol></div>"

    return html

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("## 👗 StyleSavvy — AI Fashion Consultant")
    gr.Markdown("Upload your photo and get personalized fashion advice tailored to your features and occasion.")

    with gr.Row():
        with gr.Column(scale=1):
            with gr.Group():
                gr.Markdown("### 🧾 Style Details")
                bg_remove = gr.Checkbox(label="Remove Background")
                body_type = gr.Radio(["Slim", "Athletic", "Curvy", "Plus-size"], label="Body Type")
                face_shape = gr.Radio(["Oval", "Round", "Square", "Heart"], label="Face Shape")
                gender = gr.Radio(["Male", "Female"], label="Gender")
                occasion = gr.Textbox(label="Occasion", placeholder="e.g. Wedding, Office Party")

        with gr.Column(scale=1):
            with gr.Group():
                gr.Markdown("### 📸 Upload Your Look")
                image = gr.Image(type="pil", label="Upload Photo")

    submit_btn = gr.Button("✨ Generate Style Tips")
    output = gr.HTML()

    submit_btn.click(
        fn=run_style_savvy,
        inputs=[image, bg_remove, body_type, face_shape, gender, occasion],
        outputs=output
    )

if __name__ == "__main__":
    demo.launch()