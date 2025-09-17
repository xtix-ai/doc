project = 'XTIX'
copyright = '2025, XTIX'
author = 'nndii'
version = 'v2'
release = 'v2'

extensions = [
    'sphinxcontrib.httpdomain',
    'cloud_sptheme',
    # 'cloud_sptheme.ext.index_styling',
]

source_suffix = '.rst'
source_encoding = 'utf8'
master_doc = 'index'
exclude_trees = ['build']

pygments_style = 'sphinx'
html_theme = 'cloud'
# html_theme = 'XTIX'
# html_theme_options = {}
# html_theme_path = ['_templates']
html_static_path = ['_static']

primary_domain = 'http'
http_index_shortname = 'API Reference'
http_index_localname = 'XTIX HTTP API'
http_index_grouping = False
