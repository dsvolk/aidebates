import gradio as gr

MOTIONS = [
    "This house would ban the use of facial recognition technology",
    "This house believes that we should privatize the prison system",
    "Parliament members should be appointed by a lottery among the general population",
]


def generate_stream(input_text):
    # Replace this with your actual implementation
    return "\n".join(f"Generated text {i} for {input_text}" for i in range(6))


def create_app(input_text, text1, text2):
    return generate_stream(input_text)


iface = gr.Interface(
    fn=create_app,
    inputs=[
        gr.Dropdown(choices=MOTIONS, type="value", allow_custom_value=True, label="Motion"),
        gr.Textbox(lines=5, placeholder="Enter government arguments here...", label="Government arguments"),
        gr.Textbox(lines=5, placeholder="Enter opposition arguments here...", label="Opposition arguments"),
    ],
    outputs="text",
    allow_flagging="never",
)

iface.launch()
