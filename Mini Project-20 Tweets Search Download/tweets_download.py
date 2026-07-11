def search_tweets(query, count):
    print(f'Searching for {count} tweets containing: {query}')
    # Used to use tweepy or snscrape
    mock_tweets = [
        f'I love learning about {query} #AI',
        f'{query} is the future of tech.'
    ]
    return mock_tweets

if __name__ == '__main__':
    tweets = search_tweets('Agentic AI', 2)
    for t in tweets:
        print(t)