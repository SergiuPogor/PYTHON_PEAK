from flask import Flask, request

app = Flask(__name__)

# Route with dynamic URL
@app.route("/user/<username>")
def show_user_profile(username):
    # A route that dynamically captures the username and responds accordingly
    return f"User: {username}"

# Route with dynamic integer and string parameters
@app.route("/post/<int:post_id>/<string:category>")
def show_post(post_id, category):
    # Route that captures both an integer post_id and a string category
    return f"Post ID: {post_id}, Category: {category}"

# Route with optional query parameters
@app.route("/search")
def search():
    query = request.args.get("q", "No search query provided")
    # If no query parameter is passed, default message is used
    return f"Search results for: {query}"

# Route with dynamic number of path segments (Wildcard)
@app.route("/files/<path:subpath>")
def show_subpath(subpath):
    # This route captures multiple segments like /files/subdir/file.txt
    return f"Subpath: {subpath}"

# Example POST request handler with dynamic data in the route
@app.route("/order/<int:order_id>", methods=["POST"])
def update_order(order_id):
    # This route updates an order and assumes dynamic POST data
    order_status = request.form.get("status", "pending")
    return f"Order {order_id} updated to status: {order_status}"

# Example route with a combination of GET and POST dynamic behavior
@app.route("/comment/<int:comment_id>", methods=["GET", "POST"])
def manage_comment(comment_id):
    if request.method == "POST":
        # In case of a POST request, update comment
        content = request.form.get("content", "No content")
        return f"Comment {comment_id} updated with content: {content}"
    else:
        # In case of a GET request, show comment
        return f"Viewing comment {comment_id}"

if __name__ == "__main__":
    app.run(debug=True)