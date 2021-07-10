from django.contrib.auth import get_user_model
from rest_framework import serializers

from car_research_api.models import CarSpecsModel, CarMakersModel, CarListingsModel, CarModelsModel

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['url', 'username', 'email', 'groups']

class CarSpecsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CarSpecsModel
        fields = ['BasicSpec_Year',
                'BasicSpec_Make',
                'BasicSpec_Model',
                'BasicSpec_Trim',
                'BasicSpec_FuelType',
                'BasicSpec_Transmission',
                'EngineandDrivetrain_AirIntakeType',
                'BasicSpec_Horsepower',
                'BasicSpec_Tourque',
                'EngineandDrivetrain_MaxNbrGears',
                'EngineandDrivetrain_NbrCylinders',
                'EngineandDrivetrain_CylinderLayout',
                'EngineandDrivetrain_EnginePosition',
                'EngineandDrivetrain_EngineOrientation',
                'EngineandDrivetrain_EngineId',
                'BasicSpec_BodyType',
                'BasicSpec_Size',
                'BasicSpec_MSRP',
                'EngineandDrivetrain_Drivetrain',
                'Body_SeatCapacity',
                'EngineandDrivetrain_Displacement',
                'BasicSpec_MPG',
                'BasicSpec_EstimatedElectricRange',
                'Body_TankCapacity',
                'EngineandDrivetrain_FuelGrade',
                'Body_Length',
                'Body_Width',
                'Body_Height',
                'Body_Wheelbase',
                'Body_GroundClearance',
                'Body_DoorCount',
                'Body_CurbWeight',
                'Body_BedLength',
                'EngineandDrivetrain_TowingCapacity',
                'EngineandDrivetrain_MaxSpeed',
                'BasicSpec_0To60mph',
                'BasicSpec_Warranty',
                'EngineandDrivetrain_CompressionRatio',
                'EngineandDrivetrain_MaxHpRPM',
                'EngineandDrivetrain_MaxTorqueRPM',
                'EngineandDrivetrain_EngineSpecialTechnology',
                'EngineandDrivetrain_FuelInjection',
                'EngineandDrivetrain_CylinderHeadMaterial',
                'EngineandDrivetrain_EngineBlockMaterial',
                'Chasis_FrontSuspension',
                'Chasis_RearSuspension',
                'Body_FrameType',
                'Chasis_PowerSteeringType',
                'Braking_FrontBrakeSystem',
                'Braking_RearBrakeSystem',
                'Braking_ParkingBrake',
                'Wheels_FrontWheelSize',
                'Wheels_RearWheelSize',
                'Wheels_SpareTire',
                'Safety_FrontAirbag',
                'Safety_SideAirbags',
                'Safety_SideCurtainAirbag',
                'Safety_KneeAirbags',
                'Safety_HeadRestraints',
                'Safety_InflatableSeatbelt',
                'Safety_FrontCenterAirbag',
                'Safety_PanoramicSunroofAirbag',
                'Safety_SeatCusionAirbag',
                'Safety_ExternalHoodAirbag',
                'Safety_TPM',
                'Safety_ChildDoorLocks',
                'Safety_SeatBeltWarning',
                'Safety_LATCH',
                'Safety_ABS',
                'Safety_HighBeamAssist',
                'Safety_BlindSpotDetection',
                'Safety_ReverseAutomaticBraking',
                'Safety_VehicleDynamicsControl',
                'Safety_BrakeAssistant',
                'Safety_TractionControlSystem',
                'Safety_ElectronicStabilityProgram',
                'Safety_LaneDepartureWarning',
                'Safety_LaneKeepingAssistance',
                'Safety_TrafficSignRecognition',
                'Safety_ForwardCollisionWarning',
                'Safety_NightVision',
                'Safety_DriverFatigueMonitorSystem',
                'Convenience_ParkingSensor',
                'Convenience_DriverAssistanceCamera',
                'Safety_RearCrossTrafficAlert',
                'Convenience_CruiseControl',
                'Convenience_DrivingModeSelection',
                'Convenience_AutomaticParking',
                'Convenience_EngineStartStopSystem',
                'Convenience_AutoHold',
                'Convenience_HillstartAssitControl',
                'Convenience_HillDescentControl',
                'Convenience_AdaptiveChasisControl',
                'Convenience_Airsuspension',
                'Convenience_MagneticRideControlSuspension',
                'Convenience_CentralDiffLock',
                'Convenience_VariableRatioSteering',
                'Convenience_ActiveAllWheelSteering',
                'Convenience_LimitedSlipDifferential',
                'Exterior_Sunroof',
                'Exterior_SportAppearancePackage',
                'Exterior_WheelMaterial',
                'Exterior_SoftCloseDoor',
                'Exterior_SlidingDoorType',
                'Exterior_PowerRearGate',
                'Exterior_HandsFreeTailGate',
                'Exterior_RearGateHeightMemory',
                'Exterior_RearHatchGlassWindow',
                'Exterior_RoofRack',
                'Security_AntiTheftSystem',
                'Exterior_KeylessStartSystem',
                'Exterior_KeylessEntry',
                'Exterior_ActiveGrilleShut',
                'Exterior_EngineRemoteStart',
                'Exterior_RunningBoards',
                'Interior_SteeringWheelMaterial',
                'Interior_SteeringWheelAdjustment',
                'Interior_MultifunctionSteeringWheel',
                'Interior_PaddleShift',
                'Interior_HeatedSteeringWheel',
                'Interior_MemorySteeringWheel',
                'Interior_LcdInstrumentScreen',
                'Interior_HUD',
                'Interior_ActiveNoiseCancellation',
                'Interior_CellPhoneWirelessCharging',
                'Interior_AdjustablePedal',
                'Seating_Upholstery',
                'Seating_PerformanceDesignFrontSeats',
                'Seating_DriverSeatAdjustment',
                'Seating_PassengerSeatAdjustment',
                'Seating_VentilatedFrontSeats',
                'Seating_VentilatedRearSeats',
                'Seating_HeatedFrontSeats',
                'Seating_HeatedRearSeats',
                'Seating_RecliningRearSeats',
                'Seating_PowerAdjustedRearSeats',
                'Seating_RearSeatTrayTable',
                'Seating_CaptainsSeats',
                'Seating_FoldDownRearSeats',
                'Seating_RearSeatCenterArmRest',
                'Seating_RearSeatCupholder',
                'Seating_HeatedCoolingCupholder',
                'Multimedia_CarStereoType',
                'Multimedia_SizeOfCenterScreen',
                'Multimedia_Navigation',
                'Multimedia_RealTimeTrafficInformation',
                'Multimedia_CallingforRoadSideAssistance',
                'Multimedia_SplitviewScreen',
                'Multimedia_BluetoothAudio',
                'Multimedia_AppleCaplayAndroidAuto',
                'Multimedia_VoiceRecognition',
                'Multimedia_GuestureControl',
                'Multimedia_FacialRecognition',
                'Multimedia_OTAUpdate',
                'Multimedia_RearEntertainment',
                'Multimedia_RearSeatMultimediaControl',
                'Multimedia_MediaChargingPort',
                'Multimedia_NbrOfUSBTypeCfPorts',
                'Multimedia_CDDVD',
                'Multimedia_120VPowerOutlet',
                'Multimedia_AmplifierBrand',
                'Multimedia_NbrOfSpeaker',
                'Lighting_LowBeam',
                'Lighting_HighBeam',
                'Lighting_DaytimeRunningLight',
                'Lighting_AutoHighBeam',
                'Lighting_AutoHeadLight',
                'Lighting_SideMirrorTurnSignals',
                'Lighting_FogLight',
                'Lighting_AllWeatherLight',
                'Lighting_HeadLightWasher',
                'Lighting_AdaptiveHeadlights',
                'Lighting_HeadLightRangeControl',
                'Lighting_AmbientLighting',
                'Lighting_DelayedHeadlight',
                'Lighting_ReadingLight',
                'WindowsandMirrors_PowerWindows',
                'WindowsandMirrors_OneTouchPowerWindows',
                'WindowsandMirrors_PowerWindowsAntiPinch',
                'WindowsandMirrors_AcousticWindows',
                'WindowsandMirrors_ExteriorMirrorFunctions',
                'WindowsandMirrors_InteriorMirrorFunctions',
                'WindowsandMirrors_RearWindShieldSunShades',
                'WindowsandMirrors_RearPrivacyWindow',
                'WindowsandMirrors_RearWindowSunShield',
                'WindowsandMirrors_SunVisor',
                'WindowsandMirrors_RearWiper',
                'WindowsandMirrors_RainSensorWiper',
                'WindowsandMirrors_HeatedWindShieldWasherNozzle',
                'WindowsandMirrors_HeatedMirror',
                'ClimateControl_AutomaticAC',
                'ClimateControl_RearAC',
                'ClimateControl_RearVent',
                'ClimateControl_DualZoneClimateControl',
                'ClimateControl_Airpurifier',
                'ClimateControl_FragranceDiffuser',
                'ClimateControl_CarRefridgerator',
                'Packages_Packages',
                'Convenience_GarageDoorOpener',
                'BasicSpec_PayloadCapacity',
                'Safety_PedestrianDetection',
                'Exterior_RearSpoiler',
                'WindowsandMirrors_RearWindowDefroster',
                'Safety_BackupCamera',
                'Convenience_remoteControlLiftgateTrunkRelease',
                'Safety_SideViewCamera',
                'Safety_SurroundViewCamera',
                'Seating_ThridRowSeats',
                'Seating_TopViewCamera',
                'EngineandDrivetrain_TurningDiameter',
                'CarPictures',]

class CarMakersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CarMakersModel
        fields = ['BasicSpec_Make',]

class CarListingsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CarListingsModel
        fields = ['Title',
                'Odometer',
                'FuelEconomy',
                'ExteriorColor',
                'InteriorColor',
                'BodySeating',
                'Transmission',
                'DriveTrain',
                'Engine',
                'HighlightedFeatures',
                'DetailedSpecs',
                'Price',
                'Condition',
                'DealerName',
                'CarMakers',
                'CarModels',
                'CarTrims',
                'CarYears',
                'ZipCode',
                'BodyStyle']

class CarModelsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CarModelsModel
        fields = ['CarModels']