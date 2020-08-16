import web
import mvc.model.model as alumnos

model_alumno = alumnos.Alumnos()

render=web.template.render('mvc/views/alumnos/')

class Update:
    def GET(self, id_persona):
        try: 
            result=model_alumno.view(id_persona[0])
            return render.update(result)
        except Exception as e:
            result=[]    
            result.append('error'+ str(e.args))
            return result

    def POST(self, id_alumno):
        try:
            data=web.input()
            id=int(data.id_alumno)
            matricula=int(data.matricula)
            name=str(data.name)
            paterno=str(data.paterno)
            materno=str(data.materno)
            edad=int(data.edad)
            fecha=str(data.fecha)
            genero=str(data.genero)
            state=str(data.estado)
            model_alumno.update(id,matricula,name,paterno,materno,edad,fecha,genero,state)
            web.seeother('/list')
        except Exception as e:
            result=[]    
            result.append('error'+ str(e.args))
            return result