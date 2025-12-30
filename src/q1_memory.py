from typing import List, Tuple
from datetime import datetime
import json
from collections import Counter

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    """
    Memory-optimized solution: Process data in a streaming fashion.
    First pass: find top 10 dates. Second pass: find top user per date.
    """
   
    date_counts = Counter()

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            tweet = json.loads(line)
            date = datetime.fromisoformat(tweet['date']).date()
            date_counts[date] += 1

 
    top_10_dates = {date for date, _ in date_counts.most_common(10)}

  
    date_user_counts = {date: Counter() for date in top_10_dates}

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            tweet = json.loads(line)
            date = datetime.fromisoformat(tweet['date']).date()

            if date in top_10_dates:
                username = tweet['user']['username']
                date_user_counts[date][username] += 1

   
    result = []
    for date, _ in date_counts.most_common(10):
        top_user = date_user_counts[date].most_common(1)[0][0]
        result.append((date, top_user))

    return result