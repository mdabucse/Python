from jinja2 import Environment, FileSystemLoader
from config import TEMPLATE_DIR

env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))

def render_template(template_name, context):
    template = env.get_template(f"{template_name}.html")
    return template.render(context)