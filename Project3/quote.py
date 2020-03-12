from quote_locators import QuoteLocators

class QuoteParser:
	"""
	Given one of the specific quote divs, find out the data
	about the quote( quote content, author, tags).
	"""

	def __init__(self, parent):
		self.parent = parent


	def __repr__(self):
		return ("Quote %s, by %s"%(self.content,self.author))


	@property
	def content(self):
		locator = QuoteLocators.CONTENT
		return self.parent.select_one(locator).string

	@property
	def author(self):
		locator = QuoteLocators.AUTHOR
		return self.parent.select_one(locator).string

	@property
	def tags(self):
		locator = QuoteLocators.AUTHOR
		return [e.strings for e in self.parent.select(locator)]

	
