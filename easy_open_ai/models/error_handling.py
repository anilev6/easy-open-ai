import warnings
import time
import asyncio


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
                raise Exception(error_message) from None
            retry_error_message = RETRY_ERROR_HANDLERS.get(error_type)
            if retry_error_message:
                raise Exception("Please retry later." + retry_error_message) from None
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

            raise Exception(
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
                raise Exception(error_message) from None
            retry_error_message = RETRY_ERROR_HANDLERS.get(error_type)
            if retry_error_message:
                raise Exception("Please retry later. " + retry_error_message) from None
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
                        print(f"Retry ({retries + 1}/{max_retries}): {RETRY_ERROR_HANDLERS[error_type]}")
                        warnings.warn(
                            f"Retry ({retries + 1}/{max_retries}): {RETRY_ERROR_HANDLERS[error_type]}"
                        )
                        retries += 1
                        await asyncio.sleep(initial_sleep * retries)
                    else:
                        raise e from None
            raise Exception(
                f"Max retries ({max_retries}) reached. Could not complete the operation."
            ) from None

        return wrapper

    return decorator
