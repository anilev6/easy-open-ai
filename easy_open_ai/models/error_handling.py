import openai


class EasyOpenAIError(BaseException):
    def __init__(self, original_exception: openai.error.OpenAIError):
        self.original_exception = original_exception

    def __str__(self):
        return str(self.original_exception)


def handle_openai_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except openai.error.OpenAIError as e:
            raise EasyOpenAIError(e) from None

    return wrapper


def ahandle_openai_error(func):
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except openai.error.OpenAIError as e:
            raise EasyOpenAIError(e) from None

    return wrapper
