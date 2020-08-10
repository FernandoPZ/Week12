import web 

render=web.template.render('page/views/alumnos/')

class Index():
    def GET(self):
      try:
        return render.index()
      except Exception as e:
        return "--E-R-R-R-R--" + str(e.args)
