import web

urls = (
    '/', 'mvc.controllers.index.Index',
    '/list', 'mvc.controllers.alumnos.list.Lista',
    '/insert', 'mvc.controllers.alumnos.insert.Insert',
    '/delete/?', 'mvc.controllers.alumnos.delete.Delete',
    '/view/(.*)', 'mvc.controllers.alumnos.viewOne.View',
    '/update', 'mvc.controllers.alumnos.update.Update',
)
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()