from flask import Blueprint, request, jsonify

# Define the Blueprint
ptw_bp = Blueprint('ptw_bp', __name__)

ptw_data = []  # This will simulate a database for the example

@ptw_bp.route('/ptw', methods=['POST'])
def create_ptw():
    data = request.json
    ptw_data.append(data)
    return jsonify(data), 201

@ptw_bp.route('/ptw/<int:id>', methods=['PUT'])
def edit_ptw(id):
    data = request.json
    for ptw in ptw_data:
        if ptw.get('id') == id:
            ptw.update(data)
            return jsonify(ptw), 200
    return jsonify({'message': 'PTW not found'}), 404

@ptw_bp.route('/ptw/<int:id>', methods=['GET'])
def view_ptw(id):
    for ptw in ptw_data:
        if ptw.get('id') == id:
            return jsonify(ptw), 200
    return jsonify({'message': 'PTW not found'}), 404

@ptw_bp.route('/ptw/<int:id>', methods=['DELETE'])
def delete_ptw(id):
    global ptw_data
    ptw_data = [ptw for ptw in ptw_data if ptw.get('id') != id]
    return jsonify({'message': 'Deleted successfully'}), 204

@ptw_bp.route('/ptw', methods=['GET'])
def list_ptws():
    return jsonify(ptw_data), 200
