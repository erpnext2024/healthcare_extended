app_name = "healthcare_extended"
app_title = "Healthcare Extended"
app_publisher = "NexuSuite"
app_description = "Extended the Healthcare Source"
app_email = "ethmain2015@gmail.com"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/healthcare_extended/css/healthcare_extended.css"
# app_include_js = "/assets/healthcare_extended/js/healthcare_extended.js"

# include js, css files in header of web template
web_include_css = ["/assets/healthcare_extended/css/healthcare_extended.css",
				   "https://cdn.datatables.net/v/dt/jq-3.7.0/dt-2.0.7/datatables.min.css"]
web_include_js = ["https://cdn.datatables.net/v/dt/dt-2.0.7/datatables.min.js",
				  "/assets/healthcare_extended/js/healthcare_extended.js"]

website_route_rules = [
	{"from_route": "/patients-list", "to_route": "/extend_patients/list"},
	{"from_route": "/patients-list/new", "to_route": "/extend_patients/new"},
	{"from_route": "/healthcare-service-unit-type", "to_route": "/healthcare_service_unit_type/list"}
]

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "healthcare_extended/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
doctype_list_js = {
	"Patient Appointment": "healthcare_extended/custom_secript/patient_appointment_list.js",
	"Healthcare Service Unit":"healthcare_extended/custom_secript/healthcare_service_unit.js",
	"Healthcare Service Unit Type":"healthcare_extended/custom_secript/healthcare_service_unit_type.js",
	"Healthcare Practitioner":"healthcare_extended/custom_secript/healthcare_practitioner.js"
}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "healthcare_extended/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "healthcare_extended.utils.jinja_methods",
# 	"filters": "healthcare_extended.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "healthcare_extended.install.before_install"
# after_install = "healthcare_extended.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "healthcare_extended.uninstall.before_uninstall"
# after_uninstall = "healthcare_extended.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "healthcare_extended.utils.before_app_install"
# after_app_install = "healthcare_extended.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "healthcare_extended.utils.before_app_uninstall"
# after_app_uninstall = "healthcare_extended.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "healthcare_extended.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }


# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"healthcare_extended.tasks.all"
# 	],
# 	"daily": [
# 		"healthcare_extended.tasks.daily"
# 	],
# 	"hourly": [
# 		"healthcare_extended.tasks.hourly"
# 	],
# 	"weekly": [
# 		"healthcare_extended.tasks.weekly"
# 	],
# 	"monthly": [
# 		"healthcare_extended.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "healthcare_extended.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "healthcare_extended.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "healthcare_extended.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["healthcare_extended.utils.before_request"]
# after_request = ["healthcare_extended.utils.after_request"]

# Job Events
# ----------
# before_job = ["healthcare_extended.utils.before_job"]
# after_job = ["healthcare_extended.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"healthcare_extended.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }
