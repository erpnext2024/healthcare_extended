
import frappe
import json
from frappe import only_for
from healthcare_extended.globals import BREADCRUMBS
from healthcare_extended.patients_api import get_patients_popup_fields

def get_context(context):
    if "Patients Manager" not in frappe.get_roles(frappe.session.user):
        frappe.throw("You do not have permission to access this resource.", frappe.PermissionError)

    context.service_unit_type = frappe.get_all('Healthcare Service Unit Type', fields=['*'], order_by='creation desc')
    context.breadrcrumbs = BREADCRUMBS.get("healthcare_service_unit_type", {})

    for service_unit in context.service_unit_type:
    	if service_unit['_comments']:
        	service_unit['_comments'] = json.loads(service_unit['_comments'])

    return context
