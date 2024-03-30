# pip install comtypes pycaw

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume, ISimpleAudioVolume

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

current = volume.GetMasterVolumeLevel()
volume.SetMasterVolumeLevel(current + 6.0, None)

volume.SetMasterVolumeLevel(0.0, None)
volume.SetMute(1, None)

sessions = AudioUtilities.GetAllSessions()

for session in sessions:
    volume = session._ctl.QueryInterface(ISimpleAudioVolume)
    if session.Process:
        print(session.Process.name())
    if session.Process and session.Process.name() == "obs64.exe":
        volume.SetMasterVolumeLevel(0.5, None)

