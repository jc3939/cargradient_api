from django.contrib.auth import get_user_model
from rest_framework import serializers

from car_research.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['url', 'username', 'email', 'groups']

class CarSpecsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CarSpecsModel
        fields = ['BasicSpec_0To60mph',
                'BasicSpec_BodyType',
                'BasicSpec_EstimatedElectricRange',
                'BasicSpec_FuelType',
                'BasicSpec_Horsepower',
                'BasicSpec_Make',
                'BasicSpec_Model',
                'BasicSpec_MPG',
                'BasicSpec_MSRP',
                'BasicSpec_PayloadCapacity',
                'BasicSpec_Size',
                'BasicSpec_Tourque',
                'BasicSpec_Transmission',
                'BasicSpec_Trim',
                'BasicSpec_Warranty',
                'BasicSpec_Year',
                'Body_BedLength',
                'Body_CurbWeight',
                'Body_DoorCount',
                'Body_GroundClearance',
                'Body_Height',
                'Body_Length',
                'Body_SeatCapacity',
                'Body_TankCapacity',
                'Body_Wheelbase',
                'Body_Width',
                'Braking_FrontBrakeSystem',
                'Braking_ParkingBrake',
                'Braking_RearBrakeSystem',
                'CarPictures',
                'Chasis_FrontSuspension',
                'Chasis_RearSuspension',
                'ClimateControl_Airpurifier',
                'ClimateControl_AutomaticAC',
                'ClimateControl_CarRefridgerator',
                'ClimateControl_DualZoneClimateControl',
                'ClimateControl_RearAC',
                'ClimateControl_RearVent',
                'Convenience_ActiveAllWheelSteering',
                'Convenience_AdaptiveChasisControl',
                'Convenience_Airsuspension',
                'Convenience_AutoHold',
                'Convenience_AutomaticParking',
                'Convenience_CentralDiffLock',
                'Convenience_CruiseControl',
                'Convenience_DriverAssistanceCamera',
                'Convenience_DrivingModeSelection',
                'Convenience_EngineStartStopSystem',
                'Convenience_HillDescentControl',
                'Convenience_HillstartAssitControl',
                'Convenience_LimitedSlipDifferential',
                'Convenience_MagneticRideControlSuspension',
                'Convenience_ParkingSensor',
                'Convenience_remoteControlLiftgateTrunkRelease',
                'Convenience_VariableRatioSteering',
                'EngineandDrivetrain_AirIntakeType',
                'EngineandDrivetrain_CylinderLayout',
                'EngineandDrivetrain_Displacement',
                'EngineandDrivetrain_Drivetrain',
                'EngineandDrivetrain_EngineId',
                'EngineandDrivetrain_EngineOrientation',
                'EngineandDrivetrain_EnginePosition',
                'EngineandDrivetrain_FuelGrade',
                'EngineandDrivetrain_MaxSpeed',
                'EngineandDrivetrain_NbrCylinders',
                'EngineandDrivetrain_TowingCapacity',
                'EngineandDrivetrain_TurningDiameter',
                'Exterior_EngineRemoteStart',
                'Exterior_KeylessEntry',
                'Exterior_KeylessStartSystem',
                'Exterior_PowerRearGate',
                'Exterior_RearSpoiler',
                'Exterior_RoofRack',
                'Exterior_RunningBoards',
                'Exterior_Sunroof',
                'Exterior_WheelMaterial',
                'Interior_CellPhoneWirelessCharging',
                'Interior_HeatedSteeringWheel',
                'Interior_HUD',
                'Interior_MemorySteeringWheel',
                'Interior_PaddleShift',
                'Interior_SteeringWheelAdjustment',
                'Lighting_AdaptiveHeadlights',
                'Lighting_AutoHeadLight',
                'Lighting_AutoHighBeam',
                'Lighting_DaytimeRunningLight',
                'Lighting_DelayedHeadlight',
                'Lighting_FogLight',
                'Lighting_HeadLightWasher',
                'Lighting_HighBeam',
                'Lighting_LowBeam',
                'Multimedia_120VPowerOutlet',
                'Multimedia_AmplifierBrand',
                'Multimedia_AppleCaplayAndroidAuto',
                'Multimedia_BluetoothAudio',
                'Multimedia_CarStereoType',
                'Multimedia_FacialRecognition',
                'Multimedia_GuestureControl',
                'Multimedia_Navigation',
                'Multimedia_NbrOfSpeaker',
                'Multimedia_NbrOfUSBTypeCfPorts',
                'Multimedia_OTAUpdate',
                'Multimedia_RealTimeTrafficInformation',
                'Multimedia_RearEntertainment',
                'Multimedia_RearSeatMultimediaControl',
                'Multimedia_SizeOfCenterScreen',
                'Multimedia_VoiceRecognition',
                'Packages_Packages',
                'Safety_ABS',
                'Safety_BackupCamera',
                'Safety_BlindSpotDetection',
                'Safety_BrakeAssistant',
                'Safety_DriverFatigueMonitorSystem',
                'Safety_ElectronicStabilityProgram',
                'Safety_ForwardCollisionWarning',
                'Safety_FrontAirbag',
                'Safety_InflatableSeatbelt',
                'Safety_KneeAirbags',
                'Safety_LaneKeepingAssistance',
                'Safety_NightVision',
                'Safety_PedestrianDetection',
                'Safety_RearCrossTrafficAlert',
                'Safety_ReverseAutomaticBraking',
                'Safety_SideAirbags',
                'Safety_SideCurtainAirbag',
                'Safety_SideViewCamera',
                'Safety_SurroundViewCamera',
                'Safety_TPM',
                'Safety_TractionControlSystem',
                'Safety_TrafficSignRecognition',
                'Seating_CaptainsSeats',
                'Seating_DriverSeatAdjustment',
                'Seating_FoldDownRearSeats',
                'Seating_HeatedCoolingCupholder',
                'Seating_HeatedFrontSeats',
                'Seating_HeatedRearSeats',
                'Seating_PassengerSeatAdjustment',
                'Seating_PowerAdjustedRearSeats',
                'Seating_RecliningRearSeats',
                'Seating_ThridRowSeats',
                'Seating_TopViewCamera',
                'Seating_Upholstery',
                'Seating_VentilatedFrontSeats',
                'Seating_VentilatedRearSeats',
                'Security_AntiTheftSystem',
                'Wheels_FrontWheelSize',
                'Wheels_RearWheelSize',
                'Wheels_SpareTire',
                'WindowsandMirrors_AcousticWindows',
                'WindowsandMirrors_ExteriorMirrorFunctions',
                'WindowsandMirrors_HeatedMirror',
                'WindowsandMirrors_InteriorMirrorFunctions',
                'WindowsandMirrors_OneTouchPowerWindows',
                'WindowsandMirrors_PowerWindows',
                'WindowsandMirrors_RainSensorWiper',
                'WindowsandMirrors_RearPrivacyWindow',
                'WindowsandMirrors_RearWindowDefroster',
                'WindowsandMirrors_RearWiper']

class CarMakersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CarMakersModel
        fields = ['BasicSpec_Make',]

class CarListingsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CarListingsModel
        fields = ['ListingId',
                'Title',
                'Odometer',
                'FuelType',
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
                'BodyStyle',
                'ImageUrls',
                'DetailedAddress',
                'City',
                'State']

class CarModelsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CarModelsModel
        fields = ['BasicSpec_Make',
                  'BasicSpec_Model']

class CarModelsListingsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CarModelsListings
        fields = ['BasicSpec_Year',
                  'BasicSpec_Make',
                  'BasicSpec_Model']

class CarMakersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CarMakersModel
        fields = ['BasicSpec_Make']

class CarYearsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CarYearsModel
        fields = ['BasicSpec_Year',
                  'BasicSpec_Make',
                  'BasicSpec_Model']

class CarTrimsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CarTrimsModel
        fields = ['BasicSpec_Year',
                  'BasicSpec_Make',
                  'BasicSpec_Model',
                  'BasicSpec_Trim']


class ListingInquirySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ListingInquiryModel
        fields = '__all__'