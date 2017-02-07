# Ansible and Jinja2 editor/debugger/renderer

A simple web-based app to edit, debug, and render ansible templates. 

This tool is forked and extended from the [jinja2-live-parser](https://github.com/jasonguy/jinja2-live-parser), which 
is a lightweight live parser for [Jinja2](http://jinja.pocoo.org/docs/dev/) based on [Flask](http://flask.pocoo.org/) and [Jquery](http://jquery.com/).  

## Install

### Clone + pip

    $ git clone https://github.com/jasonguy/ansible-template-editor.git
    $ pip install -r requirements.txt
    $ python parser.py

## Usage

You are all set, browse to `http://localhost:5000/` and paste in your ansible template code and variables.  
You can add any custom filter you'd like in `filters.py`.  Just make sure the function's name starts with `filter_`.
