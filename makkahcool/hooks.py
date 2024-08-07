from . import __version__ as app_version

app_name = "makkahcool"
app_title = "Makkah Cool"
app_publisher = "sastechnologies.co"
app_description = "Makkah Cool"
app_email = "rawas@sastechnologies.co"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/makkahcool/css/makkahcool.css"
# app_include_js = "/assets/makkahcool/js/makkahcool.js"

# include js, css files in header of web template
# web_include_css = "/assets/makkahcool/css/makkahcool.css"
# web_include_js = "/assets/makkahcool/js/makkahcool.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "makkahcool/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

doctype_js = {
    "Sales Invoice": "public/js/sales_vo.js",
    "Purchase Invoice": "public/js/purchase_vo.js",
    "Delivery Note": "public/js/delivery_vo.js",
    "Quotation": "public/js/quotation_vo.js",
    }

doc_events = {
	"Delivery Note": {
		"autoname": "makkahcool.makkah_cool.custom_script.delivery_note.autoname"
	},
    "Sales Invoice": {
		"autoname": "makkahcool.makkah_cool.custom_script.sales_invoice.autoname"
	},
    "Purchase Invoice": {
		"autoname": "makkahcool.makkah_cool.custom_script.purchase_invoice.autoname"
	},
    "Payment Entry": {
		"autoname": "makkahcool.makkah_cool.custom_script.payment_entry.autoname"
	},
}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "makkahcool.utils.jinja_methods",
#	"filters": "makkahcool.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "makkahcool.install.before_install"
# after_install = "makkahcool.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "makkahcool.uninstall.before_uninstall"
# after_uninstall = "makkahcool.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "makkahcool.utils.before_app_install"
# after_app_install = "makkahcool.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "makkahcool.utils.before_app_uninstall"
# after_app_uninstall = "makkahcool.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "makkahcool.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"makkahcool.tasks.all"
#	],
#	"daily": [
#		"makkahcool.tasks.daily"
#	],
#	"hourly": [
#		"makkahcool.tasks.hourly"
#	],
#	"weekly": [
#		"makkahcool.tasks.weekly"
#	],
#	"monthly": [
#		"makkahcool.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "makkahcool.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "makkahcool.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "makkahcool.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["makkahcool.utils.before_request"]
# after_request = ["makkahcool.utils.after_request"]

# Job Events
# ----------
# before_job = ["makkahcool.utils.before_job"]
# after_job = ["makkahcool.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"makkahcool.auth.validate"
# ]

fixtures=[
    {
    	"doctype": "DocType Layout",
        "filters": [
            [
                "name",
                "in",
                [ 
                    "Delivery Note",
                    "Purchase Order",
                    "Quotation",
                    "Purchase Invoice",
                    "Sales Invoice",
                    "Payment Entry"
                 ]
            ]
        ]
    },
    {
    	"doctype": "Custom Field",
        "filters": [
            [
                "name",
                "in",
                [ 
                    "Sales Invoice Item-sqty",
                    "Sales Invoice Item-buying_price_list",
                    "Quotation Item-buying_price_list",
                    "Delivery Note Item-last_buy_price",
                    "Delivery Note Item-buying_price_list",
                    "Delivery Note Item-sqty",
                    "Sales Invoice-home",
                    "Sales Invoice-street",
                    "Sales Invoice-block",
                    "Purchase Invoice Item-stock_q",
                    "Sales Invoice Item-last_buy_price",
                    "Sales Invoice Item-last_buy_price",
                    "Delivery Note-street",
                    "Delivery Note-block",
                    "Delivery Note-home",
                    "Sales Invoice-custom_lpo_and_reference_no",
                    "Delivery Note-custom_lpo_and_reference_no",
                    "Delivery Note-lpo_and_reference_no",
                    "Payment Entry-supplier_invoice_number",
                    "Quotation-custom_set_warehouse",
                    "Purchase Order-custom_email",
                    "Purchase Order-custom_mobile_no",
                    "Purchase Order-custom_payment_term",
                    "Purchase Order-custom_attn",
                    "Purchase Order-custom_quotation_ref",
                    "Quotation-custom_mobile_no",
                    "Quotation-custom_ref_no",
                    "Quotation-custom_email",
                    "Quotation-custom_payment_term",
                    "Quotation-custom_attn",
                    "Supplier Quotation-custom_attn",
                    "Supplier Quotation-custom_payment_term",
                    "Supplier Quotation-custom_mobile_no",
                    "Supplier Quotation-custom_date_break",
                    "Supplier Quotation-custom_email",
                    "Supplier Quotation-custom_quotation_ref",
                    "Quotation-custom_sales_teamw",
                    "Quotation-custom_sales_teamm",
                    "Delivery Note-custom_section_break_pidkp",
                    "Quotation Item-custom_available_qty",
                    "Delivery Note-block",
                    
                 ]
            ]
        ]
    },
    {
    	"doctype": "Property Setter",
        "filters": [
            [
                "name",
                "in",
                [ 
                    "Sales Invoice-set_posting_time-default"
                 ]
            ]
        ]
    }
]
