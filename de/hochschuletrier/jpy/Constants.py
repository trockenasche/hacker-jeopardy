__author__ = 'miko'
from tkFont import Font


class Constants:
	SCREENW = 0
	SCREENH = 0
	COLORS = ["red", "green", "purple", "brown", "black", "yellow"]


class Fonts:
	MONEY_BIG = 0
	MONEY_SMALL = 0
	MONEY_MEDIUM = 0
	SYSTEM_REGULAR = 0
	SYSTEM_BIG = 0
	USER_LABEL_NAME = 0
	USER_LABEL_NAME_BIG = 0

	@staticmethod
	def construct():
		Fonts.USER_LABEL_NAME = Font(family="Ubuntu", size=Fonts.sizing(18), weight="normal")
		Fonts.USER_LABEL_NAME_BIG = Font(family="Ubuntu", size=Fonts.sizing(30), weight="normal")
		Fonts.MONEY_BIG = Font(family="Swiss911 UCm BT", size=Fonts.sizing(65), weight="normal")
		Fonts.MONEY_SMALL = Font(family="Swiss911 UCm BT", size=Fonts.sizing(20), weight="normal")
		Fonts.SYSTEM_BIG = Font(family="Times New Roman", size=Fonts.sizing(45), weight="normal")
		Fonts.SYSTEM_REGULAR = Font(family="Times New Roman", size=Fonts.sizing(25), weight="normal")
		Fonts.MONEY_MEDIUM = Font(family="Swiss911 UCm BT", size=Fonts.sizing(38), weight="normal")

	@staticmethod
	def sizing(percentage):
		size = int(round(Constants.SCREENH / 7 * float(percentage) / 100))
		return size
