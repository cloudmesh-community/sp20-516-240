import os
import platform

class Hypervisor:
    def hyperv(self):
    """
    Switches on and off Hyper-V

    :param status: if true switches on the hypervisor
    """
        if platform.system() != 'Windows':
            return
        version = platform.system() + platform.release()
        if version != 'Windows 10':
            print(f"Your version is not supported. You run {version}")

