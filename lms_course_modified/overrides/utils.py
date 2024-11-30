from lms.lms.utils import get_lesson_url as original_get_lesson_url
from lms.lms.utils import show_start_learing_cta as original_show_start_learing_cta
import frappe

def custom_get_lesson_url(course, lesson_number):
	if not lesson_number:
		return
	else:
		member = frappe.session.user
		filters = {"member": member, "course": course}
		membership = frappe.db.exists("LMS Enrollment", filters)
		if membership:
			return f"/courses/{course}/learn/{lesson_number}"
		else:
			return f"/billing/course/{course}"



def custom_show_start_learing_cta(course, membership):
	
	print("##################### LOG ################")
	# if not membership:
	# 	return True
