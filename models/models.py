# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError
class billable_timesheet(models.Model):
	_inherit = 'account.analytic.line'

	percentage_billable = fields.Float("Billable %")
	time_billable = fields.Float("Billable Time")

	def function_code(self, field):
		if not self.env.user.has_group('project.group_project_manager'):
			raise UserError("You must be project manager in order to change %s"%field)
		if field and field=='time_billable':
			if self.time_billable and self.unit_amount:
				self.percentage_billable = 100*(self.time_billable/self.unit_amount)

		if field and field=='percentage_billable':
			if self.percentage_billable and self.unit_amount:
				self.time_billable = (self.unit_amount*self.percentage_billable)/100


	@api.onchange('percentage_billable')
	def onchange_name(self):
	    self.function_code(field='percentage_billable')
	   
	@api.onchange('time_billable')
	def onchange_address(self):  
	    self.function_code(field='time_billable')

	@api.onchange('unit_amount')
	def onchange_unit_amount(self):
		if not self.env.user.has_group('project.group_project_manager'):
			return
		self.function_code(field='percentage_billable')
