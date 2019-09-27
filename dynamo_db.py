KEY_SCHEMA = [
    {
        'AttributeName': 'hashed_id',
        'KeyType': 'HASH'
    },
]

ATTRIBUTE_DEFINITIONS = [
    {
        'AttributeName': 'datetime',
        'AttributeType': 'S'
    },

    {
        'AttributeName': 'HouseholdSize',
        'AttributeType': 'N'
    },
    {
        'AttributeName': 'SelectedResidenceCountryId',
        'AttributeType': 'N'
    },
    {
        'AttributeName': 'HousingSize',
        'AttributeType': 'N'
    },
    {
        'AttributeName': 'SelectedHousingTypeOptionId',
        'AttributeType': 'N'
    },
    {
        'AttributeName': 'NotKnownElectricityConsumption',
        'AttributeType': 'BOOL'
    },
    {
        'AttributeName': 'ElectricityConsumption',
        'AttributeType': 'N
    },
    {
        'AttributeName': 'UsageLightbulbs',
        'AttributeType': 'BOOL'
    },
    {
        'AttributeName': 'UsageEnergyStar',
        'AttributeType': 'BOOL'
    },
    {
        'AttributeName': 'UsageThermostat',
        'AttributeType': 'BOOL'
    },
    {
        'AttributeName': 'UsageEnergySavingDevices',
        'AttributeType': 'BOOL'
    },
    {
        'AttributeName': 'UsageSolarWaterHeater',
        'AttributeType': 'BOOL'
    },
    {
        'AttributeName': 'CleanSource',
        'AttributeType': 'N'
    },
    {
        'AttributeName': 'SelectedHeatingSourceOptionId',
        'AttributeType': 'N'
    },


    {
        'AttributeName': 'Intercity',
        'AttributeType': 'N'
    },
    {
        'AttributeName': 'Subway',
        'AttributeType': 'N'
    },
    {
        'AttributeName': 'Bus',
        'AttributeType': 'N'
    },
    {
        'AttributeName': 'CityBus',
        'AttributeType': 'N'
    },
    {
        'AttributeName': 'Tram',
        'AttributeType': 'N'
    },
    {
        'AttributeName': 'BikeWalk',
        'AttributeType': 'N'
    },
    {
        'AttributeName': 'CAR_SelectedFuelTypeOptionId',
        'AttributeType': 'N'
    },
    {
        'AttributeName': 'CAR_AnnualMileage',
        'AttributeType': 'N'
    },
    {
        'AttributeName': 'CAR_AverageConsumption',
        'AttributeType': 'N'
    },
    {
        'AttributeName': 'VeryLongRangeFlight',
        'AttributeType': 'N'
    },
    {
        'AttributeName': 'LongRangeFlight',
        'AttributeType': 'N'
    },
    {
        'AttributeName': 'MediumRangeFlight',
        'AttributeType': 'N'
    },
    {
        'AttributeName': 'ShortRangeFlight',
        'AttributeType': 'N'
    },


    {
        'AttributeName': 'SelectedDietOptionId',
        'AttributeType': 'N'
    },
    {
        'AttributeName': 'SelectedLocalProductsOptionId',
        'AttributeType': 'N'
    },
    {
        'AttributeName': 'SelectedResponsibleCompaniesOptionId',
        'AttributeType': 'N'
    },
    {
        'AttributeName': 'MealsOut',
        'AttributeType': 'N'
    },
    {
        'AttributeName': 'RecycleFood',
        'AttributeType': 'BOOL'
    },
    {
        'AttributeName': 'RecyclePaper',
        'AttributeType': 'BOOL'
    },
    {
        'AttributeName': 'RecycleTinCans',
        'AttributeType': 'BOOL'
    },
    {
        'AttributeName': 'RecyclePlastic',
        'AttributeType': 'BOOL'
    },
    {
        'AttributeName': 'RecycleGlass',
        'AttributeType': 'BOOL'
    },
    
    
    {
        'AttributeName': 'total_annual',
        'AttributeType': 'N'
    },
    {
        'AttributeName': 'country_average',
        'AttributeType': 'N'
    },
    {
        'AttributeName': 'world_average',
        'AttributeType': 'N'
    },
    {
        'AttributeName': 'household',
        'AttributeType': 'N'
    },
    {
        'AttributeName': 'transport',
        'AttributeType': 'N'
    },
    {
        'AttributeName': 'flights',
        'AttributeType': 'N'
    },
    {
        'AttributeName': 'lifestyle',
        'AttributeType': 'N'
    }
]

PROVISIONED_THROUGHPUT = {
    'ReadCapacityUnits': 20,
    'WriteCapacityUnits': 20
}