import web 

import page.models.alumnos as alumnos
model_alumnos = alumnos.Alumnos()

render=web.template.render('page/views/alumnos/')

class Delete():
    def GET(self):
      try:
        return render.delete()
      except Exception as e:
        return "--E-R-R-0-R--" + str(e.args)
    def POST(self, matricula):
      try:
        form = web.input()
        matricula = form['matricula']
        result = model_alumnos.delete(matricula)
        web.seeother('/list')
      except Exception as e:
        return "--E-R-R-0-R--" + str(e.args)
