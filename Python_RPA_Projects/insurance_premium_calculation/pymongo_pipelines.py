# Requires pymongo 3.6.0+
from dataclasses import dataclass
import pandas as pd
from bson.objectid import ObjectId
from utils.dataFrame import enforceColumns
from utils.mongoClient import mongoAggregate, callMongoSubroutine


# Define the OfferData dataclass
@dataclass
class OfferData:
    oib: str
    contractor_oib: str
    firstName: str
    contractor_firstName: str
    lastName: str
    contractor_lastName: str
    customer_type: str
    contractor_type: str
    chassis: str
    reg_prefix: str
    reg_no: str
    reg: str
    street: str
    zip_code: str
    city: str
    full_address: str
    contractor_street: str
    contractor_zip_code: str
    contractor_city: str
    contractor_full_address: str
    leasing: bool
    only_kasko: bool
    bonus: int


def get_offer_data(offer_id):

    """Returns the offer data from MongoDB"""
    try:
        ### aggregation
        # insert collection name
        collection = "collectionName"
        # insert pipeline
        pipeline = [
            {"$match": {"_id": ObjectId(offer_id)}},  # Your query criteria
            {"$project": {
                "Oib": "$sharedData.owner.oib",
                "OwnerFirstName": "$sharedData.owner.firstName",
                "OwnerLastName": "$sharedData.owner.lastName",
                "ContractorOib": "$sharedData.contractor.oib",
                "ContractorFirstName": "$sharedData.contractor.firstName",
                "ContractorLastName": "$sharedData.contractor.lastName",
                "CustomerType": "$sharedData.customerType",
                "ContractorType": "$sharedData.contractor.type",
                "ChassisNumber": "$sharedData.calculationData.vehicle.chassisNumber",
                "RegistrationPrefix": "$sharedData.calculationData.registration.prefix",
                "RegistrationNumber": "$sharedData.calculationData.registration.number",
                "OwnerStreet": "$sharedData.owner.address.streetAndHouseNumber",
                "OwnerZipCode": "$sharedData.owner.address.zipCode",
                "OwnerCity": "$sharedData.owner.address.city",
                "ContractorStreet": "$sharedData.contractor.address.streetAndHouseNumber",
                "ContractorZipCode": "$sharedData.contractor.address.zipCode",
                "ContractorCity": "$sharedData.contractor.address.city",
                # Add other fields as necessary
                "Leasing": "$sharedData.calculationData.isLeasing",
                "OnlyKasko": "$sharedData.calculationData.onlyKasko",
                "InitialBonus": "$sharedData.initialBonus"
            }}
        ]
        # insert additional options example: {"allowDiskUse": True}
        options = {}

        df = pd.json_normalize(mongoAggregate(collection, pipeline, options))
        # example: enforceColumns(df, {
        #   "name": "string",
        #   "isPaid": "bool",
        #   "years": "int",
        #   "amount": "float"
        #   "_id": "ObjectId"
        # })
        # enforceColumns(df, {

        # })
        if 'Leasing' not in df.columns:
            df['Leasing'] = False
        if 'CustomerType' not in df.columns:
            df['CustomerType'] = "person"
        if 'ContractorType' not in df.columns:
            df['ContractorType'] = "person"
        
        df['InsurancePremium'] = None
        df['CommercialDiscount'] = None
        df['AdvisorDiscount'] = None
        df['Status'] = ""
        df['ErrorLog'] = ""
        df['ErrorStage'] = None
        df["Runtime"] = None


        offer_data = OfferData(
            oib=df["Oib"][0],
            contractor_oib=df["ContractorOib"][0],
            firstName=df["OwnerFirstName"][0],
            contractor_firstName=df["ContractorFirstName"][0],
            lastName=df["OwnerLastName"][0],
            contractor_lastName=df["ContractorLastName"][0],
            customer_type=df["CustomerType"][0],
            contractor_type=df["ContractorType"][0],
            chassis=df["ChassisNumber"][0],
            reg_prefix=df["RegistrationPrefix"][0],
            reg_no=df["RegistrationNumber"][0],
            reg=f"{df['RegistrationPrefix'][0]}{df['RegistrationNumber'][0]}",
            street=df["OwnerStreet"][0],
            zip_code=df["OwnerZipCode"][0],
            city=df["OwnerCity"][0],
            full_address=f"{df['OwnerStreet'][0]}, {df['OwnerZipCode'][0]} {df['OwnerCity'][0]}",
            contractor_street=df["ContractorStreet"][0],
            contractor_zip_code=df["ContractorZipCode"][0],
            contractor_city=df["ContractorCity"][0],
            contractor_full_address=f"{df['ContractorStreet'][0]}, {df['ContractorZipCode'][0]} {df['ContractorCity'][0]}",
            leasing=df["Leasing"][0],
            only_kasko=df["OnlyKasko"][0],
            bonus=df["InitialBonus"][0]
        )

        return df, offer_data
    except Exception as e:
        print(f"An error occurred: {str(e)}")
