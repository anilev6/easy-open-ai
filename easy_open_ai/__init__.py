# Version 0.1.6
from .functions.picture import (
    get_picture,
    aget_picture,
    get_n_pictures,
    aget_n_pictures,
)
from .functions.text import get_answer, aget_answer, correct_grammar, acorrect_grammar

# Version 0.1.7
from .functions.picture import (
    get_picture_url,
    aget_picture_url,
    get_n_pictures_urls,
    aget_n_pictures_urls,
)
from .functions.text import (
    sum_up_as_haiku,
    asum_up_as_haiku,
    get_poem,
    aget_poem,
    get_answer_as_poem,
    aget_answer_as_poem,
)
from .functions.text import autocomplete_text, aautocomplete_text
from .functions.text import translate_text, atranslate_text
from .functions.text import get_answer_with_instruction, aget_answer_with_instruction

from .models.error_handling import EasyOpenAIException, EasyOpenAIRetryException
