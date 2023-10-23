# Copyright (c) 2023, scratchup and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import json

class NodeOmar(Document):
	pass

@frappe.whitelist()
def get_nodes_of_context( context_id):
	atrributes = frappe.db.get_list("Node Omar",fields=['name', 'type', 'properties'], filters={'type': 'attribute'})
	def map_to_json(atrribute):
		return {
			"name": atrribute.name,
			"type": atrribute.type,
			"properties": json.loads(atrribute.properties)
		}
	result = map(map_to_json,atrributes)
	nodes_of_context  = None
	for obj in result:
		if obj['properties']['contextId'] == context_id:
			nodes_of_context = obj['properties']['connection']

	response = None
	if nodes_of_context:
		node_one = frappe.get_doc("Node Omar", nodes_of_context[0])
		node_two = frappe.get_doc("Node Omar", nodes_of_context[1])
		response = [
			node_one,
			node_two
		]
	return response