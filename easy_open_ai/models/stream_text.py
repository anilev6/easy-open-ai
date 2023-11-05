# Example of an OpenAI ChatCompletion request with stream=True
# https://platform.openai.com/docs/guides/chat
import openai

from .api_key import OPENAI_API_KEY

# send a ChatCompletion request to count to 100
openai.api_key = OPENAI_API_KEY
# response = openai.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {
#             "role": "user",
#             "content": "Count to 10, with a comma between each number and no newlines. E.g., 1, 2, 3, ...",
#         }
#     ],
#     temperature=0,
#     stream=True,
# )


# collected_messages = []
# # iterate through the stream of events
# for chunk in response:
#     chunk_message = chunk["choices"][0]["delta"]  # extract the message
#     if chunk_message == {}:
#         break
#     collected_messages.append(chunk_message.get("content", ""))  # save the message
#     print(chunk_message.get("content", ""))

# full_reply_content = "".join(collected_messages)
# print(f"Full conversation received: {full_reply_content}")

from .error_handling import handle_openai_error_stream, ahandle_openai_error_stream


# ------------------------------------------------------General Custom Instructions------------------------------------------------------------
class BaseChatCompletionStream:
    DEFAULT_MAX_TOKENS = 1024
    DEFAULT_TEMPERATURE = 0
    DEFAULT_MODEL = "gpt-3.5-turbo"
    DEFAULT_TASK_FOR_AI = "You are a helpful assistant."

    def __init__(
        self,
        user_input: str,
        task_for_ai: str = DEFAULT_TASK_FOR_AI,
        model: str = DEFAULT_MODEL,
        max_tokens: int = DEFAULT_MAX_TOKENS,
        temperature: float = DEFAULT_TEMPERATURE,
    ):
        self.task_for_ai = task_for_ai
        self.user_input = user_input
        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature

    def _get_messages(self):
        """returns a piece of json needed for the api call"""
        return [
            {"role": "system", "content": self.task_for_ai},
            {"role": "user", "content": self.user_input},
        ]

    @handle_openai_error_stream
    def chat_completion_task(self) -> str:
        openai.api_key = OPENAI_API_KEY
        for chunk in openai.ChatCompletion.create(
            model=self.model,
            messages=self._get_messages(),
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            stream=True,
        ):
            chunk_message = chunk["choices"][0]["delta"]
            if chunk_message == {}:
                break
            yield chunk_message.get("content", "")

    @ahandle_openai_error_stream
    async def async_chat_completion_task(self) -> str:
        openai.api_key = OPENAI_API_KEY
        async_gen = await openai.ChatCompletion.acreate(
            model=self.model,
            messages=self._get_messages(),
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            stream=True,
        )
        async for chunk in async_gen:
            chunk_message = chunk["choices"][0]["delta"]
            if chunk_message == {}:
                break
            yield chunk_message.get("content", "")
