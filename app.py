import gradio as gr
from src.config import GlobalConfig
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


def stream_debate():
    for next_token, content in stream():
        yield [[content, None]]

    saved_content = content

    for next_token, content in stream():
        yield [[saved_content, content]]


with gr.Blocks() as app:
    motion_dd = gr.Dropdown(choices=GlobalConfig.SAMPLE_MOTIONS, type="value", allow_custom_value=True, label="Motion")
    gov_args_tb = gr.Textbox(lines=5, placeholder="Enter government arguments here...", label="Government arguments")
    opp_args_tb = gr.Textbox(lines=5, placeholder="Enter opposition arguments here...", label="Opposition arguments")
    start_btn = gr.Button(value="Start debate")

    chatbot = gr.Chatbot(show_label=True, show_copy_button=True)

    start_btn.click(stream_debate, None, chatbot, queue=True)


app.queue().launch()


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
