from ImageProcess.PrepareFrames.YImage import YImage


class ScoreNumbers:
	def __init__(self, scale):
		self.score_images = []
		scoreprefix = "-"
		score_x = scoreprefix + "x"
		score_percent = scoreprefix + "percent"
		score_dot = scoreprefix + "dot"
		for x in range(10):
			self.score_images.append(YImage(scoreprefix + str(x), scale, prefix="ScorePrefix"))

		self.score_percent = YImage(score_percent, scale, prefix="ScorePrefix")

		self.score_dot = YImage(score_dot, scale, prefix="ScorePrefix")

		self.score_x = YImage(score_x, scale, prefix="ScorePrefix")

		self.combo_images = []
		for x in range(10):
			self.combo_images.append(YImage(scoreprefix + str(x), scale, prefix="ComboPrefix"))
		self.combo_x = YImage(score_x, scale, prefix="ComboPrefix")
