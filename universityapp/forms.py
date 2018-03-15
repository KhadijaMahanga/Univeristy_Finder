from django import forms

Gender_Options = [('', 'Select Gender'),('F', 'Female'), ('M', 'Male'),]
Region_Options = [('', 'Select Region'),('Mwanza', 'Mwanza'),('Arusha','Arusha'),('DAR ES SALAAM','DAR ES SALAAM'),('Dodoma','Dodoma'),
('Singida','Singida'),
('Mtwara','Mtwara'),
('Mara','Mara'),
('Morogoro','Morogoro'),
('Arusha','Arusha'),
('Arusha','Arusha'),
('Arusha','Arusha'),
('Arusha','Arusha'),
('Arusha','Arusha'),
('Arusha','Arusha'),
('Arusha','Arusha'),
('Arusha','Arusha'),
('Arusha','Arusha'),
('Arusha','Arusha'),
('Arusha','Arusha'),]
Career_Options = [('Doctor', 'Doctor'), ('Pilot', 'Pilot')]
Education_Level_Options = [('0', 'Education Level'), ('1', 'O-level'), ('2', 'Primary Education level')]


class InputForm(forms.Form):
    subjects = forms.CharField( help_text = "eg. History-E, Geography-C" )
    diplomas = forms.CharField( help_text = "eg. Diploma in Medicine-3.8" )
    olevel_subjects = forms.CharField( help_text = "eg. History-E, Geography-C" )
