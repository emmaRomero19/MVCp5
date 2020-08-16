import web
render=web.template.render('mvc/views/')

class Index:
    def GET(self):
        try:
            return render.index()
        except Exception as e:
            result=[]    
            result.append('error'+ str(e.args))
            return result