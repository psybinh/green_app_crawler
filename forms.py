URL = "https://offset.climateneutralnow.org/footprintresult"

HOUSEHOLD = {
    "HouseholdViewModel.HouseholdSize": [i for i in range(1, 9, 1)],
    "HouseholdViewModel.SelectedResidenceCountryId": [35, 33, 45, 72, 80],
    # "HouseholdViewModel.HousingSize": [i for i in range(25, 1000, 10)],
    "HouseholdViewModel.SelectedHousingTypeOptionId": [1, 2, 3, 4],
    
    "HouseholdViewModel.NotKnownElectricityConsumption": [True, False],
    #"HouseholdViewModel.ElectricityConsumption": [i for i in range(12, 3366, 50)],
    #"HouseholdViewModel.UsageLightbulbs": [True, False],
    #"HouseholdViewModel.UsageEnergyStar": [True, False],
    #"HouseholdViewModel.UsageThermostat": [True, False],
    #"HouseholdViewModel.UsageEnergySavingDevices": [True, False],
    #"HouseholdViewModel.UsageSolarWaterHeater": [True, False],
    
    "HouseholdViewModel.CleanSource": [i for i in range(0, 100, 5)],
    "HouseholdViewModel.SelectedHeatingSourceOptionId": [5, 6, 7, 8, 9, 10, 11, 12, 13],
}

TRANSPORT = {
    "TransportViewModel.Intercity": [i for i in range(0, 9)],
    "TransportViewModel.Subway": [i for i in range(0, 12)],
    "TransportViewModel.Bus": [i for i in range(0, 4)],
    "TransportViewModel.CityBus": [i for i in range(0, 6)],
    "TransportViewModel.Tram": [i for i in range(0, 5)],
    "TransportViewModel.BikeWalk": [i for i in range(0, 31)],
    
    #"TransportViewModel.CarUsageList[0].SelectedFuelTypeOptionId": [15, 16, 17, 18],
    #"TransportViewModel.CarUsageList[0].AnnualMileage": [i for i in range(1, 50000, 500)],
    #"TransportViewModel.CarUsageList[0].AverageConsumption": [i for i in range(1, 12, 1)],
    
    "TransportViewModel.VeryLongRangeFlight": [i for i in range(0, 6, 1)],
    "TransportViewModel.LongRangeFlight": [i for i in range(0, 5, 1)],
    "TransportViewModel.MediumRangeFlight": [i for i in range(0, 4, 1)],
    "TransportViewModel.ShortRangeFlight": [i for i in range(0, 61, 1)],
}

LIFESTYLE = {
    "LifestyleViewModel.SelectedDietOptionId": [19, 20, 21, 22, 23],
    "LifestyleViewModel.SelectedLocalProductsOptionId": [24, 25, 26],
    "LifestyleViewModel.SelectedResponsibleCompaniesOptionId": [28, 29, 30],
    "LifestyleViewModel.MealsOut": [i for i in range(0, 15, 1)],
    "LifestyleViewModel.RecycleFood": [True, False],
    "LifestyleViewModel.RecyclePaper": [True, False],
    "LifestyleViewModel.RecycleTinCans": [True, False],
    "LifestyleViewModel.RecyclePlastic": [True, False],
    "LifestyleViewModel.RecycleGlass": [True, False]
}

FORM = {**HOUSEHOLD, **TRANSPORT, **LIFESTYLE}