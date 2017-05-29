# The frontal lobe is responsible for thinking initiation, behaviour, judgment and other things
# On this context, the frontal lobe will swallow Lex's responses and return actionables
# through consulting the configured intents

class FrontalLobe(object):
	def handleResponse(self, message: dict):
		print (message)