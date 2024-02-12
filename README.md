# DJANGO PATTERNS
### Pattern A

    This is the [b]first[/b] of the four **Primary Application Patterns** I am building out using'
tthe Django Web Framework. Each of them demonstrates varying degrees of functionality, specific features
depending on their intended audience and usage.


### Blog-like: Static Content

##### Purpose
    The purpose of this application pattern is for an individual or organization looking
to funnel traffic by way of *regularly updated content*. While this usually will be a blog,
the blog `Post` model is very extensible, and can encapsulate any type of repetitive content.


###### Noteworthy Features
    * No authentication
    * Paginated list view of Static Content
    * Side navigation area where most popular, most recent, posts can be shown
    * SEO-friendly, human readable URL patterns using Title slugs
    * RSS feed subscription CTA
    * sitemap.xml
    * Detail view for Posts
        - Each has "Share this post" CTA that allows one to share a link to the post via
        email
        - List of comments that guests have made on the post, no registration is required to comment
    * Markdown support for post content
    * PostgreSQL configuration and Postgres search functionalities
    * Tagging system for posts, can filter posts by tags and group them as "similar"



