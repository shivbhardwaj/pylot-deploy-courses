from system.core.controller import *

class Courses(Controller):
    def __init__(self, action):
        super(Courses, self).__init__(action)
        self.load_model('Course')
        self.db = self._app.db
   
    def index(self):
        courses=self.models['Course'].all_courses()
        return self.load_view('index.html', courses=courses)

    def add(self):
        if len(request.form['course_name'])<15:
            flash('Please enter a course name with more than 15 characters')
            return redirect('/')
        courses=self.models['Course'].add_course(request.form)
        return redirect('/')

    def destroy(self, id):
        courses=self.models['Course'].course_by_id(id)
        return self.load_view('delete.html', id=id, courses=courses)

    def destroy_process(self,id):
        courses=self.models['Course'].delete_course(id)
        return redirect('/')