# Changes the directory structure 
# from `blog/YEAR/DD-blog_post_dir_name`
# to `blog/blog_post_dir_name`
# This allows to have a structure in the work directory 
# that is not directly reflected in the URL of the blog posts.

from pathlib import Path

blog_path = Path("blog")
first_level_dirs = list(blog_path.iterdir())
for blog_post_dir in blog_path.glob("./*/*"):
    new_name = blog_post_dir.name.split("-", maxsplit=1)[1]  # Remove `DD-` prefix
    target_dir = blog_path
    new_path = target_dir / new_name
    blog_post_dir.rename(new_path)
 
for old_dir in first_level_dirs:
    old_dir.rmdir()
