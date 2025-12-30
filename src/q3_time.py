from typing import List, Tuple
import json
from collections import Counter

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    """
    Time-optimized solution: Load all mentioned users into memory.
    Uses Counter for fast aggregation of mentions.
    """
    mention_counter = Counter()

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            tweet = json.loads(line)

            
            mentioned_users = tweet.get('mentionedUsers')

            if mentioned_users:
                for user in mentioned_users:
                    username = user.get('username')
                    if username:
                        mention_counter[username] += 1

    return mention_counter.most_common(10)