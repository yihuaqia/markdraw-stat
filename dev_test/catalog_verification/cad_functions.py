"""CAD functions for the cataloger."""

# MarkDraw functions
MARK_DRAW_FOO = {
    "m0": {
        "name": "StartLayoutAssembler",
        "args": [
            "Library.string",
            "CellName.string",
            "OpenCellViewMode.string",
            "CellSizeX.float",
            "CellSizeY.float",
            "CenterX.float",
            "CenterY.float",
            "Category.string"
        ]
    },
    "m1": {
        "name": "xy_canon",
        "args": [
            "cv.cvid",
            "lpp.lpp",
            "xy_cds.points",
            "xy_lengths.points",
            "xy_distance.points",
            "stepping.list",
            "shift.boolean",
            "varname.declare"
        ]
    },
    "m2": {
        "name": "spa_canon",
        "args": [
            "cv.cvid",
            "lpp.lpp",
            "cd.float",
            "length.float",
            "spacing.float",
            "stepping.list",
            "orientation.string",
            "varname.declare"
        ]
    },
    "m3": {
        "name": "fa_canon",
        "args": [
            "cv.cvid",
            "lpp.lpp",
            "cd.float",
            "length.float",
            "spacing.float",
            "stepping.list",
            "orientation.string",
            "delta.float",
            "doublet_space.float",
            "varname.declare"
        ]
    },
    "m4": {
        "name": "hash_canon",
        "args": [
            "cv.cvid",
            "lpp.lpp",
            "cd.float",
            "pitch.float",
            "height.float",
            "width.float",
            "varname.declare"
        ]
    },
    "m5": {
        "name": "center_canon",
        "args": [
            "cv.cvid",
            "lpp.lpp",
            "cd.float",
            "spacing.float",
            "varname.declare"
        ]
    },
    "m6": {
        "name": "tvpa_canon",
        "args": [
            "cv.cvid",
            "lpp.lpp",
            "cd.float",
            "box_space.float",
            "cross_width.float",
            "cross_height.float",
            "varname.declare"
        ]
    },
    "m7": {
        "name": "chopped_tvpa_canon",
        "args": [
            "cv.cvid",
            "lpp.lpp",
            "box_side.float",
            "chunk_height.float",
            "num_chunks.int",
            "center_delta.float",
            "varname.declare"
        ]
    },
    "m8": {
        "name": "bedazzle",
        "args": [
            "cv.cvid",
            "shapes.list",
            "lpp.lpp",
            "circle_lpp.lpp",
            "style.string"
        ]
    },
    "m9": {
        "name": "bool_and",
        "args": [
            "cv.cvid",
            "in1_lpp.lpp",
            "in2_lpp.lpp",
            "out_lpp.lpp"
        ]
    },
    "m10": {
        "name": "bool_and_not",
        "args": [
            "cv.cvid",
            "in1_lpp.lpp",
            "in2_lpp.lpp",
            "out_lpp.lpp"
        ]
    },
    "m11": {
        "name": "bool_or",
        "args": [
            "cv.cvid",
            "in1_lpp.lpp",
            "in2_lpp.lpp",
            "out_lpp.lpp"
        ]
    },
    "m12": {
        "name": "shape_size",
        "args": [
            "cv.cvid",
            "lpp.lpp",
            "left_size.float",
            "bottom_size.float",
            "right_size.float",
            "top_size.float",
            "keep_shapes.boolean"
        ]
    },
    "m13": {
        "name": "zonal_background",
        "args": [
            "library.string",
            "cell_name.string",
            "cell_size.points",
            "lpp.lpp",
            "cd.float",
            "pitch.float",
            "swirl.boolean"
        ]
    },
    "m14": {
        "name": "create_gratings",
        "args": [
            "cv.cvid",
            "lpp.lpp",
            "bbox.bbox",
            "cd.float",
            "pitch.float",
            "orientation.string",
            "varname.declare"
        ]
    },
    "m15": {
        "name": "diagonal_gratings",
        "args": [
            "cv.cvid",
            "lpp.lpp",
            "angle.int",
            "cd.float",
            "pitch.float",
            "min_length.float",
            "offset.boolean",
            "exclude_distance.points"
        ]
    },
    "m16": {
        "name": "create_rectangle",
        "args": [
            "cv.cvid",
            "lpp.lpp",
            "bbox.bbox"
        ]
    },
    "m17": {
        "name": "create_id",
        "args": [
            "cv.cvid",
            "idtype.string",
            "layers.layers"
        ]
    },
    "m18": {
        "name": "create_instance",
        "args": [
            "cv.cvid",
            "master_lib.string",
            "master_cell.string",
            "master_view.string",
            "inst_name.string",
            "origin.points",
            "orientation.string"
        ]
    },
    "m19": {
        "name": "flatten_instances",
        "args": [
            "cv.cvid",
            " flat_levels.int"
        ]
    },
    "m20": {
        "name": "make_fdr_dummy",
        "args": [
            "cv.cvid",
            "dummy_lib.string",
            "dummy_name.string",
            "fdr_toplib.string",
            "fdr_topcell.string"
        ]
    },
    "m21": {
        "name": "custom_filler_flow",
        "args": [
            "library.string",
            "cell.string",
            "filler_cell_lib.string",
            "filler_cell_name.string",
            "fill_extents_lpp.string",
            "keep_away_lpp.string",
            "filler_cell_fill_extents_lpp.string",
            "overlay_mode.string"
        ]
    }
}
