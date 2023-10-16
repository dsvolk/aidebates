import gradio as gr

# from src.config import GlobalConfig
from src.debates.round import DebateRound
from src.gradio import stream


def run_debate(motion, gov_args, opp_args):
    dround = DebateRound(motion, gov_args, opp_args)
    gov_speech = dround.gov_opening()
    # opp_speech = round.opp_opening()
    # gov_rebuttal = round.gov_rebuttal()
    # opp_rebuttal = round.opp_rebuttal()
    # gov_closing = round.gov_closing()
    # opp_closing = round.opp_closing()

    return [[f"""{gov_speech}"""]]


def ask_llm(message, history):
    for next_token, content in stream(message):
        yield (content)


with gr.Blocks() as app:
    chatInterface = gr.ChatInterface(
        fn=ask_llm,
    )

    # with gr.Accordion("Prompts", open=True):
    #     model_name_dd = gr.Dropdown(
    #         choices=["gpt-3.5-turbo", "gpt-4"],
    #         value="gpt-3.5-turbo",
    #         interactive=True,
    #         type="value",
    #         allow_custom_value=False,
    #         label="Model name",
    #     )
    #     gov_prompt_template_tb = gr.Textbox(
    #         lines=5,
    #         value="""In parliament debates, you are the government and I am the opposition. You are arguing for the motion: {gov_motion}. Your reasons are:""",
    #         interactive=True,
    #         placeholder="Enter government prompt template here...",
    #         label="Government prompt template",
    #     )
    #     opp_prompt_template_tb = gr.Textbox(
    #         lines=5,
    #         value="""In parliament debates, you are the opposition and I am the government. You are arguing against the motion: {opp_motion}. Your reasons are:""",
    #         interactive=True,
    #         placeholder="Enter opposition prompt template here...",
    #         label="Opposition prompt template",
    #     )

    # motion_dd = gr.Dropdown(choices=GlobalConfig.SAMPLE_MOTIONS, type="value", allow_custom_value=True, label="Motion")
    # gov_args_tb = gr.Textbox(lines=5, placeholder="Enter government arguments here...", label="Government arguments")
    # opp_args_tb = gr.Textbox(lines=5, placeholder="Enter opposition arguments here...", label="Opposition arguments")
    # start_btn = gr.Button(value="Start debate")

    # chatbot = gr.Chatbot()

    # start_btn.click(run_debate, [motion_dd, gov_args_tb, opp_args_tb], chatbot)

app.queue().launch()


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
