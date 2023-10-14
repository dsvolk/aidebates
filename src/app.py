import gradio as gr

from src.debates.round import DebateRound

MOTIONS = [
    "This house would ban the use of facial recognition technology",
    "This house believes that we should privatize the prison system",
    "Parliament members should be appointed by a lottery among the general population",
]


def run_debate(motion, gov_args, opp_args):
    dround = DebateRound(motion, gov_args, opp_args)
    gov_speech = dround.gov_opening()
    # opp_speech = round.opp_opening()
    # gov_rebuttal = round.gov_rebuttal()
    # opp_rebuttal = round.opp_rebuttal()
    # gov_closing = round.gov_closing()
    # opp_closing = round.opp_closing()

    return [[f"""{gov_speech}"""]]


with gr.Blocks() as app:
    motion_dd = gr.Dropdown(choices=MOTIONS, type="value", allow_custom_value=True, label="Motion")
    gov_args_tb = gr.Textbox(lines=5, placeholder="Enter government arguments here...", label="Government arguments")
    opp_args_tb = gr.Textbox(lines=5, placeholder="Enter opposition arguments here...", label="Opposition arguments")
    start_btn = gr.Button(value="Start debate")

    chatbot = gr.Chatbot()

    start_btn.click(run_debate, [motion_dd, gov_args_tb, opp_args_tb], chatbot)

app.launch()


# def generate_stream(input_text):
#     # Replace this with your actual implementation
#     return "\n".join(f"Generated text {i} for {input_text}" for i in range(6))


# def create_app(input_text, text1, text2):
#     return generate_stream(input_text)


# iface = gr.Interface(
#     fn=create_app,
#     inputs=[
#         gr.Dropdown(choices=MOTIONS, type="value", allow_custom_value=True, label="Motion"),
#         gr.Textbox(lines=5, placeholder="Enter government arguments here...", label="Government arguments"),
#         gr.Textbox(lines=5, placeholder="Enter opposition arguments here...", label="Opposition arguments"),
#     ],
#     outputs="text",
#     allow_flagging="never",
# )

# iface.launch()
