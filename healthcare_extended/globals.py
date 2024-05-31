BREADCRUMBS = {
	"patients": [
		{"title": "Healthcare", "link": "/healthcare"},
		{"title": "Patients", "link": "/patients-list"}
	],
	"new_patient": [
		{"title": "New Patient", "link": "/patients-list/new"}
	],
	"healthcare_service_unit_type": [
		{"title": "Healthcare", "link": "/healthcare"},
		{"title": "Healthcare Service Unit Type", "link": "/healthcare-service-unit-type"},

	]
}

WEB_FORMS = {
	"new-patient-form": "new-patient",
	"new-patient-popup-form": "patient-popup"
}


def generate_breadcrumbs(*keys):
	merged_breadcrumbs = []

	for key in keys:
		if key in BREADCRUMBS:
			merged_breadcrumbs.extend(BREADCRUMBS[key])

	return merged_breadcrumbs
