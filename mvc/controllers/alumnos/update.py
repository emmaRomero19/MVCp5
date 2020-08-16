import web
render=web.template.render('mvc/views/alumnos/')

class Update:
    def GET(self):
        try: 
            return render.update()
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
            return render.list(matricula,name,paterno,materno,edad,fecha,genero,state)
        except Exception as e:
            result=[]    
            result.append('error'+ str(e.args))
            return result