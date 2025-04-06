# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import subprocess

def _get_git_info():
    try:
        sha = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"]).decode().strip()
        branch = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"]).decode().strip()
        return sha, branch
    except Exception:
        return "latest", "latest"

sha, branch = _get_git_info()

html_context = {
    "git_sha": sha,
    "git_branch": branch,
}


project = 'py-benchmark-docs'
copyright = '2025, Ali-Akber Saifee'
author = 'Ali-Akber Saifee'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

html_js_files = [
    'benchmark-loader.js',
]
html_extra_path = ['_static']
html_sidebars = {
    "**": ["benchmark_context.html", "globaltoc.html", "sourcelink.html", "searchbox.html"]
}
