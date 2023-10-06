import string
from ctypes import windll
from ctypes import wintypes as w
import ctypes


def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter + ":\\")
        bitmask >>= 1
    return drives


def get_info(disks):
    dll = ctypes.WinDLL('kernel32', use_last_error=True)
    dll.GetVolumeInformationW.argtypes = w.LPCWSTR, w.LPWSTR, w.DWORD, w.LPDWORD, w.LPDWORD, w.LPDWORD, w.LPWSTR, w.DWORD
    dll.GetVolumeInformationW.restype = w.BOOL

    volumeNameBuffer = ctypes.create_unicode_buffer(w.MAX_PATH + 1)
    fileSystemNameBuffer = ctypes.create_unicode_buffer(w.MAX_PATH + 1)
    serial_number = w.DWORD()
    max_component_length = w.DWORD()
    file_system_flags = w.DWORD()

    dll.GetDiskFreeSpaceExW.argtypes = (ctypes.c_wchar_p,) + (ctypes.POINTER(ctypes.c_ulonglong),) * 3
    result = []
    for disk in disks:
        _ = ctypes.c_ulonglong()
        total = ctypes.c_ulonglong()
        free = ctypes.c_ulonglong()
        dll.GetDiskFreeSpaceExW(disk, ctypes.byref(_), ctypes.byref(total), ctypes.byref(free))
        used = total.value - free.value
        dll.GetVolumeInformationW(disk,
                                  volumeNameBuffer, ctypes.sizeof(volumeNameBuffer),
                                  ctypes.byref(serial_number),
                                  ctypes.byref(max_component_length),
                                  ctypes.byref(file_system_flags),
                                  fileSystemNameBuffer, ctypes.sizeof(fileSystemNameBuffer))

        mount_point = disk
        disk_label = volumeNameBuffer.value
        fs_type = fileSystemNameBuffer.value
        max_length = max_component_length.value
        serial = serial_number.value

        result.append(
                str(mount_point) + " метка тома - '" + str(disk_label) + "' тип файловой системы - " + str(
                fs_type) + " размер - " + str(max_length) + " серия - " + str(serial) + " использовано места - " + str(
                int(used / 1024 / 1024 / 1024)) + "Gb свободно - " + str(
                int(free.value / 1024 / 1024 / 1024)) + "Gb всего - " + str(
                int(total.value / 1024 / 1024 / 1024)) + "Gb")
    return result


for info in get_info(get_drives()):
    print(info)
