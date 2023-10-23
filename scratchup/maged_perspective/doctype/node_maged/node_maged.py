# Copyright (c) 2023, scratchup and contributors
# For license information, please see license.txt
# APT http://localhost:8000/api/method/scratchup.node.get_all_nodes

import frappe
from frappe.model.document import Document
import json

class NodeMaged(Document):
	pass

@frappe.whitelist()
def get_context_of_node(node_name, context=None):
	node = frappe.get_doc("Node Maged", node_name)
	response = None
	if context:
		field_id_of_context = json.loads(node.contexts)[context]
		content_of_context =  frappe.get_doc("Node Content Maged",node.content )

		versions = json.loads(content_of_context.versions)
		content = versions[field_id_of_context]
		response = {
			"name": node.name,
			"contexts": json.loads(node.contexts),
			"content": content
		}
	else:
		response = {
			"name": node.name,
			"contexts": json.loads(node.contexts),
			"content": node.content
		}
	return response
