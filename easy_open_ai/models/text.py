"""Basics that do the job. Each method call equals one API call."""

import openai
import tiktoken

from .api_key import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY


# ------------------------------------------------------General Custom Instructions------------------------------------------------------------
class BaseChatCompletion:
    model = "gpt-3.5-turbo"
    temperature = 0
    max_tokens = 1024

    def __init__(self, user_input: str):
        self.task_for_ai = None
        self.user_input = user_input

    def _get_messages(self):
        """returns a piece of json needed for the api call"""
        return [
            {"role": "system", "content": self.task_for_ai},
            {"role": "user", "content": self.user_input},
        ]

    def chat_completion_task(self) -> str:
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=self._get_messages(),
            temperature=self.temperature,
            max_tokens=self.max_tokens,
        )
        return response["choices"][0]["message"]["content"]

    async def async_chat_completion_task(self) -> str:
        response = await openai.ChatCompletion.acreate(
            model=self.model,
            messages=self._get_messages(),
            temperature=self.temperature,
            max_tokens=self.max_tokens,
        )
        return response["choices"][0]["message"]["content"]


# ------------------------------------------------------Grammar correction-------------------------------------------------------------
class GrammarCorrection(BaseChatCompletion):
    def __init__(self, user_input: str):
        self.task_for_ai = "You will be provided with statements in some language, and your task is to convert them to standard language fixing all the grammar."
        self.user_input = user_input


# ------------------------------------------------------Translate----------------------------------------------------------------------
class TranslateText(BaseChatCompletion):
    def __init__(self, user_input: str, target_language="Ukrainian"):
        self.task_for_ai = f"You will be provided with a text, and your task is to translate it into {target_language}."
        self.user_input = user_input


# ------------------------------------------------------Changing Tone of Text------------------------------------------------------
class ChangeTone(BaseChatCompletion):
    temperature = 0.4

    def __init__(self, user_input: str):
        self.task_for_ai = (
            "You will be provided with a text, and your task is to change its tone."
        )
        self.user_input = user_input


# ------------------------------------------------------Rephrasing Text------------------------------------------------------
class RephraseText(BaseChatCompletion):
    def __init__(self, user_input: str):
        self.task_for_ai = (
            "You will be provided with a text, and your task is to rephrase it."
        )
        self.user_input = user_input


# ------------------------------------------------------Summarizing Text------------------------------------------------------
class SummarizeText(BaseChatCompletion):
    def __init__(self, user_input: str):
        self.task_for_ai = "You will be provided with a lengthy text, and your task is to summarize it."
        self.user_input = user_input


# ------------------------------------------------------Text Moderation------------------------------------------------------
def num_tokens_from_string(string: str, model_name: str = "gpt-3.5-turbo") -> int:
    """Returns the number of tokens in a text string. Needed to limit up to 8k+ or whatever"""
    encoding = tiktoken.encoding_for_model(model_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens


class IsHarmfulText:  # free API call, no charge
    def __init__(self, user_input: str):
        self.user_input = user_input

    def validation_task(self) -> list:
        response = openai.Moderation.create(input=self.user_input)
        result = []
        r = response["results"][0]
        if r["flagged"]:
            for k, v in r["categories"].items():
                if v:
                    result.append(k)
        return result

    async def async_validation_task(self) -> list:
        response = await openai.Moderation.acreate(input=self.user_input)
        result = []
        r = response["results"][0]
        if r["flagged"]:
            for k, v in r["categories"].items():
                if v:
                    result.append(k)
        return result
