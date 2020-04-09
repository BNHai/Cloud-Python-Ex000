import web
urls = (
'/', 'index'
)
class index:
    def GET(self):
        return "Nguyen Hai Bang 2172225/Week 03"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
