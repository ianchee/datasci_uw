import json
import sys

sent_dict = {}

def parse_sentiment_file(sent_file):
	for line in sent_file:
		sentiments = line.split("\t")
		sent_dict[sentiments[0]] = int(sentiments[1].replace("\n", ""))

def extract_tweet_text(tweet_json):
	tweet = json.loads(tweet_json)
	text = tweet.get('text')

	return text if text != None else ""

def eval_tweet_sentiment(tweet_text):
	tweet_terms = tweet_text.split(" ")
	sentiment = 0

	for term in tweet_terms:
		if sent_dict.has_key(term):
			sentiment = sentiment + sent_dict[term]
	return sentiment

def parse_tweet_file(tweet_file):
	for line in tweet_file:
		tweet_text = extract_tweet_text(line)
		print float(eval_tweet_sentiment(tweet_text))

def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	parse_sentiment_file(sent_file)
	parse_tweet_file(tweet_file)
	

if __name__ == '__main__':
    main()
