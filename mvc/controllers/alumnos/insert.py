import web
import mvc.model.model as alumnos

model_alumno = alumnos.Alumnos()

render=web.template.render('mvc/views/alumnos/')

class Insert:
    def GET(self):
        try:
            return render.insert()
        except Exception as e:
            result=[]    
            result.append('error'+ str(e.args))
            return result
    def POST(self):
        try:
            data=web.input()
            matricula=int(data.matricula)
            name=str(data.name)
            paterno=str(data.paterno)
            materno=str(data.materno)
            edad=int(data.edad)
            fecha=str(data.fecha)
            genero=str(data.genero)
            state=str(data.state)
            model_alumno.insert(matricula,name,paterno,materno, edad, fecha, genero, state)
            web.seeother('/list')
        except Exception as e:
            result=[]    
            result.append('error'+ str(e.args))
            return result