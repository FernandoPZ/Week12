import web
import page.models.alumnos as alumnos

model_alumnos = alumnos.Alumnos()

render=web.template.render('page/views/alumnos/')

class View():
    def GET(self):
      try:
        result = model_alumnos.view(matricula)[0]
        return render.view(result)
      except Exception as e:
        return "--E-R-R-0-R--" + str(e.args)
