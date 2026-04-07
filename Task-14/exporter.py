import json

def export_json(graph):
    with open("data/graph.json", "w") as f:
        json.dump({k: list(v) for k, v in graph.items()}, f, indent=2)


def export_sitemap(urls):
    with open("data/sitemap.xml", "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')

        for url in urls:
            f.write(f"  <url><loc>{url}</loc></url>\n")

        f.write("</urlset>")