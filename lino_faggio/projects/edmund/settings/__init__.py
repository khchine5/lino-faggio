# -*- coding: UTF-8 -*-

from __future__ import unicode_literals
from __future__ import print_function

import datetime

from lino_faggio.projects.base import *

class Site(Site):

    title = "Lino Faggio à la Edmund"
    languages = "en et"

    demo_fixtures = """std few_languages few_countries few_cities
    demo faggio demo2""".split()

