import pymongo

from Modules.blog import Blog
from Modules.posts import Post
from database import Database

Database.initialize()

blog = Blog(title="New Blog",
            author="Tara")

blog.new_post()

blog.save_to_db()

from_db = Blog.from_db(blog.id)

print(blog.get_post())



