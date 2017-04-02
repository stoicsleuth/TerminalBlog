import uuid

import datetime

from database import Database


class Post(object):
    def __init__(self, blog_id, title, content, author, date=datetime.datetime.utcnow(), id=None):
        self.blog_id = blog_id
        self.title = title
        self.createdDate = date
        self.content = content
        self.author = author
        self.id = uuid.uuid4().hex if id is None else id

    def save_to_db(self):
        Database.insert(collection='posts', post=self.json_build())

    def json_build(self):
        return {
            'id': self.id,
            'blog_id': self.blog_id,
            'date': self.createdDate,
            'content': self.content,
            'author': self.author,
            'title': self.title
        }

    @staticmethod
    def from_mongo(id):
        return Database.find_one(collection='posts', query={'id': id})

    @staticmethod
    def from_blog(blog_id):
        return [post for post in Database.find(collection='posts', query={'blog_id': blog_id})]
