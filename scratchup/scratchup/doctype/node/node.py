# Copyright (c) 2023, scratchup and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import requests
import json

class Node(Document):
	pass
@frappe.whitelist(allow_guest=True)
def get_context(target_context_id, parent_context_id=None):
	node_content_id = "65352e8bb290b062d72d4c43"
	if parent_context_id:
		context_node = frappe.get_doc("Node", target_context_id)
		context_node.contexts = json.loads(context_node.contexts)
		node_content_id = context_node.contexts[parent_context_id]
		
		
	url = "http://192.168.1.111:5000/api/v1/node-contents/"
	target_context_node_content = None
	try:
		target_context_node_content =json.loads( requests.get(url+node_content_id)._content)
		if target_context_node_content["node_ids"]:
			node_ids_content = []
			for node_id in target_context_node_content["node_ids"]:
				node = frappe.get_doc("Node", node_id)
				node_content_id = json.loads(node.contexts)[target_context_id]
				node_content =json.loads(requests.get(url+node_content_id)._content)
				final_shape = {
					"node_id": node_id,
					"node_type": node.node_type,
					"node_content": node_content
				}
				node_ids_content.append(final_shape)			
			target_context_node_content["node_ids"] = node_ids_content
		if "relations" in target_context_node_content["properties"]:
			relations = []
			for relation_id in target_context_node_content["properties"]["relations"]:
				relation = frappe.get_doc("Relation", relation_id)
				relations.append(relation)
			target_context_node_content["properties"]["relations"] = relations
		return target_context_node_content
	except Exception as e:
		print("error",e)	
		return "error"