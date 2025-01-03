import bpy
from .ST_0_start.OT_start_modeling import OTStartModelingTT, OTStartFromExistingTT
from .ST_10_import_scan.OT_import_scan import OTImportScanTT
from .ST_20_indicate.OT_indicate_patella import OTMoveScanTT
from .ST_30_clean_up.OT_clean_up import OTCleanUpTT
from .ST_40_verify_clean_up.OT_verify_clean_up import (
    OTHighlightNonManifoldTT,
    OTFillNonManifoldTT,
    OTDeleteNonManifoldTT,
    OTApproveCleanUpTT,
)
from .ST_50_rotate.OT_rotate_scan import OTSaveRotationTT
from .ST_60_circumferences.OT_circumferences import (
    OTCircumferenceTT,
    OTCircumferencesCalcTT,
    OTCircumferencesDoneTT,
    OTCircumferencesHighlightTT
)
from .ST_70_push_pull_smooth.OT_push_pull_smooth import (
    OTPushPullRegionTT,
    OTSmoothRegionTT,
    OTFreeSculptCheckpointTT,
    OTPushPullSmoothDoneTT
)
from .ST_80_pull_bottom.OT_pull_bottom import OTPullBottomTT, OTPullBottomDoneTT
from .ST_90_cutout_prep.OT_cutout_prep import OTCutoutPlaneTT
from .ST_100_cutout.OT_cutout import OTCutoutTT
from .ST_105_cutout_selection.OT_cutout_selection import OTCutoutSelectionTT
from .ST_110_scale.OT_liner_scaling import OTLinerScaleTT
from .ST_120_verify_scaling.OT_verify_scaling import OTApproveScalingTT
from .ST_125_socket_milling.OT_socket_milling import OTSocketMillingTT
from .ST_130_milling_model.OT_milling_model import OTMillingModelTT
from .ST_130_thickness.OT_thickness import OTThicknessTT
from .ST_132_custom_thickness.OT_custom_thickness import OTCustomThicknessTT, OTCustomThicknessDoneTT
from .ST_135_flare.OT_flare import OTFlareTT, OTFlareDoneTT
from .ST_140_verify_socket.OT_verify_socket import OTApproveSocketTT
from .ST_150_import_connector.OT_import_connector import OTImportConnectorTT
from .ST_160_align.OT_alignment import OTSaveAlignmentTT
from .ST_170_transition.OT_transition_connector import OTTransitionConnectorTT
from .ST_180_export.OT_export_socket import OTExportSocketTT
from .ST_190_finish.OT_finish import OTFinishTT


def register():
    bpy.utils.register_class(OTStartModelingTT)
    bpy.utils.register_class(OTStartFromExistingTT)
    bpy.utils.register_class(OTImportScanTT)
    bpy.utils.register_class(OTMoveScanTT)
    bpy.utils.register_class(OTCleanUpTT)
    bpy.utils.register_class(OTHighlightNonManifoldTT)
    bpy.utils.register_class(OTFillNonManifoldTT)
    bpy.utils.register_class(OTDeleteNonManifoldTT)
    bpy.utils.register_class(OTApproveCleanUpTT)
    bpy.utils.register_class(OTSaveRotationTT)
    bpy.utils.register_class(OTCircumferenceTT)
    bpy.utils.register_class(OTCircumferencesCalcTT)
    bpy.utils.register_class(OTCircumferencesDoneTT)
    bpy.utils.register_class(OTCircumferencesHighlightTT)
    bpy.utils.register_class(OTSmoothRegionTT)
    bpy.utils.register_class(OTPushPullRegionTT)
    bpy.utils.register_class(OTFreeSculptCheckpointTT)
    bpy.utils.register_class(OTPushPullSmoothDoneTT)
    bpy.utils.register_class(OTPullBottomTT)
    bpy.utils.register_class(OTPullBottomDoneTT)
    bpy.utils.register_class(OTCutoutPlaneTT)
    bpy.utils.register_class(OTCutoutTT)
    bpy.utils.register_class(OTCutoutSelectionTT)
    bpy.utils.register_class(OTLinerScaleTT)
    bpy.utils.register_class(OTApproveScalingTT)
    bpy.utils.register_class(OTSocketMillingTT)
    bpy.utils.register_class(OTMillingModelTT)
    bpy.utils.register_class(OTThicknessTT)
    bpy.utils.register_class(OTCustomThicknessTT)
    bpy.utils.register_class(OTCustomThicknessDoneTT)
    bpy.utils.register_class(OTFlareTT)
    bpy.utils.register_class(OTFlareDoneTT)
    bpy.utils.register_class(OTApproveSocketTT)
    bpy.utils.register_class(OTImportConnectorTT)
    bpy.utils.register_class(OTSaveAlignmentTT)
    bpy.utils.register_class(OTTransitionConnectorTT)
    bpy.utils.register_class(OTExportSocketTT)
    bpy.utils.register_class(OTFinishTT)


def unregister():
    bpy.utils.unregister_class(OTStartModelingTT)
    bpy.utils.unregister_class(OTStartFromExistingTT)
    bpy.utils.unregister_class(OTImportScanTT)
    bpy.utils.unregister_class(OTMoveScanTT)
    bpy.utils.unregister_class(OTCleanUpTT)
    bpy.utils.unregister_class(OTHighlightNonManifoldTT)
    bpy.utils.unregister_class(OTFillNonManifoldTT)
    bpy.utils.unregister_class(OTDeleteNonManifoldTT)
    bpy.utils.unregister_class(OTApproveCleanUpTT)
    bpy.utils.unregister_class(OTSaveRotationTT)
    bpy.utils.unregister_class(OTCircumferenceTT)
    bpy.utils.unregister_class(OTCircumferencesCalcTT)
    bpy.utils.unregister_class(OTCircumferencesDoneTT)
    bpy.utils.unregister_class(OTCircumferencesHighlightTT)
    bpy.utils.unregister_class(OTSmoothRegionTT)
    bpy.utils.unregister_class(OTPushPullRegionTT)
    bpy.utils.unregister_class(OTFreeSculptCheckpointTT)
    bpy.utils.unregister_class(OTPushPullSmoothDoneTT)
    bpy.utils.unregister_class(OTPullBottomTT)
    bpy.utils.unregister_class(OTPullBottomDoneTT)
    bpy.utils.unregister_class(OTCutoutPlaneTT)
    bpy.utils.unregister_class(OTCutoutTT)
    bpy.utils.unregister_class(OTCutoutSelectionTT)
    bpy.utils.unregister_class(OTLinerScaleTT)
    bpy.utils.unregister_class(OTApproveScalingTT)
    bpy.utils.unregister_class(OTSocketMillingTT)
    bpy.utils.unregister_class(OTMillingModelTT)
    bpy.utils.unregister_class(OTThicknessTT)
    bpy.utils.unregister_class(OTCustomThicknessTT)
    bpy.utils.unregister_class(OTCustomThicknessDoneTT)
    bpy.utils.unregister_class(OTFlareTT)
    bpy.utils.unregister_class(OTFlareDoneTT)
    bpy.utils.unregister_class(OTApproveSocketTT)
    bpy.utils.unregister_class(OTImportConnectorTT)
    bpy.utils.unregister_class(OTSaveAlignmentTT)
    bpy.utils.unregister_class(OTTransitionConnectorTT)
    bpy.utils.unregister_class(OTExportSocketTT)
    bpy.utils.unregister_class(OTFinishTT)
