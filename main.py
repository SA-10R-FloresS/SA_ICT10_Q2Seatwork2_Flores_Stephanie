from pyscript import document

def calculate_gwa(e):
	document.getElementById('result').innerHTML = ' '
	document.getElementById('summary').innerHTML = ' '

	subjects = ['Science', 'Sorcery', 'History', 'Linguistics', 'Cookery', 'Physical Education']
	units_subject = (5, 3, 2, 1)

	first_name = document.getElementById('first_name').value
	last_name = document.getElementById('last_name').value

	science = float(document.getElementById('science').value)
	sorcery = float(document.getElementById('sorcery').value)
	history = float(document.getElementById('history').value)
	linguistics = float(document.getElementById('linguistics').value)
	cookery = float(document.getElementById('cookery').value)
	pe = float(document.getElementById('pe').value)

	weighted_sum = (science * units_subject[0] + 
			sorcery * units_subject[0] + 
			linguistics * units_subject[1] +
			history * units_subject[1] +
			cookery * units_subject[2] + 
			pe * units_subject[3]) 
	total_units = (units_subject[0] * 2) + (units_subject[1] * 2) + units_subject[2] + units_subject[3]
	gwa = weighted_sum / total_units

	result = f"""<span>Hi, <b>{first_name} {last_name}</b>! Your general weighted average is <b>{gwa:.2f}</b>. """

	summary = f"""<div class="mt-2 mb-2 row">
		<div class="col-6">
			<strong>{subjects[0]}:</strong> {science:.0f}<br>
			<strong>{subjects[1]}:</strong> {sorcery:.0f}<br>
			<strong>{subjects[2]}:</strong> {history:.0f}<br>
		</div>
		<div class="col-6">
			<strong>{subjects[3]}:</strong> {linguistics:.0f}<br>
			<strong>{subjects[4]}:</strong> {cookery:.0f}<br>
			<strong>{subjects[5]}:</strong> {pe:.0f}
		</div>
	</div>"""

	document.getElementById('result').innerHTML = result
	document.getElementById('summary').innerHTML = summary

def reset_form(e):
	document.getElementById('first_name').value = ''
	document.getElementById('last_name').value = ''
	document.getElementById('science').value = ''
	document.getElementById('sorcery').value = ''
	document.getElementById('history').value = ''
	document.getElementById('linguistics').value = ''
	document.getElementById('cookery').value = ''
	document.getElementById('pe').value = ''
	document.getElementById('result').innerHTML = ''
	document.getElementById('summary').innerHTML = ''