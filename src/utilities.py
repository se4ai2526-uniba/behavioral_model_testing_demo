"""
Utilities module for text preprocessing before model predictions.

This module contains various text preprocessing functions to clean and normalize
text data before feeding it to machine learning models.
"""

import re


def remove_emojis(text: str) -> str:
    """
    Remove emojis and other Unicode symbols from text.

    This function removes:
    - Emoticons (Unicode range U+1F600 to U+1F64F)
    - Symbols & Pictographs (Unicode range U+1F300 to U+1F5FF)
    - Transport & Map Symbols (Unicode range U+1F680 to U+1F6FF)
    - Flags (Unicode range U+1F1E0 to U+1F1FF)
    - Supplemental Symbols and Pictographs (Unicode range U+1F900 to U+1F9FF)
    - Miscellaneous Symbols and Pictographs (Unicode range U+2600 to U+26FF)
    - Dingbats (Unicode range U+2700 to U+27BF)
    - Enclosed Alphanumeric Supplement (Unicode range U+1F0A0 to U+1F0FF)
    - Enclosed Ideographic Supplement (Unicode range U+1F200 to U+1F2FF)
    - Miscellaneous Symbols (Unicode range U+2300 to U+23FF)
    - Geometric Shapes (Unicode range U+25A0 to U+25FF)
    - Variation Selectors (Unicode range U+FE00 to U+FE0F)
    - Zero Width Joiner (U+200D)

    Args:
        text: Input text string that may contain emojis and Unicode symbols.

    Returns:
        Cleaned text string with emojis and Unicode symbols removed.

    Examples:
        >>> remove_emojis("Hello 😀 World!")
        'Hello  World!'
        >>> remove_emojis("Great job! 👍🎉")
        'Great job! '
        >>> remove_emojis("No emojis here")
        'No emojis here'
    """
    if not isinstance(text, str):
        raise TypeError(f"Expected str, got {type(text).__name__}")

    # Comprehensive emoji pattern covering most Unicode emoji ranges
    # Excludes CJK characters and basic text ranges
    emoji_pattern = re.compile(
        "["
        "\U0001f600-\U0001f64f"  # emoticons
        "\U0001f300-\U0001f5ff"  # symbols & pictographs
        "\U0001f680-\U0001f6ff"  # transport & map symbols
        "\U0001f1e0-\U0001f1ff"  # flags (iOS)
        "\U0001f900-\U0001f9ff"  # supplemental symbols and pictographs
        "\U0001fa00-\U0001fa6f"  # chess symbols
        "\U0001fa70-\U0001faff"  # symbols and pictographs extended-a
        "\U00002702-\U000027b0"  # dingbats
        "\U0001f0a0-\U0001f0ff"  # enclosed alphanumeric supplement
        "\U00002300-\U000023ff"  # miscellaneous technical
        "\U00002600-\U000026ff"  # miscellaneous symbols
        "\U00002700-\U000027bf"  # dingbats
        "\U0000fe00-\U0000fe0f"  # variation selectors
        "\U00002190-\U000021ff"  # arrows
        "\U00002b50-\U00002b55"  # stars
        "\U0000231a-\U0000231b"  # watch
        "\U000023e9-\U000023f3"  # play/pause buttons
        "\U000023f8-\U000023fa"  # more buttons
        "\U0000fe0f"  # variation selector
        "\U0000200d"  # zero width joiner
        "\U0001f004"  # mahjong tile
        "\U0001f0cf"  # playing card
        "\U0001f170-\U0001f171"  # A and B buttons
        "\U0001f17e-\U0001f17f"  # O button
        "\U0001f18e"  # AB button
        "\U0001f191-\U0001f19a"  # squared CL, Cool, etc.
        "\U0000203c"  # double exclamation mark
        "\U00002049"  # exclamation question mark
        "\U000025aa-\U000025ab"  # black/white small square
        "\U000025b6"  # black right-pointing triangle
        "\U000025c0"  # black left-pointing triangle
        "\U000025fb-\U000025fe"  # white/black medium square
        "\U00002600-\U00002604"  # weather symbols
        "\U0000260e"  # telephone
        "\U00002611"  # ballot box with check
        "\U00002614-\U00002615"  # umbrella, hot beverage
        "\U00002618"  # shamrock
        "\U0000261d"  # white up pointing index
        "\U00002620"  # skull and crossbones
        "\U00002622-\U00002623"  # radioactive, biohazard
        "\U00002626"  # orthodox cross
        "\U0000262a"  # star and crescent
        "\U0000262e-\U0000262f"  # peace symbol, yin yang
        "\U00002638-\U0000263a"  # wheel of dharma, smileys
        "\U00002640"  # female sign
        "\U00002642"  # male sign
        "\U00002648-\U00002653"  # zodiac signs
        "\U0000265f-\U00002660"  # chess pieces
        "\U00002663"  # club suit
        "\U00002665-\U00002666"  # heart and diamond suit
        "\U00002668"  # hot springs
        "\U0000267b"  # recycling symbol
        "\U0000267e-\U0000267f"  # infinity, wheelchair
        "\U00002692-\U00002697"  # hammer, alembic, etc.
        "\U00002699"  # gear
        "\U0000269b-\U0000269c"  # atom symbol, fleur-de-lis
        "\U000026a0-\U000026a1"  # warning, high voltage
        "\U000026aa-\U000026ab"  # white/black circle
        "\U000026b0-\U000026b1"  # coffin, funeral urn
        "\U000026bd-\U000026be"  # soccer ball, baseball
        "\U000026c4-\U000026c5"  # snowman, sun behind cloud
        "\U000026c8"  # thunder cloud and rain
        "\U000026ce"  # ophiuchus
        "\U000026cf"  # pick
        "\U000026d1"  # rescue worker's helmet
        "\U000026d3-\U000026d4"  # chains, no entry
        "\U000026e9-\U000026ea"  # shinto shrine, church
        "\U000026f0-\U000026f5"  # mountain, sailboat, etc.
        "\U000026f7-\U000026fa"  # skier, tent, etc.
        "\U000026fd"  # fuel pump
        "\U00002934-\U00002935"  # arrow pointing right then curving up/down
        "\U00002b05-\U00002b07"  # arrows
        "\U00002b1b-\U00002b1c"  # black/white large square
        "\U00002b50"  # white medium star
        "\U00002b55"  # heavy large circle
        "\U00003030"  # wavy dash
        "\U0000303d"  # part alternation mark
        "\U00003297"  # circled ideograph congratulation
        "\U00003299"  # circled ideograph secret
        "]+",
        flags=re.UNICODE,
    )

    # Remove emojis
    cleaned_text = emoji_pattern.sub("", text)

    return cleaned_text
