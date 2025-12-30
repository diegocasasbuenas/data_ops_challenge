from typing import List, Tuple
from datetime import datetime
import json
from collections import Counter, defaultdict

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    """
    Time-optimized solution: Load all data into memory for fast processing.
    Uses dictionaries and counters for O(1) lookups and efficient counting.
    """
    date_counts = Counter()
    date_user_counts = defaultdict(Counter)

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            tweet = json.loads(line)
            date = datetime.fromisoformat(tweet['date']).date()
            username = tweet['user']['username']

            date_counts[date] += 1
            date_user_counts[date][username] += 1


    top_dates = date_counts.most_common(10)


    result = []
    for date, _ in top_dates:
        top_user = date_user_counts[date].most_common(1)[0][0]
        result.append((date, top_user))

    return result