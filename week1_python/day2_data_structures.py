posts = [
    "How to Optimize WordPress",
    "SEO Best Practices 2024",
    "Javascript Performance Tips"
]

# WordPress posts data
print("Starting Posts:")
print(posts)
print(f"Total posts: {len(posts)}")

# Adding posts
print("\n--- Adding New Posts ---")

posts.append("React Fundamentals")
print(f"After append: {posts}")
print(f"Total now: {len(posts)}")

posts.insert(0, "Welcome Post")
print(f"After insert at start: {posts}")
print(f"Total now: {len(posts)}")

# Accessing posts
print("\n--- Accessing Individual Posts ---")

first_post = posts[0]
last_post = posts[-1]

print(f"First post: {first_post}")
print(f"Last post: {last_post}")

print(f"Second post: {posts[1]}")
print(f"Second-to-last post: {posts[-2]}")

# Slicing
print("\n--- Slicing Lists ---")

recent_posts = posts[-3:] # Last 3 posts
first_two = posts[:2] # First 2 posts
middle_posts = posts[1:4] # Posts from index 1 to 3 (4 is excluded)

print(f"All posts: {posts}")
print(f"Recent posts (last 3): {recent_posts}")
print(f"First two posts: {first_two}")
print(f"Middle posts (1:4): {middle_posts}")

# Let's experiment with slicing
print("\n--- Slicing Experiments ---")

# posts = ["Welcome Post", "How to Optimize WordPress", "SEO Best Practices 2024", "JavaScript Performance Tips", "React Fundamentals"]
#           0               1                            2                          3                              4

print(f"posts[1:3]: {posts[1:3]}") # Index 1 and 2 (3 is excluded)
print(f"posts[:3]: {posts[:3]}") # From start to index 2
print(f"posts[2:]: {posts[2:]}") # From index 2 to end
print(f"posts[::2]: {posts[::2]}") # Every 2nd item (step=2)
print(f"posts[::-1]: {posts[::-1]}") # Reverse the list!

# WordPress menu items experiment
menu_items = ["Home", "About", "Services", "Portfolio", "Blog", "Contact"]

print(f"Original menu: {menu_items}")
print("Original menu:", menu_items)
print("First 3 items:", menu_items[:3])
print("Last 2 items:", menu_items[-2:])
print("Every other itme:", menu_items[::2])
print("Reversed menu:", menu_items[::-1])

# Add a new menu item
menu_items.append("Testimonials")
print("After adding Testimonials:", menu_items)

# Insert "Products" between "Services" and "Portfolio"
menu_items.insert(3, "Products") # Position 3
print("After inserting Products:", menu_items)

# Practical WordPress scenario
print("\n--- Real WrodPress Example ---")

blog_posts = []

# Add posts as they are published
blog_posts.append("Getting Started with WordPress")
blog_posts.append("10 Essential Plugins")
blog_posts.append("SEO Optimization Guide")
blog_posts.append("Speed Optimization Tips")
blog_posts.append("Security Best Practices")

print(f"Total published posts: {len(blog_posts)}")

# Get recent posts for Home page (last 3)
homepage_posts = blog_posts[-3:]
print(f"Recent Blog Posts {homepage_posts}")

# Get older posts for Archive page (everything except last 3)
archive_posts = blog_posts[:-3]
print(f"Archive posts: {archive_posts}")

