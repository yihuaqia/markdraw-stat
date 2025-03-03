"""Contains the details of the marks for the different metro modules"""


# Metrology modules available
METRO_MODULES = {"CAXX":  {"metrology": "Alignment",
                           "module": "Canon",
                           "CAD": "MarkDraw",
                           "more": None  # Can add extra info here related to the module, etc.
                           },
                 "CA4X": {"metrology": "Alignment",
                          "module": "Canon4x",
                          "CAD": "MarkDraw",  # CAD tool to be used to draw the mark
                          "more": None  # Can add extra info here related to the module, etc.
                          },
                 "CA2X": {"metrology": "Alignment",
                          "module": "Canon2x",
                          "CAD": "MarkDraw",  # CAD tool to be used to draw the mark
                          "more": None  # Can add extra info here related to the module, etc.
                          },
                 "NIK": {"metrology": "Alignment",
                         "module": "Nikon",
                         "CAD": "NikonCode",  # CAD tool to be used to draw the mark
                         "more": None  # Can add extra info here related to the module, etc.
                         },
                 "uEGA": {"metrology": "Alignment",
                          "module": "Nikon",
                          "CAD": "NikonCode",
                          "more": None
                          },
                 "ASML": {"metrology": "Alignment",
                          "module": "ASML",
                          "CAD": "UMG",  # CAD tool to be used to draw the mark
                          "more": None  # Can add extra info here related to the module, etc.
                          },
                 "DBO": {"metrology": "Overlay",
                         "module": "DBO",
                         "CAD": "UMG",  # CAD tool to be used to draw the mark
                         "more": None  # Can add extra info here related to the module, etc.
                         }
                 }

# The following dictionary contains the details of the marks for the Canon module
CANON_CATALOG = {
    "CAXXID": {  # Ids mark
        "module": "CAXX",
        "metro_details": METRO_MODULES["CAXX"],
        "mark_shape": "",
        "mark_style": "",
        "mark_type": "ID",
        "mark_orientation": "id",
        "corduroy": {"style": "ID",
                     "orientation": None,
                     "lpp": None,
                     "cd": None,
                     "pitch": None,
                     "pullback": None,
                     },
        "CAD_info": {"tool": "MarkDraw",  # Custom filler flow
                     "function_sequence": ("m0", "m17")}
    },
    "CAXXD1": {  # Dummy mark
        "module": "CAXX",
        "metro_details": METRO_MODULES["CAXX"],
        "mark_shape": "",
        "mark_style": "",
        "mark_type": "DUMMY",
        "mark_orientation": "dummmy",
        "corduroy": {"style": "FILLER",
                     "orientation": "ALL",
                     "lpp": None,
                     "cd": None,
                     "pitch": None,
                     "pullback": None,
                     },
        "CAD_info": {"tool": "MarkDraw",  # Custom filler flow
                     "function_sequence": ("m0", "m21")}
    },
    "CAXXD2": {  # Dummy mark
            "module": "CAXX",
            "metro_details": METRO_MODULES["CAXX"],
            "mark_shape": "",
            "mark_style": "",
            "mark_type": "DUMMY",
            "mark_orientation": "dummmy",
            "corduroy": {"style": "FILLER",
                         "orientation": "ALL",
                         "lpp": None,
                         "cd": None,
                         "pitch": None,
                         "pullback": None,
                         },
            "CAD_info": {"tool": "MarkDraw",  # Make FDR dummy
                         "function_sequence": ("m0", "m20")}
        },
    "CAXXD3": {  # Diagonal dummy mark
        "module": "CAXX",
        "metro_details": METRO_MODULES["CAXX"],
        "mark_shape": "",
        "mark_style": "",
        "mark_type": "DUMMY",
        "mark_orientation": "dummmy",
        "corduroy": {"style": "DIAGONAL",
                     "orientation": "45",
                     "lpp": None,
                     "cd": None,
                     "pitch": None,
                     "pullback": None,
                     },
        "CAD_info": {"tool": "MarkDraw",  # Make FDR dummy
                     "function_sequence": ("m0", "m15")}
    },
    "CAXXD4": {  # Diagonal dummy mark
        "module": "CAXX",
        "metro_details": METRO_MODULES["CAXX"],
        "mark_shape": "",
        "mark_style": "",
        "mark_type": "DUMMY",
        "mark_orientation": "dummmy",
        "corduroy": {"style": "DIAGONAL",
                     "orientation": "135",
                     "lpp": None,
                     "cd": None,
                     "pitch": None,
                     "pullback": None,
                     },
        "CAD_info": {"tool": "MarkDraw",  # Make FDR dummy
                     "function_sequence": ("m0", "m15")}
    },
    "CAXXD5": {  # Diagonal dummy mark
        "module": "CAXX",
        "metro_details": METRO_MODULES["CAXX"],
        "mark_shape": "",
        "mark_style": "",
        "mark_type": "DUMMY",
        "mark_orientation": "dummmy",
        "corduroy": {"style": "MANHATTAN",
                     "orientation": "H",
                     "lpp": None,
                     "cd": None,
                     "pitch": None,
                     "pullback": None,
                     },
        "CAD_info": {"tool": "MarkDraw",  # Make FDR dummy
                     "function_sequence": ("m0", "m14")}
    },
    "CAXXD6": {  # Diagonal dummy mark
        "module": "CAXX",
        "metro_details": METRO_MODULES["CAXX"],
        "mark_shape": "",
        "mark_style": "",
        "mark_type": "DUMMY",
        "mark_orientation": "dummmy",
        "corduroy": {"style": "MANHATTAN",
                     "orientation": "V",
                     "lpp": None,
                     "cd": None,
                     "pitch": None,
                     "pullback": None,
                     },
        "CAD_info": {"tool": "MarkDraw",  # Make FDR dummy
                     "function_sequence": ("m0", "m14")}
    },
    "CA4X1": {
            "module": "CA4X",
            "metro_details": METRO_MODULES["CA4X"],
            "mark_shape": "BOX_A",
            "mark_style": "XY4",
            "mark_type": "FINE ALIGNMENT",
            "mark_orientation": "D",
            "corduroy": {"style": "MANHATTAN",
                         "orientation": "V",
                         "lpp": None,
                         "cd": None,
                         "pitch": None,
                         "pullback": None,
                         },
            "CAD_info": {"tool": "MarkDraw",
                         "function_sequence": ("m0", "m1", "m14", "m10")}
    },
    "CA4X2": {
            "module": "CA4X",
            "metro_details": METRO_MODULES["CA4X"],
            "mark_shape": "POUND",
            "mark_style": "XY4",
            "mark_type": "FINE ALIGNMENT",
            "mark_orientation": "D",
            "corduroy": {"style": "MANHATTAN",
                         "orientation": "V",
                         "lpp": None,
                         "cd": None,
                         "pitch": None,
                         "pullback": None,
                         },
            "CAD_info": {"tool": "MarkDraw",
                         "function_sequence": ("m0", "m1", "m14", "m10")}
    },
    "CA4X3": {
        "module": "CA4X",
        "metro_details": METRO_MODULES["CA4X"],
        "mark_shape": "TOUCH",
        "mark_style": "TV03T",
        "mark_type": "COARSE ALIGNMENT",
        "mark_orientation": "D",
        "corduroy": {"style": "MANHATTAN",
                     "orientation": "V",
                     "lpp": None,
                     "cd": None,
                     "pitch": None,
                     "pullback": None,
                     },
        "CAD_info": {"tool": "MarkDraw",
                     "function_sequence": ("m0", "m6", "m14", "m10")}
    },
    "CA4X4": {
        "module": "CA4X",
        "metro_details": METRO_MODULES["CA4X"],
        "mark_shape": "CROSS",
        "mark_style": "TV03C",
        "mark_type": "COARSE ALIGNMENT",
        "mark_orientation": "D",
        "corduroy": {"style": "MANHATTAN",
                     "orientation": "V",
                     "lpp": None,
                     "cd": None,
                     "pitch": None,
                     "pullback": None,
                     },
        "CAD_info": {"tool": "MarkDraw",
                     "function_sequence": ("m0", "m7", "m14", "m10")}
    },
    "CA4X5": {
        "module": "CA4X",
        "metro_details": METRO_MODULES["CA4X"],
        "mark_shape": "BOX_A",
        "mark_style": "XY4",
        "mark_type": "FINE ALIGNMENT",
        "mark_orientation": "D",
        "corduroy": {"style": "MANHATTAN",
                     "orientation": "H",
                     "lpp": None,
                     "cd": None,
                     "pitch": None,
                     "pullback": None,
                     },
        "CAD_info": {"tool": "MarkDraw",
                     "function_sequence": ("m0", "m1", "m14", "m10")}
    },
    "CA4X6": {
        "module": "CA4X",
        "metro_details": METRO_MODULES["CA4X"],
        "mark_shape": "POUND",
        "mark_style": "XY4",
        "mark_type": "FINE ALIGNMENT",
        "mark_orientation": "D",
        "corduroy": {"style": "MANHATTAN",
                     "orientation": "H",
                     "lpp": None,
                     "cd": None,
                     "pitch": None,
                     "pullback": None,
                     },
        "CAD_info": {"tool": "MarkDraw",
                     "function_sequence": ("m0", "m1", "m14", "m10")}
    },
    "CA4X7": {
        "module": "CA4X",
        "metro_details": METRO_MODULES["CA4X"],
        "mark_shape": "TOUCH",
        "mark_style": "TV03T",
        "mark_type": "COARSE ALIGNMENT",
        "mark_orientation": "D",
        "corduroy": {"style": "MANHATTAN",
                     "orientation": "H",
                     "lpp": None,
                     "cd": None,
                     "pitch": None,
                     "pullback": None,
                     },
        "CAD_info": {"tool": "MarkDraw",
                     "function_sequence": ("m0", "m6", "m14", "m10")}
    },
    "CA4X8": {
        "module": "CA4X",
        "metro_details": METRO_MODULES["CA4X"],
        "mark_shape": "CROSS",
        "mark_style": "TV03C",
        "mark_type": "COARSE ALIGNMENT",
        "mark_orientation": "D",
        "corduroy": {"style": "MANHATTAN",
                     "orientation": "H",
                     "lpp": None,
                     "cd": None,
                     "pitch": None,
                     "pullback": None,
                     },
        "CAD_info": {"tool": "MarkDraw",
                     "function_sequence": ("m0", "m7", "m14", "m10")}
    },
    "CA4X9": {
        "module": "CA4X",
        "metro_details": METRO_MODULES["CA4X"],
        "mark_shape": "BOX_A",
        "mark_style": "XY4",
        "mark_type": "FINE ALIGNMENT",
        "mark_orientation": "D",
        "corduroy": {"style": "ZONAL",
                     "orientation": "ALL",
                     "lpp": None,
                     "cd": None,
                     "pitch": None,
                     "pullback": None,
                     },
        "CAD_info": {"tool": "MarkDraw",
                     "function_sequence": ("m13", "m0", "m1", "m10")}
    },
    "CA2X1": {
            "module": "CA2X",
            "metro_details": METRO_MODULES["CA2X"],
            "mark_shape": "BOX_A",
            "mark_style": "XY4",
            "mark_type": "FINE ALIGNMENT",
            "mark_orientation": "D",
            "corduroy": {"style": "MANHATTAN",
                         "orientation": "V",
                         "lpp": None,
                         "cd": None,
                         "pitch": None,
                         "pullback": None,
                         },
            "CAD_info": {"tool": "MarkDraw",
                         "function_sequence": ("m0", "m1", "m14", "m10")}
    },
    "CA2X2": {
            "module": "CA2X",
            "metro_details": METRO_MODULES["CA2X"],
            "mark_shape": "POUND",
            "mark_style": "XY4",
            "mark_type": "FINE ALIGNMENT",
            "mark_orientation": "D",
            "corduroy": {"style": "MANHATTAN",
                         "orientation": "V",
                         "lpp": None,
                         "cd": None,
                         "pitch": None,
                         "pullback": None,
                         },
            "CAD_info": {"tool": "MarkDraw",
                         "function_sequence": ("m0", "m1", "m14", "m10")}
    },
    "CA2X3": {
        "module": "CA2X",
        "metro_details": METRO_MODULES["CA2X"],
        "mark_shape": "TOUCH",
        "mark_style": "TV03T",
        "mark_type": "COARSE ALIGNMENT",
        "mark_orientation": "D",
        "corduroy": {"style": "MANHATTAN",
                     "orientation": "V",
                     "lpp": None,
                     "cd": None,
                     "pitch": None,
                     "pullback": None,
                     },
        "CAD_info": {"tool": "MarkDraw",
                     "function_sequence": ("m0", "m6", "m14", "m10")}
    },
    "CA2X4": {
        "module": "CA2X",
        "metro_details": METRO_MODULES["CA2X"],
        "mark_shape": "CROSS",
        "mark_style": "TV03C",
        "mark_type": "COARSE ALIGNMENT",
        "mark_orientation": "D",
        "corduroy": {"style": "MANHATTAN",
                     "orientation": "V",
                     "lpp": None,
                     "cd": None,
                     "pitch": None,
                     "pullback": None,
                     },
        "CAD_info": {"tool": "MarkDraw",
                     "function_sequence": ("m0", "m7", "m14", "m10")}
    },
    "CA2X5": {
        "module": "CA2X",
        "metro_details": METRO_MODULES["CA2X"],
        "mark_shape": "BOX_A",
        "mark_style": "XY4",
        "mark_type": "FINE ALIGNMENT",
        "mark_orientation": "D",
        "corduroy": {"style": "MANHATTAN",
                     "orientation": "H",
                     "lpp": None,
                     "cd": None,
                     "pitch": None,
                     "pullback": None,
                     },
        "CAD_info": {"tool": "MarkDraw",
                     "function_sequence": ("m0", "m1", "m14", "m10")}
    },
    "CA2X6": {
        "module": "CA2X",
        "metro_details": METRO_MODULES["CA2X"],
        "mark_shape": "POUND",
        "mark_style": "XY4",
        "mark_type": "FINE ALIGNMENT",
        "mark_orientation": "D",
        "corduroy": {"style": "MANHATTAN",
                     "orientation": "H",
                     "lpp": None,
                     "cd": None,
                     "pitch": None,
                     "pullback": None,
                     },
        "CAD_info": {"tool": "MarkDraw",
                     "function_sequence": ("m0", "m1", "m14", "m10")}
    },
    "CA2X7": {
        "module": "CA2X",
        "metro_details": METRO_MODULES["CA2X"],
        "mark_shape": "TOUCH",
        "mark_style": "TV03T",
        "mark_type": "COARSE ALIGNMENT",
        "mark_orientation": "D",
        "corduroy": {"style": "MANHATTAN",
                     "orientation": "H",
                     "lpp": None,
                     "cd": None,
                     "pitch": None,
                     "pullback": None,
                     },
        "CAD_info": {"tool": "MarkDraw",
                     "function_sequence": ("m0", "m6", "m14", "m10")}
    },
    "CA2X8": {
        "module": "CA2X",
        "metro_details": METRO_MODULES["CA2X"],
        "mark_shape": "CROSS",
        "mark_style": "TV03C",
        "mark_type": "COARSE ALIGNMENT",
        "mark_orientation": "D",
        "corduroy": {"style": "MANHATTAN",
                     "orientation": "H",
                     "lpp": None,
                     "cd": None,
                     "pitch": None,
                     "pullback": None,
                     },
        "CAD_info": {"tool": "MarkDraw",
                     "function_sequence": ("m0", "m7", "m14", "m10")}
    },
    "CA2X9": {
        "module": "CA2X",
        "metro_details": METRO_MODULES["CA2X"],
        "mark_shape": "BOX_A",
        "mark_style": "XY4",
        "mark_type": "FINE ALIGNMENT",
        "mark_orientation": "D",
        "corduroy": {"style": "EMPTY",
                     "orientation": None,
                     "lpp": None,
                     "cd": None,
                     "pitch": None,
                     "pullback": None,
                     },
        "CAD_info": {"tool": "MarkDraw",
                     "function_sequence": ("m0", "m1")}
    },
    "CA2X10": {
        "module": "CA2X",
        "metro_details": METRO_MODULES["CA2X"],
        "mark_shape": "POUND",
        "mark_style": "XY4",
        "mark_type": "FINE ALIGNMENT",
        "mark_orientation": "D",
        "corduroy": {"style": "EMPTY",
                     "orientation": None,
                     "lpp": None,
                     "cd": None,
                     "pitch": None,
                     "pullback": None,
                     },
        "CAD_info": {"tool": "MarkDraw",
                     "function_sequence": ("m0", "m1")}
    },
    "CA2X11": {
        "module": "CA2X",
        "metro_details": METRO_MODULES["CA2X"],
        "mark_shape": "TOUCH",
        "mark_style": "TV03T",
        "mark_type": "COARSE ALIGNMENT",
        "mark_orientation": "D",
        "corduroy": {"style": "EMPTY",
                     "orientation": None,
                     "lpp": None,
                     "cd": None,
                     "pitch": None,
                     "pullback": None,
                     },
        "CAD_info": {"tool": "MarkDraw",
                     "function_sequence": ("m0", "m6")}
    },
    "CA2X12": {
        "module": "CA2X",
        "metro_details": METRO_MODULES["CA2X"],
        "mark_shape": "CROSS",
        "mark_style": "TV03C",
        "mark_type": "COARSE ALIGNMENT",
        "mark_orientation": "D",
        "corduroy": {"style":  "EMPTY",
                     "orientation": None,
                     "lpp": None,
                     "cd": None,
                     "pitch": None,
                     "pullback": None,
                     },
        "CAD_info": {"tool": "MarkDraw",
                     "function_sequence": ("m0", "m7")}
    },
    "CA2X13": {
        "module": "CA2X",
        "metro_details": METRO_MODULES["CA2X"],
        "mark_shape": "BOX_A",
        "mark_style": "XY4",
        "mark_type": "FINE ALIGNMENT",
        "mark_orientation": "D",
        "corduroy": {"style": "ZONAL",
                     "orientation": "ALL",
                     "lpp": None,
                     "cd": None,
                     "pitch": None,
                     "pullback": None,
                     },
        "CAD_info": {"tool": "MarkDraw",
                     "function_sequence": ("m0", "m1", "m13")}
    },
    "CA2X14": {
        "module": "CA2X",
        "metro_details": METRO_MODULES["CA2X"],
        "mark_shape": "LINE",
        "mark_style": "X04",
        "mark_type": "FINE ALIGNMENT",
        "mark_orientation": "V",
        "corduroy": {"style": "EMPTY",
                     "orientation": None,
                     "lpp": None,
                     "cd": None,
                     "pitch": None,
                     "pullback": None,
                     },
        "CAD_info": {"tool": "MarkDraw",
                     "function_sequence": ("m0", "m3")}
    },
    "CA2X15": {
        "module": "CA2X",
        "metro_details": METRO_MODULES["CA2X"],
        "mark_shape": "LINE",
        "mark_style": "Y04",
        "mark_type": "FINE ALIGNMENT",
        "mark_orientation": "H",
        "corduroy": {"style": "EMPTY",
                     "orientation": None,
                     "lpp": None,
                     "cd": None,
                     "pitch": None,
                     "pullback": None,
                     },
        "CAD_info": {"tool": "MarkDraw",
                     "function_sequence": ("m0", "m3")}
    },
    "CA2X16": {
        "module": "CA2X",
        "metro_details": METRO_MODULES["CA2X"],
        "mark_shape": "BOX_C",
        "mark_style": "XY4",
        "mark_type": "FINE ALIGNMENT",
        "mark_orientation": "D",
        "corduroy": {"style": "EMPTY",
                     "orientation": None,
                     "lpp": None,
                     "cd": None,
                     "pitch": None,
                     "pullback": None,
                     },
        "CAD_info": {"tool": "MarkDraw",
                     "function_sequence": ("m0", "m5", "m5")}
    },
    "CA2X17": {
        "module": "CA2X",
        "metro_details": METRO_MODULES["CA2X"],
        "mark_shape": "TOUCH",
        "mark_style": "TV03T",
        "mark_type": "COARSE ALIGNMENT",
        "mark_orientation": "D",
        "corduroy": {"style": "ZONAL SWIRL",
                     "orientation": "ALL",
                     "lpp": None,
                     "cd": None,
                     "pitch": None,
                     "pullback": None,
                     },
        "CAD_info": {"tool": "MarkDraw",
                     "function_sequence": ("m13", "m0", "m16", "m6", "m6", "m12", "m6", "m12", "m10")}
    },
    "CA2X18": {
        "module": "CA2X",
        "metro_details": METRO_MODULES["CA2X"],
        "mark_shape": "CROSS",
        "mark_style": "TV03C",
        "mark_type": "COARSE ALIGNMENT",
        "mark_orientation": "D",
        "corduroy": {"style": "ZONAL SWIRL",
                     "orientation": "ALL",
                     "lpp": None,
                     "cd": None,
                     "pitch": None,
                     "pullback": None,
                     },
        "CAD_info": {"tool": "MarkDraw",
                     "function_sequence": ("m13", "m0", "m16", "m7", "m7", "m12", "m7", "m12", "m10")}
    },
    "CA2X19": {
        "module": "CA2X",
        "metro_details": METRO_MODULES["CA2X"],
        "mark_shape": "BOX_A",
        "mark_style": "XY4",
        "mark_type": "FINE ALIGNMENT",
        "mark_orientation": "D",
        "corduroy": {"style": "ZONAL SWIRL",
                     "orientation": "ALL",
                     "lpp": None,
                     "cd": None,
                     "pitch": None,
                     "pullback": None,
                     },
        "CAD_info": {"tool": "MarkDraw",
                     "function_sequence": ("m0", "m1", "m13")}
    },
}
