import tornado.ioloop
import tornado.web
import tornado.log
import queries
import os
import json
import requests
import psycopg2

from jinja2 import \
  Environment, PackageLoader, select_autoescape
  
ENV = Environment(
  loader=PackageLoader('appfiles', 'templates'),
  autoescape=select_autoescape(['html', 'xml'])
)


class TemplateHandler(tornado.web.RequestHandler):
  def render_template (self, tpl, context=None):
    if context is None:
      context = {}
      
    template = ENV.get_template(tpl)
    self.write(template.render(context))

class MainHandler(TemplateHandler):
  def get(self):
    self.set_header(
      'Cache-Control',
      'no-store, no-cache, must-revalidate, max-age=0')
    
    self.render_template("index.html")
      
  def post(self):
    sku = self.get_body_argument('sku')
    self.redirect('/product/{}'.format(sku))
    
    
    
    
class productHandler(TemplateHandler):
  def initialize(self):
      self.session = queries.Session(
      'postgresql://postgres@localhost:5432/apidb')
  def get(self, slug):
    self.set_header(
      'Cache-Control',
      'no-store, no-cache, must-revalidate, max-age=0')
    product = self.session.query(
      'SELECT * FROM apidata WHERE (sku, as_of) IN (SELECT sku, MAX(as_of) FROM apidata GROUP BY sku) AND sku LIKE %(slug)s',
      {'slug': slug}
    )
    self.render_template("product.html", {'product' : product[0]})
    
def make_app():
  return tornado.web.Application([
    (r"/", MainHandler),
    (r"/product/(.*)",productHandler),
    (
      r"/static/(.*)",
      tornado.web.StaticFileHandler,
      {'path': 'static'}
    ),
  ], autoreload=True)
  
if __name__ == "__main__":
  tornado.log.enable_pretty_logging()
  PORT = int(os.environ.get('PORT', '8080'))
  app = make_app()
  app.listen(PORT)
  tornado.ioloop.IOLoop.current().start()