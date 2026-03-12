from flask import Flask, render_template
from views import index, course, contact, about

app = Flask(__name__)

app.add_url_rule('/', endpoint='index', view_func=index)
app.add_url_rule('/course/<course_id>', endpoint='course', view_func=course)
app.add_url_rule('/contact', endpoint='contact', view_func=contact, methods=['GET', 'POST'])
app.add_url_rule('/about', endpoint='about', view_func=about)

if __name__ == '__main__':
    app.run(debug=True)