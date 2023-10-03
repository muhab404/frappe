'''
# get all nodes
GET /api/resource/Node

# get all nodes with filteration 
GET /api/resource/Node?filters=[["field1", "=", "value1"], ["field2", ">", "value2"]]

# get all nodes sorted by name in descinding order
GET /api/resource/Node?order_by=name%20desc

# get all nodes with starting record and number of records returned, like [OFFSET, LIMIT] in MySQL
GET /api/resource/Node?limit_start=5&amp;limit_page_length=10
# this is the same above becauser limit is an alias to limit_page_length
GET /api/resource/Node?limit_start=5&amp;limit=10


### Create a DocType ###
# just choose POST method and send the suitable body
POST /api/resource/Node 


### Update a node ###
PUT /api/resource/:doctype/:name

### Delete a node ###
DELETE /api/resource/:doctype/:name


# Frappe allows you to trigger arbitrary python methods using the REST API for handling custom logic. 
# These methods must be marked as whitelisted to make them accessible via REST.

'''
# import frappe

# @frappe.whitelist()
# def get_nodes():
#     nodes = frappe.get_all("Node", ["name", "content_id"])
#     return nodes


# @frappe.whitelist()
# def create_node():
#     nodes = frappe.get_all("Node", ["name", "content_id"])
#     return nodes