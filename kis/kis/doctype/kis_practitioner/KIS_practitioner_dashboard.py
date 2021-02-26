from __future__ import unicode_literals
from frappe import _

def get_data():
	return {
		'heatmap': True,
		'heatmap_message': _('This is based on transactions against this kis Practitioner.'),
		'fieldname': 'practitioner',
		'transactions': [
			{
				'label': _('Appointments and Patient Encounters'),
				'items': ['Patient Appointment', 'Patient Encounter']
			}
		]

	}

