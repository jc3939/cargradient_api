import pymongo
import pandas as pd
from car_research_api.models import CarSpecsModel
from django.core.management.base import BaseCommand, CommandError
import sys

class Command(BaseCommand):

    help = 'load car specs data from lake to db.'

    myclient = pymongo.MongoClient("mongodb://localhost:27017/")

    mydb = myclient["kbb_data"]

    mycol = mydb["car_specs"]

    car_specs_df = pd.DataFrame.from_records(mycol.find())

    @staticmethod
    def create_and_mapping_features(row):
        
        
        def _create_specs_dictionary(specs_info):
            specs = specs_info.replace('\'','').replace('{','').replace('}','').replace('"','').split(', ')
            f = lambda x: x.split(': ')
            specs = list(map(f, specs))
            specs_dict = {}
            for item in specs:
                if len(item)!=2:
                    continue
                specs_dict[item[0]] = item[1]
            return specs_dict

        try:
            specs_dictionary = _create_specs_dictionary(row['specs_info'])
            basic_dictionary = _create_specs_dictionary(row['basic_info'])
            row['BasicSpec_Year'] = row['car_year']
            row['BasicSpec_Make'] = row['car_make']
            row['BasicSpec_Model'] = row['car_model']
            row['BasicSpec_Trim'] = row['car_trim'] 
            row['BasicSpec_FuelType'] = specs_dictionary['engineType']
            row['BasicSpec_Transmission'] = specs_dictionary['dualClutchAutomaticTransmission'] if specs_dictionary['dualClutchAutomaticTransmission'] != 'Not Available' else specs_dictionary['transmissionType']
            row['EngineandDrivetrain_AirIntakeType'] = ''
            row['BasicSpec_Horsepower'] = specs_dictionary['horsepower'] + '@' + specs_dictionary['horsepowerRpm']
            row['BasicSpec_Tourque'] = specs_dictionary['torque']
            row['EngineandDrivetrain_MaxNbrGears'] = specs_dictionary['numberofSpeeds']
            row['EngineandDrivetrain_NbrCylinders'] = ''
            row['EngineandDrivetrain_CylinderLayout'] = ''
            row['EngineandDrivetrain_EnginePosition'] = ''
            row['EngineandDrivetrain_EngineOrientation'] = ''
            row['EngineandDrivetrain_EngineId'] = ''
            row['BasicSpec_BodyType'] = basic_dictionary['bodyStyle']
            row['BasicSpec_Size'] = basic_dictionary['size']
            row['BasicSpec_MSRP'] = basic_dictionary['nationalBaseDefaultPrice']
            row['EngineandDrivetrain_Drivetrain'] = specs_dictionary['driveTrain']
            row['Body_SeatCapacity'] = specs_dictionary['maxSeatingCapacity']
            row['EngineandDrivetrain_Displacement'] = ''
            row['BasicSpec_MPG'] = '/'.join([specs_dictionary['epaCity'],specs_dictionary['epaHwy'],specs_dictionary['epaMpgeCombined']])
            row['BasicSpec_EstimatedElectricRange'] = specs_dictionary['estimatedElectricRange']
            row['Body_TankCapacity'] = specs_dictionary['fuelCapacity']
            row['EngineandDrivetrain_FuelGrade'] = specs_dictionary['recommendedFuel']
            row['Body_Length'] = specs_dictionary['overallLength']
            row['Body_Width'] = ''
            row['Body_Height'] = ''
            row['Body_Wheelbase'] = specs_dictionary['wheelBase']
            row['Body_GroundClearance'] = specs_dictionary['minimumGroundClearance']
            row['Body_DoorCount'] = specs_dictionary['doors']
            row['Body_CurbWeight'] = specs_dictionary['curbWeight']
            row['Body_BedLength'] = specs_dictionary['bedLength']
            row['EngineandDrivetrain_TowingCapacity'] = specs_dictionary['maximumTowingCapacity']
            row['EngineandDrivetrain_MaxSpeed'] = ''
            row['BasicSpec_0To60mph'] = ''
            row['BasicSpec_Warranty'] = specs_dictionary['basicWarrantyMiles']+'/'+specs_dictionary['basicWarrantyYears']
            row['EngineandDrivetrain_CompressionRatio'] = ''
            row['EngineandDrivetrain_MaxHpRPM'] = ''
            row['EngineandDrivetrain_MaxTorqueRPM'] = ''
            row['EngineandDrivetrain_EngineSpecialTechnology'] = ''
            row['EngineandDrivetrain_FuelInjection'] = ''
            row['EngineandDrivetrain_CylinderHeadMaterial'] = ''
            row['EngineandDrivetrain_EngineBlockMaterial'] = ''
            row['Chasis_FrontSuspension'] = ''
            row['Chasis_RearSuspension'] = ''
            row['Body_FrameType'] = ''
            row['Chasis_PowerSteeringType'] = ''
            row['Braking_FrontBrakeSystem'] = ''
            row['Braking_RearBrakeSystem'] = ''
            row['Braking_ParkingBrake'] = ''
            row['Wheels_FrontWheelSize'] = ''
            row['Wheels_RearWheelSize'] = ''
            row['Wheels_SpareTire'] = ''
            row['Safety_FrontAirbag'] = ''
            row['Safety_SideAirbags'] = ''
            row['Safety_SideCurtainAirbag'] = ''
            row['Safety_KneeAirbags'] = ''
            row['Safety_HeadRestraints'] = '' 
            row['Safety_InflatableSeatbelt'] = ''
            row['Safety_FrontCenterAirbag'] = ''
            row['Safety_PanoramicSunroofAirbag'] = ''
            row['Safety_SeatCusionAirbag'] = ''
            row['Safety_ExternalHoodAirbag'] = ''
            row['Safety_TPM'] = ''
            row['Safety_ChildDoorLocks'] = specs_dictionary['childDoorLocks']
            row['Safety_SeatBeltWarning'] = ''
            row['Safety_LATCH'] = specs_dictionary['childSeatAnchors']
            row['Safety_ABS'] = ''
            row['Safety_HighBeamAssist'] = ''
            row['Safety_BlindSpotDetection'] = specs_dictionary['blindSpotAlert']
            row['Safety_ReverseAutomaticBraking'] = ''
            row['Safety_VehicleDynamicsControl'] = specs_dictionary['slipControl']
            row['Safety_BrakeAssistant'] = ''
            row['Safety_TractionControlSystem'] = specs_dictionary['tractionControl']
            row['Safety_ElectronicStabilityProgram'] = specs_dictionary['stabilityControl']
            row['Safety_LaneDepartureWarning'] = ''
            row['Safety_LaneKeepingAssistance'] = ''
            row['Safety_TrafficSignRecognition'] = ''
            row['Safety_ForwardCollisionWarning'] = specs_dictionary['collisionWarningSystem']
            row['Safety_NightVision'] = specs_dictionary['nightVisionSystem']
            row['Safety_DriverFatigueMonitorSystem'] = specs_dictionary['driverAttentionAssistMonitor']
            row['Convenience_ParkingSensor'] = specs_dictionary['frontRearParkingSensors']
            row['Convenience_DriverAssistanceCamera'] = ''
            row['Safety_RearCrossTrafficAlert'] = ''
            row['Convenience_CruiseControl'] = specs_dictionary['cruiseControl']
            row['Convenience_DrivingModeSelection'] = ''
            row['Convenience_AutomaticParking'] = specs_dictionary['parkAssist']
            row['Convenience_EngineStartStopSystem'] = ''
            row['Convenience_AutoHold'] = ''
            row['Convenience_HillstartAssitControl'] = specs_dictionary['hillStartAssist']
            row['Convenience_HillDescentControl'] = specs_dictionary['hillDescentControl']
            row['Convenience_AdaptiveChasisControl'] = ''
            row['Convenience_Airsuspension'] = ''
            row['Convenience_MagneticRideControlSuspension'] = ''
            row['Convenience_CentralDiffLock'] = ''
            row['Convenience_VariableRatioSteering'] = ''
            row['Convenience_ActiveAllWheelSteering'] = ''
            row['Convenience_LimitedSlipDifferential'] = specs_dictionary['limitedSlipDifferential']
            if specs_dictionary['moonRoof'] != 'Not Available':
                row['Exterior_Sunroof'] = specs_dictionary['moonRoof'] + ' Moonroof'
            elif specs_dictionary['panoramaMoonRoof'] != 'Not Available':
                row['Exterior_Sunroof'] = specs_dictionary['panoramaMoonRoof']+' PanoramaMoonroof'
            else:
                row['Exterior_Sunroof'] = 'NA'

            row['Exterior_SportAppearancePackage'] = ''
            row['Exterior_WheelMaterial'] = specs_dictionary['alloyWheels'] + 'alloywheel' if specs_dictionary['alloyWheels'] != 'Not Available' else ''
            row['Exterior_SoftCloseDoor'] = ''
            row['Exterior_SlidingDoorType'] = specs_dictionary['powerSlidingDoors'] + ' PowerSlidingDoorswheel' if specs_dictionary['alloyWheels'] != 'Not Available' else 'NA'
            row['Exterior_PowerRearGate'] = ''
            row['Exterior_HandsFreeTailGate'] = ''
            row['Exterior_RearGateHeightMemory'] = ''
            row['Exterior_RearHatchGlassWindow'] = ''
            row['Exterior_RoofRack'] = specs_dictionary['roofRails']
            row['Security_AntiTheftSystem'] = ''
            row['Exterior_KeylessStartSystem'] = specs_dictionary['pushButtonEngineStart']
            row['Exterior_KeylessEntry'] = specs_dictionary['proximitySensingKeylessEntry'] + ' ProximitySensingKeylessEntry' if specs_dictionary['proximitySensingKeylessEntry'] != 'Not Available' else specs_dictionary['remoteKeylessEntry']
            row['Exterior_ActiveGrilleShut'] = ''
            row['Exterior_EngineRemoteStart'] = specs_dictionary['remoteStart']
            row['Exterior_RunningBoards'] = ''
            row['Interior_SteeringWheelMaterial'] = specs_dictionary['leatherWrappedSteeringWheel'] + ' leather' if specs_dictionary['leatherWrappedSteeringWheel'] != 'Not Available' else 'NA'
            if specs_dictionary['tiltTelescopingSteeringWheel'] != 'Not Available':
                row['Interior_SteeringWheelAdjustment'] = 'tilt/telescoping'
            elif specs_dictionary['tiltSteeringWheel'] != 'Not Available':
                row['Interior_SteeringWheelAdjustment'] = 'tilt'
            else:
                row['Interior_SteeringWheelAdjustment'] = 'NA'

            row['Interior_MultifunctionSteeringWheel'] = specs_dictionary['steeringWheelControls']
            row['Interior_PaddleShift'] = ''
            row['Interior_HeatedSteeringWheel'] = specs_dictionary['heatedSteeringWheel']
            row['Interior_MemorySteeringWheel'] = ''
            row['Interior_LcdInstrumentScreen'] = specs_dictionary['lcdInstrumentCluster']
            row['Interior_HUD'] = ''
            row['Interior_ActiveNoiseCancellation'] = ''
            row['Interior_CellPhoneWirelessCharging'] = ''
            row['Interior_AdjustablePedal'] = specs_dictionary['powerAdjustablePedals']
            row['Seating_Upholstery'] = specs_dictionary['leatherInteriorTrim'] + ' LeatherTrim' if specs_dictionary['leatherInteriorTrim'] != 'Not Available' else 'cloth'
            row['Seating_PerformanceDesignFrontSeats'] = ''
            row['Seating_DriverSeatAdjustment'] = "powerDriversSeat" if specs_dictionary['powerDriversSeat'] != 'Not Available' else 'Manual'
            row['Seating_PassengerSeatAdjustment'] = ''
            row['Seating_VentilatedFrontSeats'] = specs_dictionary['cooledFrontSeats']  
            row['Seating_VentilatedRearSeats'] = specs_dictionary['cooledFrontSeats']
            row['Seating_HeatedFrontSeats'] = specs_dictionary['heatedFrontSeats']
            row['Seating_HeatedRearSeats'] = specs_dictionary['heatedRearSeats']
            row['Seating_RecliningRearSeats'] = ''
            row['Seating_PowerAdjustedRearSeats'] = ''
            row['Seating_RearSeatTrayTable'] = ''
            row['Seating_CaptainsSeats'] = ''
            row['Seating_FoldDownRearSeats'] = specs_dictionary['foldingRearSeat']
            row['Seating_RearSeatCenterArmRest'] = ''
            row['Seating_RearSeatCupholder'] = ''
            row['Seating_HeatedCoolingCupholder'] = ''
            row['Multimedia_CarStereoType'] = ''
            row['Multimedia_SizeOfCenterScreen'] = ''
            row['Multimedia_Navigation'] = specs_dictionary['navigation']
            row['Multimedia_RealTimeTrafficInformation'] = specs_dictionary['realTimeTrafficInformation']
            row['Multimedia_CallingforRoadSideAssistance'] = ''
            row['Multimedia_SplitviewScreen'] = ''
            row['Multimedia_BluetoothAudio'] = specs_dictionary['bluetoothStreamingAudio']
            row['Multimedia_AppleCaplayAndroidAuto'] = specs_dictionary['smartphoneInterface']
            row['Multimedia_VoiceRecognition'] = specs_dictionary['voiceRecognitionSystem']
            row['Multimedia_GuestureControl'] = ''
            row['Multimedia_FacialRecognition'] = ''
            row['Multimedia_OTAUpdate'] = ''
            row['Multimedia_RearEntertainment'] = specs_dictionary['rearDVDEntertainmentSystem']
            row['Multimedia_RearSeatMultimediaControl'] = ''
            row['Multimedia_MediaChargingPort'] = specs_dictionary['usbPort']
            row['Multimedia_NbrOfUSBTypeCfPorts'] = ''
            row['Multimedia_CDDVD'] = specs_dictionary['cdPlayer']
            row['Multimedia_120VPowerOutlet'] = specs_dictionary['powerOutlet']
            row['Multimedia_AmplifierBrand'] = ''
            row['Multimedia_NbrOfSpeaker'] = ''
            row['Lighting_LowBeam'] = ''
            row['Lighting_HighBeam'] = ''
            row['Lighting_DaytimeRunningLight'] = ''
            row['Lighting_AutoHighBeam'] = ''
            row['Lighting_AutoHeadLight'] = ''
            row['Lighting_SideMirrorTurnSignals'] = ''
            row['Lighting_FogLight'] = specs_dictionary['fogLights']
            row['Lighting_AllWeatherLight'] = ''
            row['Lighting_HeadLightWasher'] = ''
            row['Lighting_AdaptiveHeadlights'] = specs_dictionary['adaptiveHeadlights']
            row['Lighting_HeadLightRangeControl'] = ''
            row['Lighting_AmbientLighting'] = ''
            row['Lighting_DelayedHeadlight'] = ''
            row['Lighting_ReadingLight'] = ''
            row['WindowsandMirrors_PowerWindows'] = specs_dictionary['powerWindows']
            row['WindowsandMirrors_OneTouchPowerWindows'] = ''
            row['WindowsandMirrors_PowerWindowsAntiPinch'] = ''
            row['WindowsandMirrors_AcousticWindows'] = ''
            row['WindowsandMirrors_ExteriorMirrorFunctions'] = specs_dictionary['powerFoldingExteriorMirrors'] +\
                ' PowerFoldingExteriorMirrors' if specs_dictionary['powerFoldingExteriorMirrors'] != 'Not Available' else 'NA'
            row['WindowsandMirrors_InteriorMirrorFunctions'] = ''
            row['WindowsandMirrors_RearWindShieldSunShades'] = ''
            row['WindowsandMirrors_RearPrivacyWindow'] = specs_dictionary['privacyGlass']
            row['WindowsandMirrors_RearWindowSunShield'] = ''
            row['WindowsandMirrors_SunVisor'] = ''
            row['WindowsandMirrors_RearWiper'] = ''
            row['WindowsandMirrors_RainSensorWiper'] = specs_dictionary['rainSensingWindshieldWipers']
            row['WindowsandMirrors_HeatedWindShieldWasherNozzle'] = specs_dictionary['heatedWindshield']
            row['WindowsandMirrors_HeatedMirror'] = specs_dictionary['heatedMirrors']
            row['ClimateControl_AutomaticAC'] = ''
            row['ClimateControl_RearAC'] = ''
            row['ClimateControl_RearVent'] = ''
            row['ClimateControl_DualZoneClimateControl'] = ''
            row['ClimateControl_Airpurifier'] = ''
            row['ClimateControl_FragranceDiffuser'] = ''
            row['ClimateControl_CarRefridgerator'] = specs_dictionary['refrigeratorCooler']
            row['Packages_Packages'] = ''
            row['Convenience_GarageDoorOpener'] = specs_dictionary['integratedGarageDoorOpener']
            row['BasicSpec_PayloadCapacity'] = specs_dictionary['payloadCapacity']
            row['Safety_PedestrianDetection'] = specs_dictionary['pedestrianDetectionSystem']
            row['Exterior_RearSpoiler'] = specs_dictionary['rearSpoiler']
            row['WindowsandMirrors_RearWindowDefroster'] = specs_dictionary['rearWindowDefroster']
            row['Safety_BackupCamera'] = specs_dictionary['rearviewCamera']
            row['Convenience_remoteControlLiftgateTrunkRelease'] = specs_dictionary['remoteControlLiftgateTrunkRelease']
            row['Safety_SideViewCamera'] = specs_dictionary['sideViewCameras']
            row['Safety_SurroundViewCamera'] = specs_dictionary['surroundViewCamera']
            row['Seating_ThridRowSeats'] = specs_dictionary['thirdRow']
            row['Seating_TopViewCamera'] = specs_dictionary['topViewCamera']
            row['EngineandDrivetrain_TurningDiameter'] = specs_dictionary['turningDiameter']
            row['CarPictures'] = row['image_url']
        except KeyError as e:
            print(f"{row['vehicleid']} is missing {e}")

        return row

    def handle(self, *args, **options):
        car_specs_df = self.car_specs_df.apply(self.create_and_mapping_features, axis=1).drop(['_id','basic_info', 'car_make','car_model','car_trim','car_year','query_date','query_url','specs_info','vehicleid', 'status_code','image_url'],axis=1)
        car_specs_df.to_csv('car_specs_df.csv',index=False)
        car_specs_df = car_specs_df.to_dict('records')
        size_of_data = len(car_specs_df)
        k = 100
        i = 0
        while i < k:
            print('saving iter: %s' % i)
            model_instances = [CarSpecsModel(**item) for item in car_specs_df[i*int(size_of_data/k):(i+1)*int(size_of_data/k)] ]
            CarSpecsModel.objects.bulk_create(model_instances)
            i+=1

        model_instances = [CarSpecsModel(**item) for item in car_specs_df[i*int(size_of_data/k):] ]
        CarSpecsModel.objects.bulk_create(model_instances)
        self.stdout.write(self.style.SUCCESS('Successfully write car specs.'))