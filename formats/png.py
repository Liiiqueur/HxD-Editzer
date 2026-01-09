from formats.base import FileFormatAnalyzer
import struct
import zlib

class PNGAnalyser(FileFormatAnalyzer):
    name = "PNG"
    color = "#FFD1BA"
    signatures = ["89 50 4E 47 0D 0A 1A 0A", "49 45 4E 44 AE 42 60 82"]

    def extract_metadata(self, data: bytes) -> dict:
        meta = {}

        # ===== IHDR =====
        if data[12:16] != b'IHDR':
            return meta

        ihdr = data[16:29]

        meta["Width"] = struct.unpack(">I", ihdr[0:4])[0]
        meta["Height"] = struct.unpack(">I", ihdr[4:8])[0]
        meta["Bit Depth"] = ihdr[8]
        meta["Color Type"] = ihdr[9]
        meta["Compression"] = ihdr[10]
        meta["Filter"] = ihdr[11]
        meta["Interlace"] = ihdr[12]

        # ===== Chunk Loop =====
        offset = 8  # skip signature

        while offset < len(data):
            length = struct.unpack(">I", data[offset:offset+4])[0]
            ctype = data[offset+4:offset+8]
            cdata = data[offset+8:offset+8+length]

            if ctype == b'tEXt':
                key, _, value = cdata.partition(b'\x00')
                meta[f"tEXt:{key.decode(errors='ignore')}"] = value.decode(errors='ignore')

            elif ctype == b'zTXt':
                key, _, rest = cdata.partition(b'\x00')
                try:
                    text = zlib.decompress(rest[1:])
                    meta[f"zTXt:{key.decode(errors='ignore')}"] = text.decode(errors='ignore')
                except:
                    pass

            elif ctype == b'iTXt':
                parts = cdata.split(b'\x00', 5)
                if len(parts) >= 6:
                    key = parts[0].decode(errors='ignore')
                    text = parts[5].decode(errors='ignore')
                    meta[f"iTXt:{key}"] = text

            elif ctype == b'tIME':
                y, m, d, hh, mm, ss = struct.unpack(">HBBBBB", cdata)
                meta["Last Modified"] = f"{y:04}-{m:02}-{d:02} {hh:02}:{mm:02}:{ss:02}"

            elif ctype == b'pHYs':
                x, y, unit = struct.unpack(">IIB", cdata)
                meta["Resolution"] = f"{x}x{y} (unit={unit})"

            elif ctype == b'IEND':
                break

            offset += 12 + length

        return meta