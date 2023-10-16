import gradio as gr
from src.config import GlobalConfig
from src.debates.round import DebateRound


def stream_debate(motion, gov_prompt, opp_prompt, model_name):
    llm_params = {
        "model": model_name,
        "temperature": GlobalConfig.LLM_TEMPERATURE,
        "streaming": True,
    }
    dround = DebateRound(motion, gov_prompt, opp_prompt, llm_params)

    for content in dround.gov_speech():
        yield [[content, None]]

    saved_content = content

    for content in dround.opp_speech():
        yield [[saved_content, content]]


with gr.Blocks() as app:
    with gr.Row(equal_height=True) as row:
        with gr.Column(scale=5, min_width=600):
            motion_dd = gr.Dropdown(
                choices=GlobalConfig.SAMPLE_MOTIONS,
                value=GlobalConfig.SAMPLE_MOTIONS[0],
                interactive=True,
                type="value",
                allow_custom_value=True,
                label="Motion",
            )
            gov_prompt_tb = gr.Textbox(
                lines=10,
                value=GlobalConfig.GOV_PROMPT_TEMPLATE,
                interactive=True,
                type="text",
                placeholder="Enter government prompt here...",
                label="Government prompt",
            )
            opp_prompt_tb = gr.Textbox(
                lines=10,
                value=GlobalConfig.OPP_PROMPT_TEMPLATE,
                interactive=True,
                type="text",
                placeholder="Enter opposition prompt here...",
                label="Opposition prompt",
            )
        with gr.Column(scale=1, min_width=600):
            model_name_dd = gr.Dropdown(
                choices=GlobalConfig.LLM_MODEL_NAMES,
                value=GlobalConfig.LLM_MODEL_NAMES[0],
                interactive=True,
                type="value",
                allow_custom_value=False,
                label="Model name",
            )

    start_btn = gr.Button(value="Start debate")

    chatbot = gr.Chatbot(
        avatar_images=(GlobalConfig.GOV_AVATAR_PATH, GlobalConfig.OPP_AVATAR_PATH), show_copy_button=True
    )

    start_btn.click(stream_debate, [motion_dd, gov_prompt_tb, opp_prompt_tb, model_name_dd], chatbot, queue=True)


app.queue().launch()
