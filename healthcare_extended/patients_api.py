from frappe import get_all
import frappe
from frappe import _
from healthcare_extended.globals import WEB_FORMS


def get_patients_fields():
	fields = get_all("Web Form Field", filters={"parent": WEB_FORMS['new-patient-form']},
					 fields=["*"], order_by="idx")

	for field in fields:
		if field.fieldtype == "Select":
			field.options = field.options.split('\n') if field.options else []
		elif field.fieldtype == "Link":
			linked_doctype = field.options
			field.options = get_all(linked_doctype, fields=["name"])
	return fields


def get_patients_popup_fields():
	fields = get_all("Web Form Field", filters={"parent": WEB_FORMS['new-patient-popup-form']},
					 fields=["*"], order_by="idx")

	for field in fields:
		if field.fieldtype == "Select":
			field.options = field.options.split('\n') if field.options else []
		elif field.fieldtype == "Link":
			linked_doctype = field.options
			field.options = get_all(linked_doctype, fields=["name"])

	return fields


@frappe.whitelist(allow_guest=True)
def submit_patient_form():
	if "Patients Manager" not in frappe.get_roles(frappe.session.user):
		return {'status': 'error', 'message': 'Unauthorized.'}

	post_data = frappe.form_dict
	new_patient = frappe.get_doc({'doctype': 'Patient'})

	for key, value in post_data.items():
		if hasattr(new_patient, key):
			setattr(new_patient, key, value)

	new_patient.insert()

	frappe.db.commit()

	return {'status': 'success', 'message': 'Patient Created Successfully!'}
