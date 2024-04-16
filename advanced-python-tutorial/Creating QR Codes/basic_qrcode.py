# pip install segno

import segno

qrcode = segno.make_qr("hello, world!")
qrcode.save("basic_qrcode.png",
            scale=5,)

qrcode = segno.make_qr("hello, world!")
qrcode.save("transparent_qrcode.png",
            scale=5,
            dark="#00008bcc",
            light="#ccccffcc",
            quiet_zone="#d3d3d377",)

