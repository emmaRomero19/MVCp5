import web
import mvc.model.model as alumnos

model_alumno = alumnos.Alumnos()

render=web.template.render('mvc/views/alumnos/')

class Delete:
    def GET(self, id_persona):
        try:
            result=model_alumno.view(id_persona[0])
            return render.delete(result)
        except Exception as e:
            result=[]    
            result.append('error'+ str(e.args))
            return result

    def POST(self, id_alumno):
        try:
            print("ingreso")
            data=web.input()
            id=int(data.id_alumno)
            model_alumno.delete(id)
            web.seeother('/list')
        except Exception as e:
            result=[]    
            result.append('error delete'+ str(e.args))
            return result