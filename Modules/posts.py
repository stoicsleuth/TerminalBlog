class Post(object):
    def __init__(self, blog_id, title, date, content, author, id):
        self.blog_id = blog_id
        self.title = title
        self.date = date
        self.content = content
        self.author = author
        self.id = id

    def save_to_db(self):
        database.insert(collection='posts', data=self.json)

    def json_build(self):
        return {
            'id': self.id,
            'blog_id': self.blog_id,
            'date': self.date,
            'content': self.content,
            'author': self.author,
            'title': self.title
        }
