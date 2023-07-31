from
from gtts import gTTs 



language  = "en"

text = "this is just a test to see what I have to do. This is what might work. Now I am just rambling on lol"

speech = gTTs(text=text, language=language, slow=False, tld='com.au')

speech.save('textToSpeech.mp3')