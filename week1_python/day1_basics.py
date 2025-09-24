# Test data
plugins_data = [
    {"name": "Yoast SEO", "current": "19.8", "latest": "20.1"},
    {"name": "Elementor", "current": "3.15.2", "latest": "3.15.2"},
    {"name": "WooCommerce", "current": "7.8.0", "latest": "8.0.1"}
]

def version_to_tuple(version_string):
    return tuple(map(int, version_string.split('.')))

def check_plugins_for_updates(plugins_data):
    
    print("Analyzing Plugins...")
    processed = []

    for plugin in plugins_data:
        current_version = version_to_tuple(plugin["current"])
        latest_version = version_to_tuple(plugin["latest"])
        
        if current_version < latest_version:
            status = "Update Needed"
        else:
            status = "Up to Date"

        processed.append({
            "name": plugin["name"],
            "current": plugin["current"],
            "latest": plugin["latest"],
            "status": status
        })

    return processed

    # Call the inner function and print the results
results = check_plugins_for_updates(plugins_data)
for result in results:
    print(f"{result['name']}: {result['status']} (Current: {result['current']}, Latest: {result['latest']})")


