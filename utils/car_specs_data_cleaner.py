import pymongo
import pandas as pd

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["kbb_data"]

mycol = mydb["car_specs"]

car_specs_df = pd.DataFrame.from_records(mycol.find())

def create_specs_dictionary(specs_info):
    specs = specs_info.replace('\'','').replace('{','').replace('}','').split(', ')
    f = lambda x: x.split(': ')
    specs = list(map(f, specs))
    specs_dict = {}
    for item in specs:
        if len(item)!=2:
            continue
        specs_dict[item[0]] = item[1]
    return specs_dict

def create_and_mapping_features(row):
    specs_dictionary = create_specs_dictionary(row['specs_info'])
    basic_dictionary = create_specs_dictionary(row['basic_info'])
    row['Basic Spec.Year'] = row['car_year']
    row['Basic Spec.Make'] = row['car_make']
    row['Basic Spec.Model'] = row['car_model']
    row['Basic Spec.Trim'] = row['car_trim'] 
    row['Basic Spec.FuelType'] = specs_dictionary['engineType']
    row['Basic Spec.Transmission'] = specs_dictionary['dualClutchAutomaticTransmission'] if specs_dictionary['dualClutchAutomaticTransmission'] != 'Not Available' else specs_dictionary['transmissionType']
    row['Engine and Drivetrain.AirIntakeType'] = ''
    row['Basic Spec.Horsepower(hp)'] = specs_dictionary['horsepower'] + '@' + specs_dictionary['horsepowerRpm']
    row['Basic Spec.Tourque(lb-ft)'] = specs_dictionary['torque']
    row['Engine and Drivetrain.MaxNbrGears'] = specs_dictionary['numberofSpeeds']
    row['Engine and Drivetrain.NbrCylinders'] = ''
    row['Engine and Drivetrain.CylinderLayout'] = ''
    row['Engine and Drivetrain.EnginePosition'] = ''
    row['Engine and Drivetrain.EngineOrientation'] = ''
    row['Engine and Drivetrain.EngineId'] = ''
    row['Basic Spec.BodyType'] = basic_dictionary['bodyStyle']
    row['Basic Spec.Size'] = basic_dictionary['size']
    row['Basic Spec.MSRP'] = basic_dictionary['nationalBaseDefaultPrice']
    row['Engine and Drivetrain.Drivetrain'] = specs_dictionary['driveTrain']
    row['Body.SeatCapacity'] = specs_dictionary['maxSeatingCapacity']
    row['Engine and Drivetrain.Displacement'] = ''
    row['Basic Spec.MPG(City/Highway/Combined)'] = '/'.join([specs_dictionary['epaCity'],specs_dictionary['epaHwy'],specs_dictionary['epaMpgeCombined']])
    row['Basic Spec.Estimated Electric Range'] = specs_dictionary['estimatedElectricRange']
    row['Body.TankCapacity'] = specs_dictionary['fuelCapacity']
    row['Engine and Drivetrain.FuelGrade'] = specs_dictionary['recommendedFuel']
    row['Body.Length'] = specs_dictionary['overallLength']
    row['Body.Width'] = ''
    row['Body.Height'] = ''
    row['Body.Wheelbase'] = specs_dictionary['wheelBase']
    row['Body.GroundClearance'] = specs_dictionary['minimumGroundClearance']
    row['Body.DoorCount'] = specs_dictionary['doors']
    row['Body.Curb Weight'] = specs_dictionary['curbWeight']
    row['Body.Bed Length'] = specs_dictionary['bedLength']
    row['Engine and Drivetrain.TowingCapacity'] = specs_dictionary['maximumTowingCapacity']
    row['Engine and Drivetrain.MaxSpeed'] = ''
    row['Basic Spec.0-60mph'] = ''
    row['Basic Spec.Warranty'] = specs_dictionary['basicWarrantyMiles']+'/'+specs_dictionary['basicWarrantyYears']
    row['Engine and Drivetrain.CompressionRatio'] = ''
    row['Engine and Drivetrain.MaxHpRPM'] = ''
    row['Engine and Drivetrain.MaxTorqueRPM'] = ''
    row['Engine and Drivetrain.EngineSpecialTechnology'] = ''
    row['Engine and Drivetrain.FuelInjection'] = ''
    row['Engine and Drivetrain.CylinderHeadMaterial'] = ''
    row['Engine and Drivetrain.EngineBlockMaterial'] = ''
    row['Chasis.FrontSuspension'] = ''
    row['Chasis.RearSuspension'] = ''
    row['Body.FrameType'] = ''
    row['Chasis.PowerSteeringType'] = ''
    row['Braking.FrontBrakeSystem'] = ''
    row['Braking.RearBrakeSystem'] = ''
    row['Braking.ParkingBrake'] = ''
    row['Wheels.FrontWheelSize'] = ''
    row['Wheels.RearWheelSize'] = ''
    row['Wheels.SpareTire'] = ''
    row['Safety.FrontAirbag'] = ''
    row['Safety.SideAirbags'] = ''
    row['Safety.SideCurtainAirbag'] = ''
    row['Safety.KneeAirbags'] = ''
    row['Safety.HeadRestraints'] = '' 
    row['Safety.InflatableSeatbelt'] = ''
    row['Safety.Front-centerAirbag'] = ''
    row['Safety.PanoramicSunroofAirbag'] = ''
    row['Safety.SeatCusionAirbag'] = ''
    row['Safety.ExternalHoodAirbag'] = ''
    row['Safety.TPM'] = ''
    row['Safety.Child Door Locks'] = specs_dictionary['childDoorLocks']
    row['Safety.SeatBeltWarning'] = ''
    row['Safety.LATCH'] = specs_dictionary['childSeatAnchors']
    row['Safety.ABS'] = ''
    row['Safety.HighBeamAssist(HBA)'] = ''
    row['Safety.BlindSpotDetection'] = specs_dictionary['blindSpotAlert']
    row['Safety.ReverseAutomaticBraking'] = ''
    row['Safety.VehicleDynamicsControl(VDC)'] = specs_dictionary['slipControl']
    row['Safety.BrakeAssistant'] = ''
    row['Safety.TractionControlSystem(TCS)'] = specs_dictionary['tractionControl']
    row['Safety.ElectronicStabilityProgram(ESP)'] = specs_dictionary['stabilityControl']
    row['Safety.LaneDepartureWarning'] = ''
    row['Safety.LaneKeepingAssistance'] = ''
    row['Safety.TrafficSignRecognition'] = ''
    row['Safety.ForwardCollisionWarning'] = specs_dictionary['collisionWarningSystem']
    row['Safety.NightVision'] = specs_dictionary['nightVisionSystem']
    row['Safety.DriverFatigueMonitorSystem'] = specs_dictionary['driverAttentionAssistMonitor']
    row['Convenience.ParkingSensor'] = specs_dictionary['frontRearParkingSensors']
    row['Convenience.DriverAssistanceCamera'] = ''
    row['Safety.RearCrossTrafficAlert(RCTA)'] = ''
    row['Convenience.CruiseControl'] = specs_dictionary['cruiseControl']
    row['Convenience.DrivingModeSelection'] = ''
    row['Convenience.AutomaticParking'] = specs_dictionary['parkAssist']
    row['Convenience.EngineStartStopSystem'] = ''
    row['Convenience.AutoHold'] = ''
    row['Convenience.HillstartAssitControl(HAC)'] = specs_dictionary['hillStartAssist']
    row['Convenience.HillDescentControl(HDC)'] = specs_dictionary['hillDescentControl']
    row['Convenience.AdaptiveChasisControl'] = ''
    row['Convenience.Airsuspension'] = ''
    row['Convenience.MagneticRideControlSuspension'] = ''
    row['Convenience.CentralDiffLock'] = ''
    row['Convenience.VariableRatioSteering'] = ''
    row['Convenience.ActiveAllWheelSteering'] = ''
    row['Convenience.LimitedSlipDifferential'] = specs_dictionary['limitedSlipDifferential']
    if specs_dictionary['moonRoof'] != 'Not Available':
        row['Exterior.Sunroof'] = specs_dictionary['moonRoof'] + ' Moonroof'
    elif specs_dictionary['panoramaMoonRoof'] != 'Not Available':
        row['Exterior.Sunroof'] = specs_dictionary['panoramaMoonRoof']+' Panorama Moonroof'
    else:
        row['Exterior.Sunroof'] = 'NA'
    
    row['Exterior.SportAppearancePackage'] = ''
    row['Exterior.WheelMaterial'] = specs_dictionary['alloyWheels'] + 'alloy wheel' if specs_dictionary['alloyWheels'] != 'Not Available' else ''
    row['Exterior.SoftCloseDoor'] = ''
    row['Exterior.SlidingDoorType'] = specs_dictionary['powerSlidingDoors'] + ' Power Sliding Doors wheel' if specs_dictionary['alloyWheels'] != 'Not Available' else 'NA'
    row['Exterior.PowerRearGate'] = ''
    row['Exterior.HandsFreeTailGate'] = ''
    row['Exterior.RearGateHeightMemory'] = ''
    row['Exterior.RearHatchGlassWindow'] = ''
    row['Exterior.RoofRack'] = specs_dictionary['roofRails']
    row['Security.Anti-theftSystem'] = ''
    row['Exterior.KeylessStartSystem'] = specs_dictionary['pushButtonEngineStart']
    row['Exterior.KeylessEntry'] = specs_dictionary['proximitySensingKeylessEntry'] + ' Proximity Sensing Keyless Entry' if specs_dictionary['proximitySensingKeylessEntry'] != 'Not Available' else specs_dictionary['remoteKeylessEntry']
    row['Exterior.ActiveGrilleShut'] = ''
    row['Exterior.EngineRemoteStart'] = specs_dictionary['remoteStart']
    row['Exterior.RunningBoards'] = ''
    row['Interior.SteeringWheelMaterial'] = specs_dictionary['leatherWrappedSteeringWheel'] + ' leather' if specs_dictionary['leatherWrappedSteeringWheel'] != 'Not Available' else 'NA'
    if specs_dictionary['tiltTelescopingSteeringWheel'] != 'Not Available':
        row['Interior.SteeringWheelAdjustment'] = 'tilt/telescoping'
    elif specs_dictionary['tiltSteeringWheel'] != 'Not Available':
        row['Interior.SteeringWheelAdjustment'] = 'tilt'
    else:
        row['Interior.SteeringWheelAdjustment'] = 'NA'

    row['Interior.MultifunctionSteeringWheel'] = specs_dictionary['steeringWheelControls']
    row['Interior.PaddleShift'] = ''
    row['Interior.HeatedSteeringWheel'] = specs_dictionary['heatedSteeringWheel']
    row['Interior.MemorySteeringWheel'] = ''
    row['Interior.LcdInstrumentScreen'] = specs_dictionary['lcdInstrumentCluster']
    row['Interior.HUD'] = ''
    row['Interior.ActiveNoiseCancellation'] = ''
    row['Interior.CellPhoneWirelessCharging'] = ''
    row['Interior.AdjustablePedal'] = specs_dictionary['powerAdjustablePedals']
    row['Seating.Upholstery'] = specs_dictionary['leatherInteriorTrim'] + ' Leather Trim' if specs_dictionary['leatherInteriorTrim'] != 'Not Available' else 'cloth'
    row['Seating.PerformanceDesignFrontSeats'] = ''
    row['Seating.DriverSeatAdjustment'] = "powerDriversSeat" if specs_dictionary['powerDriversSeat'] != 'Not Available' else 'Manual'
    row['Seating.PassengerSeatAdjustment'] = ''
    row['Seating.VentilatedFrontSeats'] = specs_dictionary['cooledFrontSeats']  
    row['Seating.VentilatedRearSeats'] = specs_dictionary['cooledFrontSeats']
    row['Seating.HeatedFrontSeats'] = specs_dictionary['heatedFrontSeats']
    row['Seating.HeatedRearSeats'] = specs_dictionary['heatedRearSeats']
    row['Seating.RecliningRearSeats'] = ''
    row['Seating.PowerAdjustedRearSeats'] = ''
    row['Seating.RearSeatTrayTable'] = ''
    row['Seating.CaptainsSeats'] = ''
    row['Seating.FoldDownRearSeats'] = specs_dictionary['foldingRearSeat']
    row['Seating.RearSeatCenterArmRest'] = ''
    row['Seating.RearSeatCupholder'] = ''
    row['Seating.Heated/CoolingCupholder'] = ''
    row['Multimedia.CarStereoType'] = ''
    row['Multimedia.SizeOfCenterScreen'] = ''
    row['Multimedia.Navigation'] = specs_dictionary['navigation']
    row['Multimedia.RealTimeTrafficInformation'] = specs_dictionary['realTimeTrafficInformation']
    row['Multimedia.CallingforRoadSideAssistance'] = ''
    row['Multimedia.SplitviewScreen'] = ''
    row['Multimedia.BluetoothAudio'] = specs_dictionary['bluetoothStreamingAudio']
    row['Multimedia.AppleCaplay/AndroidAuto'] = specs_dictionary['smartphoneInterface']
    row['Multimedia.VoiceRecognition'] = specs_dictionary['voiceRecognitionSystem']
    row['Multimedia.GuestureControl'] = ''
    row['Multimedia.FacialRecognition'] = ''
    row['Multimedia.OTAUpdate'] = ''
    row['Multimedia.RearEntertainment'] = specs_dictionary['rearDVDEntertainmentSystem']
    row['Multimedia.RearSeatMultimediaControl'] = ''
    row['Multimedia.Media/ChargingPort'] = specs_dictionary['usbPort']
    row['Multimedia.NbrOfUSB/Type-CfPorts'] = ''
    row['Multimedia.CD/DVD'] = specs_dictionary['cdPlayer']
    row['Multimedia.120VPowerOutlet'] = specs_dictionary['powerOutlet']
    row['Multimedia.AmplifierBrand'] = ''
    row['Multimedia.NbrOfSpeaker'] = ''
    row['Lighting.LowBeam'] = ''
    row['Lighting.HighBeam'] = ''
    row['Lighting.DaytimeRunningLight'] = ''
    row['Lighting.AutoHighBeam'] = ''
    row['Lighting.AutoHeadLight'] = ''
    row['Lighting.SideMirrorTurnSignals'] = ''
    row['Lighting.FogLight'] = specs_dictionary['fogLights']
    row['Lighting.AllWeatherLight'] = ''
    row['Lighting.HeadLightWasher'] = ''
    row['Lighting.AdaptiveHeadlights'] = specs_dictionary['adaptiveHeadlights']
    row['Lighting.HeadLightRangeControl'] = ''
    row['Lighting.AmbientLighting'] = ''
    row['Lighting.DelayedHeadlight'] = ''
    row['Lighting.ReadingLight'] = ''
    row['Windows and Mirrors.PowerWindows'] = specs_dictionary['powerWindows']
    row['Windows and Mirrors.OneTouchPowerWindows'] = ''
    row['Windows and Mirrors.PowerWindowsAntiPinch'] = ''
    row['Windows and Mirrors.AcousticWindows'] = ''
    row['Windows and Mirrors.ExteriorMirrorFunctions'] = specs_dictionary['powerFoldingExteriorMirrors'] + ' Power Folding Exterior Mirrors' if specs_dictionary['powerFoldingExteriorMirrors'] != 'Not Available' else 'NA'
    row['Windows and Mirrors.InteriorMirrorFunctions'] = ''
    row['Windows and Mirrors.RearWindShieldSunShades'] = ''
    row['Windows and Mirrors.RearPrivacyWindow'] = specs_dictionary['privacyGlass']
    row['Windows and Mirrors.RearWindowSunShield'] = ''
    row['Windows and Mirrors.SunVisor'] = ''
    row['Windows and Mirrors.RearWiper'] = ''
    row['Windows and Mirrors.RainSensorWiper'] = specs_dictionary['rainSensingWindshieldWipers']
    row['Windows and Mirrors.HeatedWindShieldWasherNozzle'] = specs_dictionary['heatedWindshield']
    row['Windows and Mirrors.Heated Mirror'] = specs_dictionary['heatedMirror']
    row['Climate Control.AutomaticAC'] = ''
    row['Climate Control.RearAC'] = ''
    row['Climate Control.RearVent'] = ''
    row['Climate Control.DualZoneClimateControl'] = ''
    row['Climate Control.Airpurifier'] = ''
    row['Climate Control.FragranceDiffuser'] = ''
    row['Climate Control.CarRefridgerator'] = specs_dictionary['refrigeratorCooler']
    row['Packages.Packages'] = ''
    row['Convenience.Garage Door Opener'] = specs_dictionary['integratedGarageDoorOpener']
    row['Basic Spec.Payload Capacity'] = specs_dictionary['payloadCapacity']
    row['Safety.Pedestrian Detection'] = specs_dictionary['pedestrianDetectionSystem']
    row['Exterior.Rear Spoiler'] = specs_dictionary['rearSpoiler']
    row['Windows and Mirrors.Rear Window Defroster'] = specs_dictionary['rearWindowDefroster']
    row['Safety.Backup Camera'] = specs_dictionary['rearviewCamera']
    row['Convenience.remote Control Liftgate/Trunk Release'] = specs_dictionary['remoteControlLiftgateTrunkRelease']
    row['Safety.Side View Camera'] = specs_dictionary['sideViewCameras']
    row['Safety.Surround View Camera'] = specs_dictionary['surroundViewCamera']
    row['Seating.Thrid Row Seats'] = specs_dictionary['thirdRow']
    row['Seating.Top View Camera'] = specs_dictionary['topViewCamera']
    row['Engine and Drivetrain.Turning Diameter'] = specs_dictionary['turningDiameter']

    return row

car_specs_df = car_specs_df.apply(create_and_mapping_features, axis=1).drop(['_id','basic_info', 'car_make','car_model','car_trim','car_year','query_date','query_url','specs_info','vehicleId'],axis=1)