# Copyright 2013-2016 Luc Saffre
# This file is part of Lino Voga.
#
# Lino Voga is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# Lino Voga is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public
# License along with Lino Voga.  If not, see
# <http://www.gnu.org/licenses/>.

"""
The :xfile:`models` module for the :mod:`lino_voga.contacts` app.

"""


from django.utils.translation import ugettext_lazy as _

from lino.modlib.contacts.models import *

from lino_xl.lib.beid.mixins import BeIdCardHolder
from lino_xl.lib.appypod.mixins import PrintLabelsAction
from lino_cosi.lib.sales import models as sales


class Person(Person, BeIdCardHolder):
    pass


# class MyPartnerDetail(PartnerDetail, sales.PartnerDetailMixin):
class MyPartnerDetail(PartnerDetail):

    # main = 'general address more sales ledger'
    main = 'general address more ledger'

    #~ general = dd.Panel(PartnerDetail.main,label=_("General"))

    general = dd.Panel("""
    overview:30 contact_box:30 lists.MembersByPartner:20
    bottom_box
    """, label=_("General"))

    address = dd.Panel("""
    address_box
    """, label=_("Address"))

    more = dd.Panel("""
    id language
    addr1 url
    #courses.CoursesByCompany
    excerpts.ExcerptsByOwner
    """, label=_("More"))

    ledger = dd.Panel("""
    ledger_a ledger.MovementsByPartner
    sales.InvoicesByPartner
    """, label=dd.plugins.ledger.verbose_name)

    ledger_a = """
    invoice_recipient vat_regime
    payment_term paper_type
    """

    # sales = dd.Panel("""
    # """, label=dd.plugins.sales.verbose_name)

    bottom_box = """
    remarks
    """

    address_box = """
    name
    country region city zip_code:10
    street:25 street_no street_box
    addr2
    """

    contact_box = """
    #mti_navigator
    email
    phone
    #fax
    gsm
    """


class MyCompanyDetail(CompanyDetail, MyPartnerDetail):

    # main = 'general more ledger'

    address = dd.Panel("""
    address_box
    contacts.RolesByCompany
    """, label=_("Address"))

    more = dd.Panel("""
    id language type vat_id
    addr1 url
    rooms.BookingsByCompany
    notes.NotesByCompany
    """, label=_("More"))

    address_box = """
    prefix name
    country region city zip_code:10
    street:25 street_no street_box
    addr2
    """

    contact_box = dd.Panel("""
    #mti_navigator
    email:40
    phone
    gsm
    fax
    """)  # ,label = _("Contact"))

    bottom_box = """
    remarks
    """


class MyPersonDetail(PersonDetail, MyPartnerDetail):

    main = 'general address ledger more'

    general = dd.Panel("""
    overview:30 contact_box:30 lists.MembersByPartner:20
    remarks
    """, label=_("General"))

    address = dd.Panel("""
    address_box
    contacts.RolesByPerson
    """, label=_("Address"))

    more = dd.Panel("""
    id language url
    addr1 addr2 national_id
    notes.NotesByPerson
    """, label=_("More"))

    personal = ''

    address_box = """
    last_name first_name:15 #title:10 gender
    country region city zip_code:10
    #street_prefix street:25 street_no street_box
    birth_date age:10 personal
    """


# @dd.receiver(dd.pre_analyze)
# def customize_contacts1(sender, **kw):
#     sender.modules.contacts.Partner.define_action(
#         print_labels=PrintLabelsAction())


@dd.receiver(dd.post_analyze)
def customize_contacts2(sender, **kw):
    site = sender
    site.modules.contacts.Persons.set_detail_layout(MyPersonDetail())
    site.modules.contacts.Companies.set_detail_layout(MyCompanyDetail())
    site.modules.contacts.Partners.set_detail_layout(MyPartnerDetail())
    # site.modules.courses.Pupils.set_detail_layout(PupilDetail())
    # site.modules.courses.Teachers.set_detail_layout(TeacherDetail())