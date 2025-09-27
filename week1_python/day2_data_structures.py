posts = [
    "How to Optimize WordPress",
    "SEO Best Practices 2024",
    "Javascript Performance Tips"
]

print("Starting Posts:")
print(posts)
print(f"Total posts: {len(posts)}")

print("\n--- Adding New Posts ---")

posts.append("React Fundamentals")
print(f"After append: {posts}")
print(f"Total now: {len(posts)}")

posts.insert(0, "Welcome Post")
print(f"After insert at start: {posts}")
print(f"Total now: {len(posts)}")


