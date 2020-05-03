from ImageProcess.PrepareFrames.YImage import YImage


default_circle_size = 128


def prepare_hitcirclenumber(diff, scale):
	"""
	:param diff:
	:param scale:
	:return: [PIL.Image]
	"""
	circle_radius = (54.4 - 4.48 * diff["CircleSize"]) * scale * 0.9
	hitcircle_number = []
	scale = circle_radius * 2 / default_circle_size
	for x in range(10):
		img = YImage("-{}".format(str(x)), scale, prefix="HitCirclePrefix")
		hitcircle_number.append(img.img)
	return hitcircle_number
