import uuid

import datetime

from Modules.posts import Post
from database import Database


class Blog(object):
    def __init__(self, author, title, id=None):
        self.author = author
        self.title = title
        self.id = uuid.uuid4().hex if id is None else id

    def new_post(self):
        title = input("Enter post title")
        content = input("Enter post content")
        date = input("Input date in dd/mm/YYYY")
        if date=="":
            date=datetime.datetime.utcnow()
        else:
            date=datetime.datetime.strptime(date, "%d%m%Y")
        post = Post(blog_id=self.id,
                    title=title,
                    content=content,
                    author=self.author,
                    date=date)

        post.save_to_db()

    def get_post(self):
        return Post.from_blog(self.id)

    def save_to_db(self):
        Database.insert(collection='blogs',
                        post=self.json())

    def json(self):
        return {
            'author': self.author,
            'title': self.title,
            'id': self.id
        }
    @classmethod
    def from_db(cls, id):
        blog_data = Database.find_one( collection='blogs',
                                       query={'id': id})
        return cls( author= blog_data['author'],
                    title=blog_data['title'],
                    id=blog_data['id'])
