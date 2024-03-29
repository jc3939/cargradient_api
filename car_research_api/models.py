from django.db import models

# Create your models here.
class CarSpecsModel(models.Model):

    def __str__(self):
        return '-'.join([self.BasicSpec_Year, self.BasicSpec_Make, self.BasicSpec_Model, self.BasicSpec_Trim])
    
    BasicSpec_Year = models.CharField(max_length=50, default='') 
    BasicSpec_Make = models.CharField(max_length=50, default='') 
    BasicSpec_Model = models.CharField(max_length=50, default='') 
    BasicSpec_Trim = models.CharField(max_length=200, default='') 
    BasicSpec_FuelType = models.CharField(max_length=50, default='') 
    BasicSpec_Transmission = models.CharField(max_length=50, default='') 
    EngineandDrivetrain_AirIntakeType = models.CharField(max_length=50, default='') 
    BasicSpec_Horsepower = models.CharField(max_length=50, default='') 
    BasicSpec_Tourque = models.CharField(max_length=50, default='') 
    EngineandDrivetrain_MaxNbrGears = models.CharField(max_length=50, default='') 
    EngineandDrivetrain_NbrCylinders = models.CharField(max_length=50, default='') 
    EngineandDrivetrain_CylinderLayout = models.CharField(max_length=50, default='') 
    EngineandDrivetrain_EnginePosition = models.CharField(max_length=50, default='') 
    EngineandDrivetrain_EngineOrientation = models.CharField(max_length=50, default='') 
    EngineandDrivetrain_EngineId = models.CharField(max_length=50, default='') 
    BasicSpec_BodyType = models.CharField(max_length=50, default='') 
    BasicSpec_Size = models.CharField(max_length=50, default='') 
    BasicSpec_MSRP = models.CharField(max_length=50, default='') 
    EngineandDrivetrain_Drivetrain = models.CharField(max_length=50, default='') 
    Body_SeatCapacity = models.CharField(max_length=50, default='') 
    EngineandDrivetrain_Displacement = models.CharField(max_length=50, default='') 
    BasicSpec_MPG = models.CharField(max_length=50, default='') 
    BasicSpec_EstimatedElectricRange = models.CharField(max_length=50, default='') 
    Body_TankCapacity = models.CharField(max_length=50, default='') 
    EngineandDrivetrain_FuelGrade = models.CharField(max_length=50, default='') 
    Body_Length = models.CharField(max_length=50, default='') 
    Body_Width = models.CharField(max_length=50, default='') 
    Body_Height = models.CharField(max_length=50, default='') 
    Body_Wheelbase = models.CharField(max_length=50, default='') 
    Body_GroundClearance = models.CharField(max_length=50, default='') 
    Body_DoorCount = models.CharField(max_length=50, default='') 
    Body_CurbWeight = models.CharField(max_length=50, default='') 
    Body_BedLength = models.CharField(max_length=50, default='') 
    EngineandDrivetrain_TowingCapacity = models.CharField(max_length=50, default='') 
    EngineandDrivetrain_MaxSpeed = models.CharField(max_length=50, default='') 
    BasicSpec_0To60mph = models.CharField(max_length=50, default='') 
    BasicSpec_Warranty = models.CharField(max_length=50, default='') 
    EngineandDrivetrain_CompressionRatio = models.CharField(max_length=50, default='') 
    EngineandDrivetrain_MaxHpRPM = models.CharField(max_length=50, default='') 
    EngineandDrivetrain_MaxTorqueRPM = models.CharField(max_length=50, default='') 
    EngineandDrivetrain_EngineSpecialTechnology = models.CharField(max_length=50, default='') 
    EngineandDrivetrain_FuelInjection = models.CharField(max_length=50, default='') 
    EngineandDrivetrain_CylinderHeadMaterial = models.CharField(max_length=50, default='') 
    EngineandDrivetrain_EngineBlockMaterial = models.CharField(max_length=50, default='') 
    Chasis_FrontSuspension = models.CharField(max_length=50, default='') 
    Chasis_RearSuspension = models.CharField(max_length=50, default='') 
    Body_FrameType = models.CharField(max_length=50, default='') 
    Chasis_PowerSteeringType = models.CharField(max_length=50, default='') 
    Braking_FrontBrakeSystem = models.CharField(max_length=50, default='') 
    Braking_RearBrakeSystem = models.CharField(max_length=50, default='') 
    Braking_ParkingBrake = models.CharField(max_length=50, default='') 
    Wheels_FrontWheelSize = models.CharField(max_length=50, default='') 
    Wheels_RearWheelSize = models.CharField(max_length=50, default='') 
    Wheels_SpareTire = models.CharField(max_length=50, default='') 
    Safety_FrontAirbag = models.CharField(max_length=50, default='') 
    Safety_SideAirbags = models.CharField(max_length=50, default='') 
    Safety_SideCurtainAirbag = models.CharField(max_length=50, default='') 
    Safety_KneeAirbags = models.CharField(max_length=50, default='') 
    Safety_HeadRestraints = models.CharField(max_length=50, default='') 
    Safety_InflatableSeatbelt = models.CharField(max_length=50, default='') 
    Safety_FrontCenterAirbag = models.CharField(max_length=50, default='') 
    Safety_PanoramicSunroofAirbag = models.CharField(max_length=50, default='') 
    Safety_SeatCusionAirbag = models.CharField(max_length=50, default='') 
    Safety_ExternalHoodAirbag = models.CharField(max_length=50, default='') 
    Safety_TPM = models.CharField(max_length=50, default='') 
    Safety_ChildDoorLocks = models.CharField(max_length=50, default='') 
    Safety_SeatBeltWarning = models.CharField(max_length=50, default='') 
    Safety_LATCH = models.CharField(max_length=50, default='') 
    Safety_ABS = models.CharField(max_length=50, default='') 
    Safety_HighBeamAssist = models.CharField(max_length=50, default='') 
    Safety_BlindSpotDetection = models.CharField(max_length=50, default='') 
    Safety_ReverseAutomaticBraking = models.CharField(max_length=50, default='') 
    Safety_VehicleDynamicsControl = models.CharField(max_length=50, default='') 
    Safety_BrakeAssistant = models.CharField(max_length=50, default='') 
    Safety_TractionControlSystem = models.CharField(max_length=50, default='') 
    Safety_ElectronicStabilityProgram = models.CharField(max_length=50, default='') 
    Safety_LaneDepartureWarning = models.CharField(max_length=50, default='') 
    Safety_LaneKeepingAssistance = models.CharField(max_length=50, default='') 
    Safety_TrafficSignRecognition = models.CharField(max_length=50, default='') 
    Safety_ForwardCollisionWarning = models.CharField(max_length=50, default='') 
    Safety_NightVision = models.CharField(max_length=50, default='') 
    Safety_DriverFatigueMonitorSystem = models.CharField(max_length=50, default='') 
    Convenience_ParkingSensor = models.CharField(max_length=50, default='') 
    Convenience_DriverAssistanceCamera = models.CharField(max_length=50, default='') 
    Safety_RearCrossTrafficAlert = models.CharField(max_length=50, default='') 
    Convenience_CruiseControl = models.CharField(max_length=50, default='') 
    Convenience_DrivingModeSelection = models.CharField(max_length=50, default='') 
    Convenience_AutomaticParking = models.CharField(max_length=50, default='') 
    Convenience_EngineStartStopSystem = models.CharField(max_length=50, default='') 
    Convenience_AutoHold = models.CharField(max_length=50, default='') 
    Convenience_HillstartAssitControl = models.CharField(max_length=50, default='') 
    Convenience_HillDescentControl = models.CharField(max_length=50, default='') 
    Convenience_AdaptiveChasisControl = models.CharField(max_length=50, default='') 
    Convenience_Airsuspension = models.CharField(max_length=50, default='') 
    Convenience_MagneticRideControlSuspension = models.CharField(max_length=50, default='') 
    Convenience_CentralDiffLock = models.CharField(max_length=50, default='') 
    Convenience_VariableRatioSteering = models.CharField(max_length=50, default='') 
    Convenience_ActiveAllWheelSteering = models.CharField(max_length=50, default='') 
    Convenience_LimitedSlipDifferential = models.CharField(max_length=50, default='') 
    Exterior_Sunroof = models.CharField(max_length=50, default='') 
    Exterior_SportAppearancePackage = models.CharField(max_length=50, default='') 
    Exterior_WheelMaterial = models.CharField(max_length=50, default='') 
    Exterior_SoftCloseDoor = models.CharField(max_length=50, default='') 
    Exterior_SlidingDoorType = models.CharField(max_length=50, default='') 
    Exterior_PowerRearGate = models.CharField(max_length=50, default='') 
    Exterior_HandsFreeTailGate = models.CharField(max_length=50, default='') 
    Exterior_RearGateHeightMemory = models.CharField(max_length=50, default='') 
    Exterior_RearHatchGlassWindow = models.CharField(max_length=50, default='') 
    Exterior_RoofRack = models.CharField(max_length=50, default='') 
    Security_AntiTheftSystem = models.CharField(max_length=50, default='') 
    Exterior_KeylessStartSystem = models.CharField(max_length=50, default='') 
    Exterior_KeylessEntry = models.CharField(max_length=50, default='') 
    Exterior_ActiveGrilleShut = models.CharField(max_length=50, default='') 
    Exterior_EngineRemoteStart = models.CharField(max_length=50, default='') 
    Exterior_RunningBoards = models.CharField(max_length=50, default='') 
    Interior_SteeringWheelMaterial = models.CharField(max_length=50, default='') 
    Interior_SteeringWheelAdjustment = models.CharField(max_length=50, default='') 
    Interior_MultifunctionSteeringWheel = models.CharField(max_length=50, default='') 
    Interior_PaddleShift = models.CharField(max_length=50, default='') 
    Interior_HeatedSteeringWheel = models.CharField(max_length=50, default='') 
    Interior_MemorySteeringWheel = models.CharField(max_length=50, default='') 
    Interior_LcdInstrumentScreen = models.CharField(max_length=50, default='') 
    Interior_HUD = models.CharField(max_length=50, default='') 
    Interior_ActiveNoiseCancellation = models.CharField(max_length=50, default='') 
    Interior_CellPhoneWirelessCharging = models.CharField(max_length=50, default='') 
    Interior_AdjustablePedal = models.CharField(max_length=50, default='') 
    Seating_Upholstery = models.CharField(max_length=50, default='') 
    Seating_PerformanceDesignFrontSeats = models.CharField(max_length=50, default='') 
    Seating_DriverSeatAdjustment = models.CharField(max_length=50, default='') 
    Seating_PassengerSeatAdjustment = models.CharField(max_length=50, default='') 
    Seating_VentilatedFrontSeats = models.CharField(max_length=50, default='') 
    Seating_VentilatedRearSeats = models.CharField(max_length=50, default='') 
    Seating_HeatedFrontSeats = models.CharField(max_length=50, default='') 
    Seating_HeatedRearSeats = models.CharField(max_length=50, default='') 
    Seating_RecliningRearSeats = models.CharField(max_length=50, default='') 
    Seating_PowerAdjustedRearSeats = models.CharField(max_length=50, default='') 
    Seating_RearSeatTrayTable = models.CharField(max_length=50, default='') 
    Seating_CaptainsSeats = models.CharField(max_length=50, default='') 
    Seating_FoldDownRearSeats = models.CharField(max_length=50, default='') 
    Seating_RearSeatCenterArmRest = models.CharField(max_length=50, default='') 
    Seating_RearSeatCupholder = models.CharField(max_length=50, default='') 
    Seating_HeatedCoolingCupholder = models.CharField(max_length=50, default='') 
    Multimedia_CarStereoType = models.CharField(max_length=50, default='') 
    Multimedia_SizeOfCenterScreen = models.CharField(max_length=50, default='') 
    Multimedia_Navigation = models.CharField(max_length=50, default='') 
    Multimedia_RealTimeTrafficInformation = models.CharField(max_length=50, default='') 
    Multimedia_CallingforRoadSideAssistance = models.CharField(max_length=50, default='') 
    Multimedia_SplitviewScreen = models.CharField(max_length=50, default='') 
    Multimedia_BluetoothAudio = models.CharField(max_length=50, default='') 
    Multimedia_AppleCaplayAndroidAuto = models.CharField(max_length=50, default='') 
    Multimedia_VoiceRecognition = models.CharField(max_length=50, default='') 
    Multimedia_GuestureControl = models.CharField(max_length=50, default='') 
    Multimedia_FacialRecognition = models.CharField(max_length=50, default='') 
    Multimedia_OTAUpdate = models.CharField(max_length=50, default='') 
    Multimedia_RearEntertainment = models.CharField(max_length=50, default='') 
    Multimedia_RearSeatMultimediaControl = models.CharField(max_length=50, default='') 
    Multimedia_MediaChargingPort = models.CharField(max_length=50, default='') 
    Multimedia_NbrOfUSBTypeCfPorts = models.CharField(max_length=50, default='') 
    Multimedia_CDDVD = models.CharField(max_length=50, default='') 
    Multimedia_120VPowerOutlet = models.CharField(max_length=50, default='') 
    Multimedia_AmplifierBrand = models.CharField(max_length=50, default='') 
    Multimedia_NbrOfSpeaker = models.CharField(max_length=50, default='') 
    Lighting_LowBeam = models.CharField(max_length=50, default='') 
    Lighting_HighBeam = models.CharField(max_length=50, default='') 
    Lighting_DaytimeRunningLight = models.CharField(max_length=50, default='') 
    Lighting_AutoHighBeam = models.CharField(max_length=50, default='') 
    Lighting_AutoHeadLight = models.CharField(max_length=50, default='') 
    Lighting_SideMirrorTurnSignals = models.CharField(max_length=50, default='') 
    Lighting_FogLight = models.CharField(max_length=50, default='') 
    Lighting_AllWeatherLight = models.CharField(max_length=50, default='') 
    Lighting_HeadLightWasher = models.CharField(max_length=50, default='') 
    Lighting_AdaptiveHeadlights = models.CharField(max_length=50, default='') 
    Lighting_HeadLightRangeControl = models.CharField(max_length=50, default='') 
    Lighting_AmbientLighting = models.CharField(max_length=50, default='') 
    Lighting_DelayedHeadlight = models.CharField(max_length=50, default='') 
    Lighting_ReadingLight = models.CharField(max_length=50, default='') 
    WindowsandMirrors_PowerWindows = models.CharField(max_length=50, default='') 
    WindowsandMirrors_OneTouchPowerWindows = models.CharField(max_length=50, default='') 
    WindowsandMirrors_PowerWindowsAntiPinch = models.CharField(max_length=50, default='') 
    WindowsandMirrors_AcousticWindows = models.CharField(max_length=50, default='') 
    WindowsandMirrors_ExteriorMirrorFunctions = models.CharField(max_length=50, default='') 
    WindowsandMirrors_InteriorMirrorFunctions = models.CharField(max_length=50, default='') 
    WindowsandMirrors_RearWindShieldSunShades = models.CharField(max_length=50, default='') 
    WindowsandMirrors_RearPrivacyWindow = models.CharField(max_length=50, default='') 
    WindowsandMirrors_RearWindowSunShield = models.CharField(max_length=50, default='') 
    WindowsandMirrors_SunVisor = models.CharField(max_length=50, default='') 
    WindowsandMirrors_RearWiper = models.CharField(max_length=50, default='') 
    WindowsandMirrors_RainSensorWiper = models.CharField(max_length=50, default='') 
    WindowsandMirrors_HeatedWindShieldWasherNozzle = models.CharField(max_length=50, default='') 
    WindowsandMirrors_HeatedMirror = models.CharField(max_length=50, default='') 
    ClimateControl_AutomaticAC = models.CharField(max_length=50, default='') 
    ClimateControl_RearAC = models.CharField(max_length=50, default='') 
    ClimateControl_RearVent = models.CharField(max_length=50, default='') 
    ClimateControl_DualZoneClimateControl = models.CharField(max_length=50, default='') 
    ClimateControl_Airpurifier = models.CharField(max_length=50, default='') 
    ClimateControl_FragranceDiffuser = models.CharField(max_length=50, default='') 
    ClimateControl_CarRefridgerator = models.CharField(max_length=50, default='') 
    Packages_Packages = models.CharField(max_length=50, default='') 
    Convenience_GarageDoorOpener = models.CharField(max_length=50, default='') 
    BasicSpec_PayloadCapacity = models.CharField(max_length=50, default='') 
    Safety_PedestrianDetection = models.CharField(max_length=50, default='') 
    Exterior_RearSpoiler = models.CharField(max_length=50, default='') 
    WindowsandMirrors_RearWindowDefroster = models.CharField(max_length=50, default='') 
    Safety_BackupCamera = models.CharField(max_length=50, default='') 
    Convenience_remoteControlLiftgateTrunkRelease = models.CharField(max_length=50, default='') 
    Safety_SideViewCamera = models.CharField(max_length=50, default='') 
    Safety_SurroundViewCamera = models.CharField(max_length=50, default='') 
    Seating_ThridRowSeats = models.CharField(max_length=50, default='') 
    Seating_TopViewCamera = models.CharField(max_length=50, default='') 
    EngineandDrivetrain_TurningDiameter = models.CharField(max_length=50, default='')
    CarPictures = models.CharField(max_length=1000, default='')

class CarMakersModel(models.Model):

    def __str__(self):
        return self.BasicSpec_Make
        
    BasicSpec_Make = models.CharField(max_length=50, default='')


class CarListingsModel(models.Model):

    def __str__(self):
        return self.Title
    ListingId = models.IntegerField(default=0)
    Title = models.CharField(max_length=200, default='')
    Odometer = models.IntegerField(default=0)
    FuelEconomy = models.CharField(max_length=50, default='')
    FuelType = models.CharField(max_length=20, default='')
    ExteriorColor = models.CharField(max_length=50, default='')
    InteriorColor = models.CharField(max_length=50, default='')
    BodySeating = models.CharField(max_length=50, default='')
    Transmission = models.CharField(max_length=50, default='')
    DriveTrain = models.CharField(max_length=100, default='')
    Engine = models.CharField(max_length=50, default='')
    HighlightedFeatures = models.JSONField(null=True)
    DetailedSpecs = models.JSONField(null=True)
    Price = models.IntegerField(default=0)
    Condition = models.CharField(max_length=10)
    DealerName = models.CharField(max_length=20)
    CarMakers = models.CharField(max_length=20)
    CarModels = models.CharField(max_length=20)
    CarTrims = models.CharField(max_length=100)
    CarYears = models.CharField(max_length=50)
    ZipCode = models.CharField(max_length=50)
    BodyStyle = models.CharField(max_length=25, default='')
    ImageUrls = models.JSONField(null=True)
    DetailedAddress = models.CharField(max_length=100, default='')
    City = models.CharField(max_length=20, default='')
    State = models.CharField(max_length=5, default='')

class CarModelsModel(models.Model):

    def __str__(self):
        return '-'.join([self.BasicSpec_Make, self.BasicSpec_Model])
        
    BasicSpec_Make = models.CharField(max_length=50, default='') 
    BasicSpec_Model = models.CharField(max_length=50, default='') 

class CarYearsModel(models.Model):

    def __str__(self):
        return '-'.join([self.BasicSpec_Year, self.BasicSpec_Make, self.BasicSpec_Model])

    BasicSpec_Year = models.CharField(max_length=50, default='') 
    BasicSpec_Make = models.CharField(max_length=50, default='') 
    BasicSpec_Model = models.CharField(max_length=50, default='') 

class CarTrimsModel(models.Model):

    def __str__(self):
        return '-'.join([self.BasicSpec_Year, self.BasicSpec_Make, self.BasicSpec_Model, self.BasicSpec_Trim])
        
    BasicSpec_Year = models.CharField(max_length=50, default='') 
    BasicSpec_Make = models.CharField(max_length=50, default='') 
    BasicSpec_Model = models.CharField(max_length=50, default='') 
    BasicSpec_Trim = models.CharField(max_length=50, default='') 

class CarModelsListings(models.Model):

    def __str__(self):
        return '-'.join([self.BasicSpec_Year, self.BasicSpec_Make, self.BasicSpec_Model])
        
    BasicSpec_Year = models.CharField(max_length=50, default='') 
    BasicSpec_Make = models.CharField(max_length=50, default='') 
    BasicSpec_Model = models.CharField(max_length=50, default='') 

class ListingInquiryModel(models.Model):

    email_address = models.CharField(max_length=50, default='')
    phone_number = models.CharField(max_length=20, default='')
    inquiry_name = models.CharField(max_length=50, default='')
    message_body = models.CharField(max_length=500, default='')
    email_subscribed = models.BooleanField(default=False)
    car_listing_url = models.CharField(max_length=1000, default='')


