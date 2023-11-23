from emoji import emojize


class Emo:
	# коды эмодзи можно взять тут https://emojio.ru/smileys-emotion.html
	# или тут https://apps.timwhitlock.info/emoji/tables/unicode

	@staticmethod
	def emoj(smile):
		return emojize(smile, variant="emoji_type")

	ruble = emoj("₽")
	big_smile = emoj(":grinning_face_with_big_eyes:")
	hugs = emoj(":smiling_face_with_open_hands:")
	hand_over_mouth = emoj(":face_with_hand_over_mouth:")
	hundred = emoj(":hundred_points:")
	quiet = emoj(":shushing_face:")
	heart = emoj("❤️")
	omg_cat_face = emoj("🙀")
	red_exclamation = emoj("❗️")
	nerd_face = emoj(":nerd_face:")
	sunglasses = emoj("😎")
	explosive_head = emoj("🤯")
	hi = emoj("👋")
	just_smile = emoj("🙂")
