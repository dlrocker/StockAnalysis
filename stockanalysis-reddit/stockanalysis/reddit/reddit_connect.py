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

    for submission in reddit.subreddit("stocks").hot(limit=1):
        print(submission.title)
        print(submission.selftext)
        print("####################################################################")

        """
        Extracting comments with PRAW:
        - https://praw.readthedocs.io/en/latest/tutorials/comments.html#extracting-comments-with-praw
        - https://praw.readthedocs.io/en/latest/tutorials/comments.html#the-replace-more-method
        
        Important notes:
        - Can get comments from submission by list(submission.comments) or submission.comments.list()
        - The thread/submission may contain MoreComments object. Use the replace_more() method to remove them.
            - submission.comments.replace_more(limit=0) removes all MoreComments objects
            - submission.comments.replace_more(limit=None) replaces all MoreComments objects
            
            Each replace_more() requires a API request. replace_more() is destructive and can't be called on the same submission again.
        """
        # Limit at 5 for now to reduce API requests
        submission.comment_sort = "new"
        submission.comments.replace_more(limit=5)

        # Parse over comments in breath-first-search way (so, one "level" of comments at a time. i.e. all top level,
        # then all 2nd level, then 3rd level, and so on)
        print("Method 1 - Traverse all comments on level at a time")
        for comment in submission.comments.list():
            print(comment.body)
            print("####################################################################")

        print("Method 2 - Traverse one comment thread at a time")
        for top_level_comment in submission.comments:
            print("Top level comment: {}".format(top_level_comment.body))
            for second_level_comment in top_level_comment.replies:
                print("\nSecond level comment: {}\n\n".format(second_level_comment.body))
            print("\n####################################################################\n")


if __name__ == "__main__":
    args = parse_arguments()
    connect(args)
