COMMON_COLOR = "#FFD1BA"

FILE_SIGNATURES = {
    # ===== Image =====
    "PNG": {
        "sigs": ["89 50 4E 47 0D 0A 1A 0A", "49 45 4E 44"],
        "color": COMMON_COLOR
    },
    "JPG": {
        "sigs": ["FF D8 FF"],
        "color": COMMON_COLOR
    },
    "GIF": {
        "sigs": ["47 49 46 38 37 61", "47 49 46 38 39 61"],
        "color": COMMON_COLOR
    },
    "BMP": {
        "sigs": ["42 4D"],
        "color": COMMON_COLOR
    },
    "TIFF": {
        "sigs": ["49 49 2A 00", "4D 4D 00 2A"],
        "color": COMMON_COLOR
    },
    "WEBP": {
        "sigs": ["52 49 46 46", "57 45 42 50"],
        "color": COMMON_COLOR
    },

    # ===== Archive =====
    "ZIP": {
        "sigs": ["50 4B 03 04", "50 4B 05 06", "50 4B 07 08"],
        "color": COMMON_COLOR
    },
    "RAR": {
        "sigs": ["52 61 72 21 1A 07"],
        "color": COMMON_COLOR
    },
    "7Z": {
        "sigs": ["37 7A BC AF 27 1C"],
        "color": COMMON_COLOR
    },
    "GZIP": {
        "sigs": ["1F 8B"],
        "color": COMMON_COLOR
    },
    "TAR": {
        "sigs": ["75 73 74 61 72"],
        "color": COMMON_COLOR
    },

    # ===== Document =====
    "PDF": {
        "sigs": ["25 50 44 46"],
        "color": COMMON_COLOR
    },
    "DOC": {
        "sigs": ["D0 CF 11 E0 A1 B1 1A E1"],
        "color": COMMON_COLOR
    },
    "DOCX": {
        "sigs": ["50 4B 03 04"],
        "color": COMMON_COLOR
    },
    "XLS": {
        "sigs": ["D0 CF 11 E0 A1 B1 1A E1"],
        "color": COMMON_COLOR
    },
    "XLSX": {
        "sigs": ["50 4B 03 04"],
        "color": COMMON_COLOR
    },
    "PPT": {
        "sigs": ["D0 CF 11 E0 A1 B1 1A E1"],
        "color": COMMON_COLOR
    },

    # ===== Audio =====
    "MP3": {
        "sigs": ["49 44 33", "FF FB"],
        "color": COMMON_COLOR
    },
    "WAV": {
        "sigs": ["52 49 46 46", "57 41 56 45"],
        "color": COMMON_COLOR
    },
    "FLAC": {
        "sigs": ["66 4C 61 43"],
        "color": COMMON_COLOR
    },
    "OGG": {
        "sigs": ["4F 67 67 53"],
        "color": COMMON_COLOR
    },

    # ===== Video =====
    "MP4": {
        "sigs": ["00 00 00 18 66 74 79 70"],
        "color": COMMON_COLOR
    },
    "AVI": {
        "sigs": ["52 49 46 46", "41 56 49 20"],
        "color": COMMON_COLOR
    },
    "MKV": {
        "sigs": ["1A 45 DF A3"],
        "color": COMMON_COLOR
    },
    "MOV": {
        "sigs": ["00 00 00 14 66 74 79 70 71 74"],
        "color": COMMON_COLOR
    },

    # ===== Executable / Binary =====
    "EXE": {
        "sigs": ["4D 5A"],
        "color": COMMON_COLOR
    },
    "DLL": {
        "sigs": ["4D 5A"],
        "color": COMMON_COLOR
    },
    "ELF": {
        "sigs": ["7F 45 4C 46"],
        "color": COMMON_COLOR
    },

    # ===== Disk / Forensic =====
    "ISO": {
        "sigs": ["43 44 30 30 31"],
        "color": COMMON_COLOR
    },
    "VHD": {
        "sigs": ["63 6F 6E 65 63 74 69 78"],
        "color": COMMON_COLOR
    },
    "VMDK": {
        "sigs": ["4B 44 4D"],
        "color": COMMON_COLOR
    },

    # ===== Database =====
    "SQLITE": {
        "sigs": ["53 51 4C 69 74 65 20 66 6F 72 6D 61 74 20 33 00"],
        "color": COMMON_COLOR
    },

    # ===== Text / Script =====
    "XML": {
        "sigs": ["3C 3F 78 6D 6C"],
        "color": COMMON_COLOR
    },
    "HTML": {
        "sigs": ["3C 21 44 4F 43 54 59 50 45"],
        "color": COMMON_COLOR
    }
}