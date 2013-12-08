# -*- coding: UTF-8 -*-
## Copyright 2012-2013 Luc Saffre
## This file is part of the Lino project.
## Lino is free software; you can redistribute it and/or modify 
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 3 of the License, or
## (at your option) any later version.
## Lino is distributed in the hope that it will be useful, 
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the 
## GNU General Public License for more details.
## You should have received a copy of the GNU General Public License
## along with Lino; if not, see <http://www.gnu.org/licenses/>.


import os
#~ import lino

from lino.projects.std.settings import *
from decimal import Decimal


class Site(Site):
    #~ title = __name__
    version = "0.0.1"
    verbose_name = "Lino Faggio"
    url = "http://faggio.lino-framework.org"
    #~ author = "Luc Saffre"
    #~ author_email = "luc.saffre@gmx.net"
    
    #~ help_url = "http://lino.saffre-rumma.net/az/index.html"
    #~ migration_module = 'lino.projects.az.migrate'
    
    userdocs_prefix = 'faggio.'
    
    calendar_start_hour = 9
    calendar_end_hour = 21
    
    #~ demo_fixtures = 'std few_countries few_cities few_languages demo eiche demo2'.split()
    #~ demo_fixtures = 'std few_countries few_cities few_languages demo demo_bookings faggio demo2'.split()
    demo_fixtures = 'std few_languages demo demo_bookings faggio demo2'.split()
    
    start_year = 2013
    
    ignore_dates_before = None
    
    #~ project_model = 'contacts.Person'
    #~ project_model = 'school.Pupil'
    #~ project_model = 'courses.Course'
    #~ project_model = None
    user_model = 'users.User'
    
    #~ ldap_auth_server = 'DOMAIN_NAME SERVER_DNS'
    
    languages = 'en de fr'
    
    #~ def get_default_language(self):
        #~ return 'de'
    
    use_eid_jslib = False
    
    show_internal_field_names = True
    
    #~ index_view_action = "dsbe.Home"
    
    #~ override_modlib_models = set([
        #~ 'contacts.Person', 
        #~ 'sales.Invoice', 
        #~ 'sales.InvoiceItem', 
        #~ 'cal.Event', 
        #~ 'courses.Course', 
        #~ 'cal.Room', 
        #~ ])
    
    
    #~ remote_user_header = "REMOTE_USER"
    
       
    #~ def get_main_action(self,user):
        #~ return self.modules.ui.Home.default_action
        
    #~ def get_application_info(self):
        #~ return (__name__,__version__,__url__)
        
        
    #~ def setup_quicklinks(self,ui,user,tb):
        #~ tb.add_action(self.modules.contacts.Persons.detail_action)
        #~ if self.use_extensible:
            #~ tb.add_action(self.modules.cal.Panel)
        #~ tb.add_action(self.modules.dsbe.MyPersons)
        #~ tb.add_action(self.modules.isip.MyContracts)
        #~ tb.add_action(self.modules.jobs.MyContracts)
        
    def get_installed_apps(self):
        for a in super(Site,self).get_installed_apps():
            yield a
        yield 'django.contrib.contenttypes'
        yield 'lino.modlib.system'
        yield 'lino.modlib.users'
        yield 'lino.modlib.countries'
        #~ yield 'lino.modlib.contacts'
        yield 'lino_faggio.contacts'
        
        yield 'lino_faggio.courses'
        yield 'lino.apps.extensible'
        yield 'lino_faggio.cal'
        yield 'lino_faggio.rooms'
        
        yield 'lino.modlib.products'
        yield 'lino.modlib.accounts'
        yield 'lino.modlib.ledger'
        yield 'lino.modlib.vat'
        #~ yield 'lino.modlib.declarations'
        #~ yield 'lino.modlib.sales'
        yield 'lino.modlib.auto.sales'
        yield 'lino.modlib.finan'
        
        #~ yield 'lino.modlib.households'
        yield 'lino.modlib.notes'
        yield 'lino.modlib.uploads'
        #~ yield 'lino.modlib.cal'
        
        yield 'lino.modlib.outbox'
        #~ yield 'lino.modlib.pages'
        #~ yield 'lino.modlib.courses'
        yield 'lino_faggio'
        
    #~ def setup_workflows(self):
        #~ 
        #~ from lino.modlib.cal.workflows import welfare
      
    def setup_choicelists(self):
        """
        This defines default user profiles for :mod:`lino_welfare`.
        """
        super(Site,self).setup_choicelists()
        
        #~ raise Exception(123)
        from lino import dd
        from django.utils.translation import ugettext_lazy as _
        dd.UserProfiles.reset('* office accounts')
        add = dd.UserProfiles.add_item
        
        add('000', _("Anonymous"),     '_ _ _', name='anonymous',
            readonly=True, authenticated=False)
        add('100', _("User"),          'U U U', name='user')
        add('900', _("Administrator"), 'A A A', name='admin')
        
        self.modules.vat.configure(default_vat_class='exempt')

    def get_admin_main_items(self, ar):
        yield self.modules.courses.ActiveCourses
        

    #~ def get_vat_rate(self,tt,vc,vr):
        #~ VAT_RATES = dict(
          #~ exempt=Decimal(),
          #~ reduced=Decimal('0.07'),
          #~ normal=Decimal('0.20')
        #~ )
        #~ return VAT_RATES[vc.name]


