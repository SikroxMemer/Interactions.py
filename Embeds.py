from interactions import Embed
import datetime

clear_embed = Embed(
    title='Clear',
    description=None,
    color=0x00FF00,
    timestamp=datetime.datetime.now(),
)

clear_embed.add_field(
    name='Clear Slash Command:',
    value=f"```yaml\nSuccess ! You've Cleared Your Messages.\n```"
)

clear_embed.set_image(
    url=str('https://media.giphy.com/media/26ybwwiZmci3DJdYs/giphy.gif')
)

clear_embed_error = Embed(
    title='❌ Error',
    description=None,
    color=0xFF0000,
    timestamp=datetime.datetime.now()
)

clear_embed_error.add_field(
    name='Amount Value Error !',
    value="```diff\n-Your value is too small,try a bigger value..\n```")

clear_embed_error.set_image(
    url=str('https://media.giphy.com/media/MZGN7KsGollqG3Gz6S/giphy.gif')
)

