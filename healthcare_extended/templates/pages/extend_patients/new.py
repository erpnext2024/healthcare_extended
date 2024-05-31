from healthcare_extended.globals import generate_breadcrumbs
from healthcare_extended.patients_api import get_patients_fields

def get_context(context):
    context.breadrcrumbs = generate_breadcrumbs("patients", "new_patient")
    context.patients_fields = get_patients_fields()
    return context
