from flask import Flask, render_template, request
from wtforms import Form, StringField, TextAreaField, RadioField, SelectField

app = Flask(__name__)


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/viewpublications')
def viewpublications():
    return render_template('view_all_publications.html')


class PublicationForm(Form):
    title = StringField('Title')
    pubtype = RadioField('Type Of Publication', choices=[('sbook', 'Book'), ('smag', 'Magazine')], default='sbook')
    category = SelectField('Caterory', choices=[('', 'Select'), ('FANTASY', 'Fantasy'), ('FASHION', 'Fashion'),
                                                ('THRILLER', 'Thriller'), ('CRIME', 'Crime'), ('BUSINESS', 'Business')],
                           default='')
    publisher = StringField('Publisher')
    status = SelectField('status', choices=[('', 'Select'), ('P', 'Pending'), ('A', 'Available For Borrowing'),
                                            ('R', 'Only For Reference')], default='')
    isbn = StringField('ISBN No')
    author = StringField('Author')
    synopsis = TextAreaField('Synopsis')
    frequency = RadioField('Frequency', choices=[('D', 'Daily'), ('W', 'Weekly'), ('M', 'Monthly')])

@app.route('/newpublication')
def new():
    form = PublicationForm(request.form)
    return render_template('create_publication.html', form=form)


@app.route('/update')
def update_publication():
    # Setting values to the update_publication.html
    form = PublicationForm(request.form)
    form.title.data = 'Harry Potter and The Half Blood Prince'
    form.pubtype.data = 'sbook'
    form.category.data = 'FANTASY'
    form.publisher.data = 'Bloomsbury'
    form.status.data = 'A'
    form.isbn.data = '0-7475-8108-8'
    form.author.data = 'J. K. Rowling'
    form.synopsis.data = 'Severus Snape, a member of the Order of the Phoenix, meets with Narcissa Malfoy, Draco''s mother, and Lord Voldemort''s faithful supporter Bellatrix Lestrange. Narcissa expresses concern that her son might not survive a dangerous mission given to him by Lord Voldemort. Bellatrix feels Snape will be of no help until he surprises her by making an Unbreakable Vow with Narcissa, swearing on his life that he will protect and assist Draco in his mission.'
    return render_template('update_publication.html', form=form)


@app.route('/status1')
def status1():
    return render_template('split_equally.html')

@app.route('/tristan')
def tristan():
    return render_template('Tristan.html')


@app.route('/pakmeng1')
def pakmeng1():
    return render_template('PakMeng1.html')


@app.route('/pakmeng1Link')
def pakmeng1Link():
    return render_template('pakmeng1Link.html')


@app.route('/pakmeng2')
def pakmeng2():
    return render_template('PakMeng2.html')


@app.route('/pakmeng3')
def pakmeng3():
    return render_template('PakMeng3.html')



@app.route('/shaun')
def Split():
    return render_template('shaun.html')

@app.route('/shaun2')
def Equal():
    return render_template('shaun2.html')

@app.route('/shaun3')
def Basedonrecipient():
    return render_template('shaun3.html')

@app.route('/shaun4')
def Customize():
    return render_template('shaun4.html')

@app.route('/shaun5')
def R_Equal():
    return render_template('shaun5.html')



@app.route('/wk1')
def wk1():
    return render_template('wk1.html')

@app.route('/wk2')
def wk2():
    return render_template('wk2.html')

@app.route('/wk3')
def wk3():
    return render_template('wk3.html')

@app.route('/wk4')
def wk4():
    return render_template('wk4.html')


if __name__ == '__main__':
    app.run()

