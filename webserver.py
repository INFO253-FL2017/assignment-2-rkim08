"""
webserver.p
File that is the central location of code for your webserver.
"""

from flask import Flask, request, render_template

# Create application, and point static path (where static resources like images, css, and js files are stored) to the
# "static folder"
app = Flask(__name__, static_url_path="/static")

@app.route('/')
def hello_world():
    """
    If someone goes to the root of your website (i.e. http://localhost:5000/), run this function. The string that this
    returns will be sent to the browser
    """
    return render_template('index.html') # Render the template located in "templates/index.html"

@app.route('/index')
def index_page():
	return render_template('index.html')


@app.route('/about')
def about_page():
	return render_template('about.html')


@app.route('/contact')
def contact_page():
	return render_template('contact.html')


@app.route('/blog/8-experiments-in-motivation')
def blog_8():
	return render_template("blog/8_Experiments_in_Motivation.html")

@app.route('/blog/a-mindful-shift-of-focus')
def blog_mindful():
	return render_template("blog/A_Mindful_Shift_of_Focus.html")


@app.route('/blog/how-to-develop-an-awesome-sense-of-direction')
def blog_direction():
	return render_template("blog/How_to_Develop_an_Awesome_Sense_of_Direction.html")


@app.route('/blog/training-to-be-a-good-writer')
def blog_training():
	return render_template("blog/Training_to_Be_a_Good_Writer.html")


@app.route('/blog/what-productivity-systems-wont-solve')
def blog_what():
	return render_template("blog/What_Productivity_Systems_Won't_Solve.html")

@app.route('/contact', methods=['GET'])
def show_email_page():
  return render_template("contact.html", notifications=[])

# @app.route('/contact', methods=['POST'])
# def send_email():
#     message = request.form.get("message")
#     subject = request.form.get("subject")
#     name = request.form.get("firstname")
#     notifications = []

#     data = {
#         'from': 'rachel <rkim08@sandboxdee063edd9034d2a95668740a304ba67.mailgun.org>',
#         'to': 'rkim08@sandboxdee063edd9034d2a95668740a304ba67.mailgun.org',
#         'subject': "hi",
#         'text': "test",
#     }
#     auth = ('api', 'key-6b87a9c12af7e25199513c30269ba80b')
#     r = requests.post(
#         'https://api.mailgun.net/v3/sandboxdee063edd9034d2a95668740a304ba67.mailgun.org',
#         auth=auth,
#         data=data)
#     if r.status_code == requests.codes.ok:
#         notifications.append("Your email was sent")
#     else:
#         notifications.append("You email was not sent. Please try again later")



#     return render_template("contact.html", notifications=notifications)


@app.route('/contact', methods=['POST'])
def send_email():
    message = request.form.get("message")
    subject = request.form.get("subject")
    name = request.form.get("firstname")
    notifications = []

    data = {
        'from': os.environ["INFO253_MAILGUN_FROM_EMAIL"],
        'to': os.environ["INFO253_MAILGUN_TO_EMAIL"],
        'subject': "You just was sent a message",
        'text': message,
    }

    auth = (os.environ["INFO253_MAILGUN_USER"], os.environ["INFO253_MAILGUN_PASSWORD"])

    r = requests.post(
        'https://api.mailgun.net/v3/{}/messages'.format(os.environ["INFO253_MAILGUN_DOMAIN"]),
        auth=auth,
        data=data)

    if r.status_code == requests.codes.ok:
        notifications.append("Hi " + name + " your email was sent")
    else:
        notifications.append("You email was not sent. Please try again later")



    return render_template("contact.html", notifications=notifications)




