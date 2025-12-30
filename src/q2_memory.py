from typing import List, Tuple
import json
import re

def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    """
    Memory-optimized solution: Stream processing with minimal data structures.
    Uses a simple dict instead of Counter to reduce overhead.
    """
    emoji_counts = {}

    
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F1E0-\U0001F1FF"  # flags (iOS)
        "\U00002702-\U000027B0"
        "\U000024C2-\U0001F251"
        "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
        "\U0001FA00-\U0001FA6F"  # Chess Symbols
        "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
        "\U00002600-\U000026FF"  # Miscellaneous Symbols
        "\U00002700-\U000027BF"  # Dingbats
        "]+",
        flags=re.UNICODE
    )

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            tweet = json.loads(line)
            content = tweet.get('content', '')

            
            emojis = emoji_pattern.findall(content)

     
            for emoji_group in emojis:
                for emoji in emoji_group:
                    emoji_counts[emoji] = emoji_counts.get(emoji, 0) + 1

   
    sorted_emojis = sorted(emoji_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_emojis[:10]