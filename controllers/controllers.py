# -*- coding: utf-8 -*-
from odoo import http

# class BillableTimesheet(http.Controller):
#     @http.route('/billable_timesheet/billable_timesheet/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/billable_timesheet/billable_timesheet/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('billable_timesheet.listing', {
#             'root': '/billable_timesheet/billable_timesheet',
#             'objects': http.request.env['billable_timesheet.billable_timesheet'].search([]),
#         })

#     @http.route('/billable_timesheet/billable_timesheet/objects/<model("billable_timesheet.billable_timesheet"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('billable_timesheet.object', {
#             'object': obj
#         })