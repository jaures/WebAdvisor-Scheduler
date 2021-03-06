
class Course:
	def __init__(self,sections,credits,desc):
		self.sections = sections # array of section objects #
		self.credits = credits # string #ex "3 credits" #
		self.desc = desc #string description#


class Section:
	def __init__(self,startDate,endDate,meetings,number):
		self.startDate = startDate # date(2017,3,5) == March 5th,2017
		self.endDate = endDate # date(2017,4,15) == April 15th, 2017
		self.meetings = meetings 
		self.number = number # string # "02" #

class Meeting:
	def __init__(self,meetingType,campus,startTime,endTime,professorName,room,recurrence):
		self.meetingType = meetingType # string # "Lecture"
		self.campus = campus # string # "Newark"
		self.startTime = startTime #Time string
		self.endTime = endTime #time string
		self.professorName = professorName #name string
		self.room = room #string
		self.recurrence = recurrence
