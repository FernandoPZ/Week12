import web
import page.models.alumnos as alumnos

model_alumnos = alumnos.Alumnos()
render=web.template.render('page/views/alumnos/')

class Insert():
    def GET(self):
      try:
        return render.insert()
      except Exception as e:
        return "--E-R-R-O-R--" + str(e.args)
        
    def POST(self):
      try:
        form = web.input()
        id_alu=form.id_alumno
        mat=form.matricula
        nom=form.nombre
        pap=form.papellido
        sap=form.sapellido
        eda=form.edad
        nac=form.naci
        gen=form.genero
        est=form.estado
        render.insert(id_alu,mat,nom,pap,sap,eda,nac,gen,est)
        web.seeother('/list')
      except Exception as e:
        return "--E-R-R-O-R--" + str(e.args)
