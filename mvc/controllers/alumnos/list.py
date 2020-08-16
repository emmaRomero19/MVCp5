import web
import mvc.model.model as alumnos

model_alumno = alumnos.Alumnos()

render=web.template.render('mvc/views/alumnos/')

class Lista:
    def GET(self):
        try:
            result=model_alumno.select()
            return render.list(result)
        except Exception as e:
            result=[]    
            result.append('error'+ str(e.args))
            return result