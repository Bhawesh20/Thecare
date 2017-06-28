user_type_choices =(
	('Patient', 'Patient'),
	('Staff', 'Staff'),
)
gender_choices = (
	('', '--choose--'),
	('M', 'Male'),
	('F', 'Female'),
)
service_choices = (
	('', '--Choose--'),
	('MALE NURSE', 'Male Nurse'),
	('FEMALE NURSE', 'Female Nurse'),
	('BABY SITTER', 'Babysitter'),
	)
status_choices = (
	('Pending', 'Pending'),
	('Processing', 'Processing'),
	('Booked', 'Booked'),
	)
duration_choice = (
	('', '--Choose--'),
	('8hrs', '8hrs/day'),
	('12hrs', '12hrs/day'),
	('16hrs', '16hrs/day'),
	('24hrs', '24hrs/day'),
	)
period_choice = (
	('', '--Choose--'),
	('1day', '1day'),
	('7day', '7days'),
	('15day', '15days'),
	('30day', '30days'),
	)
test_choices = (
	('','--Lab Test--'),
	('Complete Blood Count', 'Complete Blood Count'),
	('Fast Blood Sugar', 'Fast Blood Sugar'),
	('Postprandial Blood Sugar', 'Postprandial Blood Sugar'),
	('Lipid Profile', 'Lipid Profile'),
	('Uric Acid', 'Uric Acid'),
	('Blood Pressure Test', 'Blood Pressure Test'),
	('','--Vaccination--'),
	('H1N1', 'H1N1'),
	('Chicken Pox', 'Chicken Pox'),
	('Typhoid', 'Typhoid'),
	('Hepatitis B', 'Hepatitis B'),
	('Pneumonia', 'Pneumonia'),
	)
servicetype_choice = (
	('','--Choose--'),
	('MN', 'Male Nurse'),
	('FN', 'Female Nurse'),
	('BS', 'Babysitter'),
	('PT','Physiotherapist'),
	)
