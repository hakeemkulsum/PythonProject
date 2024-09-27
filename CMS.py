# Base Content class
class Content:
    def __init__(self, title, author, content_type):
        self.title = title
        self.author = author
        self.content_type = content_type
        self.comments = []
        self.views = 0
        self.likes = 0

    def view(self):
        self.views += 1

    def like(self):
        self.likes += 1

    def add_comment(self, comment):
        self.comments.append(comment)

    def show_comments(self):
        return self.comments

    def get_popularity(self):
        return {
            "views": self.views,
            "likes": self.likes,
            "comments": len(self.comments)
        }

    def __str__(self):
        return f"{self.content_type} - {self.title} by {self.author}"

# Article class inheriting from Content
class Article(Content):
    def __init__(self, title, author, body):
        # Call the base class (Content) constructor
        super().__init__(title, author, "Article")
        self.body = body

    def __str__(self):
        return f"Article: {self.title} by {self.author}\n{self.body[:100]}..."  # Preview of content

    def update(self, new_article):
        # Update the title, author, and body of the article
        self.title = new_article.title
        self.author = new_article.author
        self.body = new_article.body

# Multimedia class inheriting from Content
class Multimedia(Content):
    def __init__(self, title, author, media_url):
        super().__init__(title, author, "Multimedia")
        self.media_url = media_url

    def __str__(self):
        return f"Multimedia: {self.title} by {self.author}\nMedia URL: {self.media_url}"

    def update(self, new_multimedia):
        # Update the title, author, and media URL
        self.title = new_multimedia.title
        self.author = new_multimedia.author
        self.media_url = new_multimedia.media_url

# CMS class to manage the content
class CMS:
    def __init__(self):
        self.content_list = []

    # Create new content
    def add_content(self, content):
        self.content_list.append(content)
        print(f"{content.content_type} added: {content.title}")

    # Read content (search by title)
    def get_content(self, title):
        for content in self.content_list:
            if content.title == title:
                return content
        print(f"Content with title '{title}' not found.")
        return None

    # Update content (by title)
    def update_content(self, title, new_content):
        content = self.get_content(title)
        if content:
            if type(content) != type(new_content):
                print(f"Cannot update content of type '{content.content_type}' with content of type '{new_content.content_type}'")
                return

            # Update content based on its type
            content.update(new_content)
            print(f"Content '{title}' updated.")
    
    # Delete content (by title)
    def delete_content(self, title):
        content = self.get_content(title)
        if content:
            self.content_list.remove(content)
            print(f"Content '{title}' deleted.")
    
    # Show all content
    def show_all_content(self):
        for content in self.content_list:
            print(content)

    # Generate popularity report
    def generate_popularity_report(self):
        for content in self.content_list:
            popularity = content.get_popularity()
            print(f"{content.title}: Views={popularity['views']}, Likes={popularity['likes']}, Comments={popularity['comments']}")

# Example Usage

# Create CMS instance
cms = CMS()

# Add articles and multimedia content
article1 = Article("Understanding AI", "Alice", "This is an article about AI.")
multimedia1 = Multimedia("AI in Action", "Bob", "https://media.url/ai_video")

cms.add_content(article1)
cms.add_content(multimedia1)

# Interact with content (views, likes, comments)
article1.view()
article1.view()
article1.like()
article1.like()

article1.add_comment("Great article!")
article1.add_comment("Interesting!")


multimedia1.view()
multimedia1.like()
multimedia1.add_comment("Awesome video!")

# Display all content
cms.show_all_content()

# Generate popularity report
cms.generate_popularity_report()

# Update content
new_article = Article("Understanding AI - Revised", "Alice", "Updated article about AI.")
cms.update_content("Understanding AI", new_article)

# Try updating multimedia with an article (should fail)
cms.update_content("AI in Action", new_article)  # This should give an error message

# Delete content
cms.delete_content("AI in Action")

# Show all content after update and delete
cms.show_all_content()

