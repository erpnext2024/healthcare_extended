
import frappe
import json
from frappe import only_for
from healthcare_extended.globals import BREADCRUMBS
from healthcare_extended.patients_api import get_patients_popup_fields

#Get List of Patients
def get_context(context):
    if "Patients Manager" not in frappe.get_roles(frappe.session.user):
        frappe.throw("You do not have permission to access this resource.", frappe.PermissionError)

    context.patient_list = frappe.get_all('Patient', fields=['*'], order_by='creation desc')
    context.patients_fields = get_patients_popup_fields()
    context.breadrcrumbs = BREADCRUMBS.get("patients", {})

    for patient in context.patient_list:
    	if patient['_comments']:
        	patient['_comments'] = json.loads(patient['_comments'])

    return context
