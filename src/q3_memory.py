from typing import List, Tuple
import json

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    """
    Memory-optimized solution: Stream processing with minimal overhead.
    Uses a simple dict instead of Counter to reduce memory usage.
    """
    mention_counts = {}

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            tweet = json.loads(line)

            # Get mentions from mentionedUsers field
            mentioned_users = tweet.get('mentionedUsers')

            if mentioned_users:
                for user in mentioned_users:
                    username = user.get('username')
                    if username:
                        mention_counts[username] = mention_counts.get(username, 0) + 1

    # Sort and get top 10
    sorted_mentions = sorted(mention_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_mentions[:10]