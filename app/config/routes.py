from system.core.router import routes
routes['default_controller'] = 'Courses'
routes['GET']['/']="Courses#index"
routes['POST']['/courses/add']='Courses#add'
routes['GET']['/courses/destroy/<id>']='Courses#destroy'
routes['/courses/destroy/<id>/process']='Courses#destroy_process'