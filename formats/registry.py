from formats.png import PNGAnalyser
# from formats.jpg import JPGAnalyzer
# from formats.pdf import PDFAnalyzer

ANALYZERS = [
    PNGAnalyser(),
    # JPGAnalyzer(),
    # PDFAnalyzer(),
]

def detect_format(data: bytes):
    for analyzer in ANALYZERS:
        if analyzer.detect(data):
            return analyzer
    return None
