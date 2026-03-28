import json
import boto3

comprehend = boto3.client('comprehend')

def lambda_handler(event, context):
    try:
        review_text = event.get("review", "")

        if not review_text:
            return {
                "statusCode": 400,
                "body": "No review text provided"
            }
        response = comprehend.detect_sentiment(
            Text=review_text,
            LanguageCode='en'
        )

        sentiment = response['Sentiment']
        score = response['SentimentScore']

        print(f"Review: {review_text}")
        print(f"Sentiment: {sentiment}")
        print(f"Scores: {score}")

        return {
            "statusCode": 200,
            "review": review_text,
            "sentiment": sentiment,
            "score": score
        }

    except Exception as e:
        print("Error:", str(e))
        return {
            "statusCode": 500,
            "error": str(e)
        }