from langchain.chat_models.openai import ChatOpenAI
from langchain.memory import ChatMessageHistory
from langchain.prompts import ChatPromptTemplate

from src.config import GlobalConfig


class DebateRound:
    def __init__(
        self,
        motion: str = "Parliament members should be appointed by a lottery among the general population",
        gov_prompt: str = "In parliament debates, you are the government. You are arguing for the motion: {gov_motion}. Your reasons are:\n{gov_args}\n\n{gov_mod}",
        gov_args: str = """- Democratic Representation
- Reducing Corruption
- Eliminating Campaign Costs""",
        gov_mod: str = """Create very emotional, dramatic, arguments.""",
        opp_prompt: str = "In parliament debates, I am the government and you are the opposition. You are arguing against my motion: {gov_motion}. Your reasons are:\n{opp_args}\n\nYou are also arguing against my points in the previous discussion.\n\n{opp_mod}",
        opp_args: str = """- Lack of Expertise
- Lack of Accountability
- Lack of Transparency
- Potential for Apathy""",
        opp_mod: str = """Create very calm, ironic arguments.""",
    ):
        self.motion = motion
        self.gov_prompt = gov_prompt
        self.gov_args = gov_args
        self.gov_mod = gov_mod
        self.opp_prompt = opp_prompt
        self.opp_args = opp_args
        self.opp_mod = opp_mod

        self.gov_history = ChatMessageHistory()
        self.opp_history = ChatMessageHistory()

        self.model = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=GlobalConfig.LLM_TEMPERATURE)  # type: ignore

    def gov_opening(self):
        gov_prompt_template = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    self.gov_prompt,
                ),
            ]
            + self.gov_history.messages
        )

        gov_chain = gov_prompt_template | self.model
        gov_speech = gov_chain.invoke(
            {
                "gov_motion": self.motion,
                "gov_args": self.gov_args,
                "gov_mod": self.gov_mod,
            }
        )

        self.gov_history.add_ai_message(gov_speech.content)
        self.opp_history.add_user_message(gov_speech.content)

        return gov_speech.content

    def gov_rebuttal(self):
        pass

    def gov_closing(self):
        pass

    def opp_opening(self):
        pass

    def opp_rebuttal(self):
        pass

    def opp_closing(self):
        pass
