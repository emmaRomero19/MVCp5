import web
import mvc.model.model as alumnos

model_alumno = alumnos.Alumnos()

render=web.template.render('mvc/views/alumnos/')

class View:
    def GET(self, id_persona):
        try: 
            result=model_alumno.view(id_persona)
            return render.viewOne(result)
        except Exception as e:
            result=[]    
            result.append('error'+ str(e.args))
            return result