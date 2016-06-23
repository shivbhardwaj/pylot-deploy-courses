from system.core.model import Model

class Course(Model):
    def __init__(self):
        super(Course, self).__init__()
    
    def all_courses(self):
        query="SELECT * FROM courses"
        return self.db.query_db(query)

    def add_course(self, request_form):
        data={
            'course_name':request_form['course_name'],
            'description':request_form['description']
        }
        query="INSERT INTO courses (course_name, description, date_added, created_at, updated_at) VALUES (:course_name, :description, NOW(), NOW(), NOW())"
        return self.db.query_db(query, data)

    def course_by_id(self, id):
        query="SELECT * FROM courses WHERE id=:id LIMIT 1"
        data={'id':id}
        return self.db.get_one(query, data)
    
    def delete_course(self, id):
        data={'id':id}
        query="DELETE FROM courses WHERE id=:id"
        return self.db.query_db(query, data)