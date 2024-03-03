import frappe

def get_lesson_urls(course, lesson_number):
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



def show_start_learing_ctas(course, membership):
	
	print("##################### LOG ################")
	# if not membership:
	# 	return True
