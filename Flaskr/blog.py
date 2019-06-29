from flask import (
  Blueprint, flash, g, redirect, render_template, request, url_for
)

from werkzeug.exeptions import abort
from Flaskr.auth import login_required
from Flaskr.db import get_db

bp = Blueprint('blog', __name__)