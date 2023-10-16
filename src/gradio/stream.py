from collections.abc import Generator
from queue import Empty, Queue
from threading import Thread

from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

from .callbacks import QueueCallback


def stream() -> Generator:
    q: Queue = Queue()
    job_done = object()

    llm = ChatOpenAI(streaming=True, model="gpt-3.5-turbo", callbacks=[QueueCallback(q)], temperature=0)

    gov_prompt_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "In parliament debates, I am the opposition and you are the government. You are arguing for the motion: {gov_motion}. Your reasons are:\n{gov_args}\n\nYou are also arguing against my points in the previous discussion.\n\n{gov_mod}",
            ),
        ]
    )

    gov_chain = gov_prompt_template | llm

    # Create a funciton to call - this will run in a thread
    def task():
        _ = gov_chain.invoke(
            {
                "gov_motion": "This house would ban the use of animals in circuses.",
                "gov_args": """- Cruelty to animals""",
                "gov_mod": """Create very calm, ironic arguments.""",
            }
        )
        q.put(job_done)

    # Create a thread and start the function
    t = Thread(target=task)
    t.start()

    content = ""

    # Get each new token from the queue and yield for our generator
    while True:
        try:
            next_token = q.get(True, timeout=1)
            if next_token is job_done:
                break
            content += next_token
            yield next_token, content
        except Empty:
            continue
