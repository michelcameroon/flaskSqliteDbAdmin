# begin

from flask import Flask, render_template, request, redirect
#from flask import Flask, render_template, request

from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import inspect

#from models import Courses

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskSqliteDbAdmin.db'

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

class Courses(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    idstr = str(id)
    name=db.Column(db.String(50))
    description = db.Column(db.String(250))
#    description = db.Column(db.Blob)

#    def __repr__(self) :        return "{} is the title and {} is the descript>
    def __repr__(self):
        return self.name + " " + self.description
#        return self.name
#        return self.description



#db.create.all()
#SQLAlchemy.create.all()
with app.app_context():
    db.create_all()

@app.route("/")
def main_page():
    '''
    here will come  how to list all tables in this db
    '''
#    return render_template('index.html',tables=tables)
    return render_template('index.html')



@app.route("/courses")
def courses():
    
    courses = Courses.query.all()
#    courses = db.session.query(Courses).filter().all()

    for course in courses:
        print (course)
    #db.session.delete(deletetodo)
    #db.session.commit()
    
    return render_template("courses.html", courses=courses)
#    return render_template("courses.html")


@app.route("/coursesNew")
def coursesNew():

#    table = inspect(model)
    table = inspect(Courses)
    tablec = table.c
    for column in table.c:
        print (column.name)

    for colName in tablec:
        print (colName)

    #print (table)

    #students = Students.query.all()
    #db.session.delete(deletetodo)
    #db.session.commit()
#    return render_template("studentsNew1.html")
    return render_template("coursesNew1.html", tablec=tablec)
#    return render_template("coursesNew1.html", table.c=table.c)
#    return render_template("studentsNew.html", table=table)
#    return render_template("studentsNew.html", tablec=tablec)
#    return render_template("students.html", students=students)


@app.route("/coursesInsert", methods=['GET','POST'])
def coursesInsert():
    print ('begin coursesInsert')
    #return render_template("coursesInsert.html")
    
    print ('begin coursesInsert')
    if request.method=='POST':
        print ('post')
        print (request.form)
#        fields = request.form['name']
        fields = request.form
        cDesc = request.form['courses.description']
        print (cDesc)
        coursesName = fields['courses.name']
        print (coursesName)

        courses = Courses(name=coursesName, description=cDesc)

        db.session.add(courses)
        db.session.commit()
        '''
        courses1 = Courses.query.all()
        print (courses1) 
        for course in courses1:
            print (course)
        '''
#db.session.delete(deletetodo)
    #db.session.commit()
       #        return render_template("courses.html", courses1=courses1)
       # return render_template("coursesInsert.html", courses1=courses1)
#        return render_template("coursesInsert.html", courses1=courses1)
        #return render_template("courses.html", courses1=courses1)
#        return redirect("/courses")
        return redirect("/courses")
        #return redirect("/coursesInsert")

 #       return render_template("courses.html")
    
    #return render_template("index.html")
    #return render_template("courses.html")
    #return render_template("index.html")







if __name__ == "__main__":
    app.run(debug=True)

