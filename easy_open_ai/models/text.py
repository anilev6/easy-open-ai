"""Basics that do the job. Each method call equals one API call."""

import openai
import tiktoken

from .api_key import OPENAI_API_KEY

from .error_handling import handle_openai_error, ahandle_openai_error


# ------------------------------------------------------General Custom Instructions------------------------------------------------------------
class BaseChatCompletion:
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

    @handle_openai_error
    def chat_completion_task(self) -> str:
        openai.api_key = OPENAI_API_KEY
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=self._get_messages(),
            temperature=self.temperature,
            max_tokens=self.max_tokens,
        )
        return response["choices"][0]["message"]["content"]

    @ahandle_openai_error
    async def async_chat_completion_task(self) -> str:
        openai.api_key = OPENAI_API_KEY
        response = await openai.ChatCompletion.acreate(
            model=self.model,
            messages=self._get_messages(),
            temperature=self.temperature,
            max_tokens=self.max_tokens,
        )
        return response["choices"][0]["message"]["content"]


# ------------------------------------------------------Grammar correction-------------------------------------------------------------
class GrammarCorrection(BaseChatCompletion):
    def __init__(self, user_input):
        super().__init__(user_input)
        self.task_for_ai = """You will be provided with statements in some language, and your task is to convert them to standard language fixing all the grammar."""


# ------------------------------------------------------Translate----------------------------------------------------------------------
class TranslateText(BaseChatCompletion):
    def __init__(self, user_input, target_language=None):
        super().__init__(user_input)
        self.task_for_ai = f"You will be provided with a text, and your task is to translate it into {target_language}."


# ------------------------------------------------------Changing Tone of Text------------------------------------------------------
class ChangeTone(BaseChatCompletion):
    def __init__(self, user_input):
        super().__init__(user_input)
        self.temperature = 0.4
        self.task_for_ai = (
            """You will be provided with a text, and your task is to change its tone."""
        )


# ------------------------------------------------------Rephrasing Text------------------------------------------------------
class RephraseText(BaseChatCompletion):
    def __init__(self, user_input):
        super().__init__(user_input)
        self.temperature = 0.3
        self.task_for_ai = (
            """You will be provided with a text, and your task is to rephrase it."""
        )


# ------------------------------------------------------Summarizing Text------------------------------------------------------
class SummarizeText(BaseChatCompletion):
    def __init__(self, user_input):
        super().__init__(user_input)
        self.task_for_ai = """You will be provided with a lengthy text, and your task is to summarize it."""


class SummarizeHaiku(BaseChatCompletion):
    def __init__(self, user_input):
        super().__init__(user_input)
        self.temperature = 0.85
        self.task_for_ai = (
            """You will be given a text, and your task is to summarize it as haiku."""
        )


# ------------------------------------------------------Rhymes and Poems------------------------------------------------------
class GetPoem(BaseChatCompletion):
    def __init__(self, user_input):
        super().__init__(user_input)
        self.temperature = 0.65
        self.task_for_ai = """You are a poet. You will be given a text, and your task is to rewrite this text in a form of a poem, but preserve the meaning, language and approximate size of a text. """


class GetAnswerRhymes(BaseChatCompletion):
    def __init__(self, user_input):
        super().__init__(user_input)
        self.temperature = 0.9
        self.max_tokens = 512
        self.task_for_ai = """You are a poet. You will be given a question, and your task is to answer it in a form of a poem in the same language."""


# ------------------------------------------------------Autocomplete------------------------------------------------------
class Autocomplete(BaseChatCompletion):
    def __init__(self, user_input):
        super().__init__(user_input)
        self.temperature = 0.6
        self.task_for_ai = """
        You are an autocomplete assistant. Return only the autocompleted part. Mind the spaces and punctuation.
        Examples:
        User: Hello
        Assistant: , how are you doing?
        User: I wanted to let you know
        Assistant:  we just arrived.
    """


# ------------------------------------------------------Text Moderation------------------------------------------------------
def num_tokens_from_string(string: str, model_name: str = "gpt-3.5-turbo") -> int:
    """Returns the number of tokens in a text string. Needed to limit up to 8k+ or whatever"""
    encoding = tiktoken.encoding_for_model(model_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens


class IsHarmfulText:
    def __init__(self, user_input):  # free API call, no charge
        # need to filter the sofisticated way of swearing as well
        self.user_input = user_input

    @handle_openai_error
    def validation_task(self) -> list:
        openai.api_key = OPENAI_API_KEY
        response = openai.Moderation.create(input=self.user_input)
        result = []
        r = response["results"][0]
        if r["flagged"]:
            result = [k for k, v in r["categories"].items() if v]
        return result

    @ahandle_openai_error
    async def async_validation_task(self) -> list:
        openai.api_key = OPENAI_API_KEY
        response = await openai.Moderation.acreate(input=self.user_input)
        result = []
        r = response["results"][0]
        if r["flagged"]:
            result = [k for k, v in r["categories"].items() if v]
        return result
