import math
import sys
from os import rename

import requests

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


r = requests.get(
    "https://prodentim.com/video.php?hop=boldapex&everclk=30bb32353b6749aaa17c820d888b8910&obclick=v1-171ce0781fff8ae5cad2cc09aa6a82a0-005922967abbb128b7724039d48393efc1-heygem3cg4yweljugqzdeljumm4tellcmq4ggljzgnrtkmbzmzrtcobvge"
)
print(r.status_code)
