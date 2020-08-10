import web

urls = (
    '/', 'page.controllers.alumnos.index.Index',
    '/list', 'page.controllers.alumnos.list.List',
    '/insert', 'page.controllers.alumnos.insert.Insert',
    '/delete', 'page.controllers.alumnos.delete.Delete',
    '/view', 'page.controllers.alumnos.view.View',
    '/update', 'page.controllers.alumnos.update.Update',
)
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
