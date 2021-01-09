# Script to connect to the Reddit API and pull information

import argparse
import praw

'''
A user agent is a unique identifier that helps Reddit determine the source of network requests.
To use Reddit’s API, you need a unique and descriptive user agent.
The recommended format is "<platform>:<app ID>:<version string> (by u/<Reddit username>)".
For example, "android:com.example.myredditapp:v1.2.3 (by u/fake_user)"
'''
user_agent = "centos:dlrocker.stockanalysis:v1.0 (by {user_id})"


def parse_arguments():
    parser = argparse.ArgumentParser(description='Process Stock Analysis App Reddit connection arguments.')

    parser.add_argument('-i', '--client-id', type=str, required=True,
                        help='The client ID is the 14-character string listed just under “personal use script” '
                             'for the desired developed application')
    parser.add_argument('-s', '--client-secret', type=str, required=True,
                        help='The client secret is the 27-character string listed adjacent '
                             'to secret for the application.')
    parser.add_argument('-u', '--user-id', type=str, required=True,
                        help='User ID who owns the client secret. i.e. u/fake_user')

    parsed_args = parser.parse_args()
    return parsed_args


def connect(parsed_args):
    reddit = praw.Reddit(
        client_id=parsed_args.client_id,
        client_secret=parsed_args.client_secret,
        user_agent=user_agent.format(user_id=parsed_args.user_id)
    )

    print(reddit.read_only)
    for submission in reddit.subreddit("stocks").hot(limit=10):
        print(submission.title)


if __name__ == "__main__":
    args = parse_arguments()
    connect(args)
