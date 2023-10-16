from typing import Any

from langchain.callbacks.base import BaseCallbackHandler


class QueueCallback(BaseCallbackHandler):
    """Callback handler for streaming LLM responses to a queue."""

    def __init__(self, q):
        self.q = q

    def on_llm_new_token(self, token: str, **kwargs: Any) -> None:
        self.q.put(token)

    def on_llm_end(self, *args, **kwargs: Any) -> None:
        return self.q.empty()

    def on_chat_model_start(self, *args, **kwargs: Any) -> None:
        pass
