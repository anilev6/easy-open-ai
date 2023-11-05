import warnings
import time
import asyncio

warnings.formatwarning = (
    lambda message, category, filename, lineno, line=None: f"{category.__name__}: {message}\n"
)

# https://platform.openai.com/docs/guides/error-codes/python-library-error-types
ERROR_HANDLERS = {
    "RateLimitError": "You have hit your assigned rate limit. Pace your requests. Read more in our Rate limit guide.",
    "InvalidRequestError": "Your request was malformed or missing some required parameters, such as a token or an input. Check the documentation for the specific API method you are calling and make sure you are sending valid and complete parameters.",
    "AuthenticationError": "Your API key or token was invalid, expired, or revoked. Check your API key or token and make sure it is correct and active. You may need to generate a new one from your account dashboard.",
}

RETRY_ERROR_HANDLERS = {
    "APIError": "Issue on our side. Contact us if the issue persists.",
    "Timeout": "Request timed out. Contact us if the issue persists.",
    "APIConnectionError": "Issue connecting to our services. Check your network settings, proxy configuration, SSL certificates, or firewall rules.",
    "ServiceUnavailableError": "Issue on our servers. Contact us if the issue persists. Check the status page.",
}


class EasyOpenAIException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class EasyOpenAIRetryException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def handle_openai_error(func):
    def wrapper(*args, **kwargs):
        try:

            @retry_with_backoff(max_retries=3, initial_sleep=1)
            def retry_wrapper():
                return func(*args, **kwargs)

            return retry_wrapper()
        except Exception as e:
            error_type = type(e).__name__
            error_message = ERROR_HANDLERS.get(error_type)
            if error_message:
                raise EasyOpenAIException(error_message) from None
            retry_error_message = RETRY_ERROR_HANDLERS.get(error_type)
            if retry_error_message:
                raise EasyOpenAIRetryException(
                    "Please retry later. " + retry_error_message
                ) from None
            else:
                raise e from None

    return wrapper


def retry_with_backoff(max_retries=3, initial_sleep=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    error_type = type(e).__name__
                    if error_type in RETRY_ERROR_HANDLERS:
                        warnings.warn(
                            f"Retry ({retries + 1}/{max_retries}): {RETRY_ERROR_HANDLERS[error_type]}"
                        )
                        retries += 1
                        time.sleep(initial_sleep * retries)
                    else:
                        raise e from None

            raise EasyOpenAIRetryException(
                f"Max retries ({max_retries}) reached. Could not complete the operation."
            ) from None

        return wrapper

    return decorator


def ahandle_openai_error(func):
    async def wrapper(*args, **kwargs):
        try:

            @aretry_with_backoff(max_retries=3, initial_sleep=1)
            async def retry_wrapper():
                return await func(*args, **kwargs)

            return await retry_wrapper()
        except Exception as e:
            error_type = type(e).__name__
            error_message = ERROR_HANDLERS.get(error_type)
            if error_message:
                raise EasyOpenAIException(error_message) from None
            retry_error_message = RETRY_ERROR_HANDLERS.get(error_type)
            if retry_error_message:
                raise EasyOpenAIRetryException(
                    "Please retry later. " + retry_error_message
                ) from None
            else:
                raise e from None

    return wrapper


def aretry_with_backoff(max_retries=3, initial_sleep=1):
    def decorator(func):
        async def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    return await func(*args, **kwargs)
                except Exception as e:
                    error_type = type(e).__name__
                    if error_type in RETRY_ERROR_HANDLERS:
                        warnings.warn(
                            f"Retry ({retries + 1}/{max_retries}): {RETRY_ERROR_HANDLERS[error_type]}"
                        )
                        retries += 1
                        await asyncio.sleep(initial_sleep * retries)
                    else:
                        raise e from None
            raise EasyOpenAIRetryException(
                f"Max retries ({max_retries}) reached. Could not complete the operation."
            ) from None

        return wrapper

    return decorator


def handle_openai_error_stream(func):
    def wrapper(*args, **kwargs):
        try:

            @retry_with_backoff_stream(max_retries=3, initial_sleep=1)
            def retry_wrapper():
                for item in func(*args, **kwargs):
                    yield item

            for i in retry_wrapper():
                yield i

        except Exception as e:
            error_type = type(e).__name__
            error_message = ERROR_HANDLERS.get(error_type)
            if error_message:
                raise EasyOpenAIException(error_message) from None
            retry_error_message = RETRY_ERROR_HANDLERS.get(error_type)
            if retry_error_message:
                raise EasyOpenAIRetryException(
                    "Please retry later. " + retry_error_message
                ) from None
            else:
                raise e from None

    return wrapper


def retry_with_backoff_stream(max_retries=3, initial_sleep=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    for i in func(*args, **kwargs):
                        yield i
                    break
                except Exception as e:
                    error_type = type(e).__name__
                    if error_type in RETRY_ERROR_HANDLERS:
                        warnings.warn(
                            f"Retry ({retries + 1}/{max_retries}): {RETRY_ERROR_HANDLERS[error_type]}"
                        )
                        retries += 1
                        time.sleep(initial_sleep * retries)
                    else:
                        raise e from None
            if retries >= max_retries:
                raise EasyOpenAIRetryException(
                    f"Max retries ({retries}) reached. Could not complete the operation."
                ) from None

        return wrapper

    return decorator


def ahandle_openai_error_stream(func):
    async def wrapper(*args, **kwargs):
        try:

            @aretry_with_backoff_stream(max_retries=3, initial_sleep=1)
            async def retry_wrapper():
                async for item in func(*args, **kwargs):
                    yield item

            async for i in retry_wrapper():
                yield i
        except Exception as e:
            error_type = type(e).__name__
            error_message = ERROR_HANDLERS.get(error_type)
            if error_message:
                raise EasyOpenAIException(error_message) from None
            retry_error_message = RETRY_ERROR_HANDLERS.get(error_type)
            if retry_error_message:
                raise EasyOpenAIRetryException(
                    "Please retry later. " + retry_error_message
                ) from None
            else:
                raise e from None

    return wrapper


def aretry_with_backoff_stream(max_retries=3, initial_sleep=1):
    def decorator(func):
        async def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    async for i in func(*args, **kwargs):
                        yield i
                    break
                except Exception as e:
                    error_type = type(e).__name__
                    if error_type in RETRY_ERROR_HANDLERS:
                        warnings.warn(
                            f"Retry ({retries + 1}/{max_retries}): {RETRY_ERROR_HANDLERS[error_type]}"
                        )
                        retries += 1
                        await asyncio.sleep(initial_sleep * retries)
                    else:
                        raise e from None
            if retries >= max_retries:
                raise EasyOpenAIRetryException(
                    f"Max retries ({retries}) reached. Could not complete the operation."
                ) from None

        return wrapper

    return decorator
