from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/portfolio')
def portfolio():
    projects = [
        {'title': 'invictus', 'description': 'project made for invicuts', 'image': 'project1.jpg', 'link': 'https://github.com/ISTE-VESIT-ORG/SR-50-Invictus'},
        {'title': 'mentorlink', 'description': '5th sem project', 'image': 'project2.jpg', 'link': 'https://github.com/Aditya149202/MentorLink'},
        {'title': 'Eduforce', 'description': '6th sem project', 'image': 'project3.jpg', 'link': 'https://github.com/Aditya149202/EduForce'}
    ]
    return render_template('portfolio.html', projects=projects)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form.get('message','')
        return redirect(url_for('success', name=name, email=email, subject=subject, message=message))
    return render_template('contact.html')

@app.route('/success')
def success():
    name = request.args.get('name')
    email = request.args.get('email')
    subject = request.args.get('subject')
    message = request.args.get('message')
    return render_template('success.html', name=name, email=email, subject=subject, message=message)

if __name__ == '__main__':
    app.run(debug=True)
