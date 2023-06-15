import praw
import csv

reddit_authorized = praw.Reddit(client_id="wvuk3g4vWcwdUFaEnwlyCA",
                                client_secret="3G3MzKZOjB5GfD4sFBMf_lcuZBrO2g",
                                user_agent="my_user_agent")#,
                                #username=" ",
                                #password=" ")

#print(reddit_authorized.read_only)
used = []
with open('used.txt', 'r') as file0:
    for line in file0:
        line = line.strip()
        used.append(line)
file0.close()

print('write url:')
url = input()

if url in used:
    print("URL IS ALREADY USED!")
    exit()

submission = reddit_authorized.submission(url)

print(submission.title)

author = submission.author
#print(author)

submission.comment_sort = 'top'
coms = submission.comments

#top_com =coms[0]
#print(top_com.body)
#print(type(top_com.body))


def extract_author_comments(comments, author_name):
    author_comments = []
    for comment in comments:
        if isinstance(comment, praw.models.reddit.more.MoreComments):
            comment_list = comment.comments()
            author_comments.extend(extract_author_comments(comment_list, author_name))
        else:
            if comment.author and comment.author.name == author_name:
                if len(comment.body.split()) > 3:
                    author_comments.append(comment.body)
            if comment.replies:
                author_comments.extend(extract_author_comments(comment.replies, author_name))
    return author_comments


author_comments = extract_author_comments(coms, author)

print(author_comments[0])

with open('data.csv', 'a') as file:
    writer = csv.writer(file, lineterminator='\n')
    for string in author_comments:
        writer.writerow([string])
file.close()


with open('used.txt', 'a') as file1:
    # write a new ID to the file
    file1.write(url+'\n')